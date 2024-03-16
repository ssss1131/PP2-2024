import psycopg2
import csv


def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts
            (name VARCHAR(100),
            phone VARCHAR(20));
        """)
    conn.commit()


def person_exists(conn, name, phone):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM contacts WHERE name = %s OR phone = %s", (name, phone))
        return cur.fetchone() is not None  # тут просто чекает если cur.fetchone NONE то это FALSE а если он не NONE то TRUE


def person_with_phone_exists(conn, name, phone):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM contacts WHERE name = %s and phone = %s", (name, phone))
        return cur.fetchone() is not None


def add_person(conn, name, phone):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (
            name, phone))  # %s чтобы избежать чтоб чел не сделал SQL-инъекций типа пишет "'; DROP TABLE users; --"
        # и удаляет с кайфом а %s как бы реально добавляет такое имя и номер игнорируя ; или другие команды
    conn.commit()


def add_many_person(conn, names):
    for user in names:
        name, phone = user

        if not person_exists(conn,name,phone):
            add_person(conn, name, phone)
        else:
            update(conn,None,phone,name)


def update(conn, new_name, phone, old_name):
    with conn.cursor() as cur:
        if new_name:
            if not person_exists(connection, new_name, new_name):
                cur.execute("UPDATE contacts SET name=%s WHERE name=%s", (new_name, old_name))
        elif phone:
            if not person_exists(connection, phone, phone):
                cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (phone, old_name))
        conn.commit()


def delete(conn, name, phone):
    with conn.cursor() as cur:
        if name is not None:
            cur.execute("DELETE FROM contacts WHERE name =%s", (name,))
        else:
            cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))

    print("Successfully")
    conn.commit()


def commands():
    print("""
    1. Add new person
    2. Update exist person
    3. Delete person 
    4. Filter
    5. Add new persons
    6. Exit
    """)


def read_from_file(conn, path):
    with open(path, mode="r") as cs:
        reader = csv.reader(cs)
        next(reader)
        for line in reader:
            with conn.cursor() as cur:
                if not person_exists(connection, line[0], line[1]):
                    cur.execute("INSERT INTO contacts(name,phone) VALUES(%s,%s)", (line[0], line[1]))

        conn.commit()


def show_data(list_of_data):
    for item in list_of_data:
        print(f"{item[0]}: {item[1]}")


def filter(conn, choice, filter):
    with conn.cursor() as cur:
        if choice == 1:
            cur.execute("SELECT * FROM contacts WHERE name LIKE %s", (
                filter + '%',))  # Символ % в SQL выполняет роль "шаблона", который может соответствовать любой последовательности символов (включая их отсутствие).
            print(f"This is all name that start with {filter}:")
            show_data(cur.fetchall())

        elif choice == 2:
            cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (filter + '%',))
            print(f"This is all phone number that start with {filter}:")
            show_data(cur.fetchall())

        elif choice == 3:
            cur.execute(f"SELECT * FROM contacts WHERE LENGTH(PHONE)<%s", (filter,))
            print(f"this is all phone number that length is less than {filter}:")
            show_data(cur.fetchall())
        elif choice == 4:
            cur.execute(f"SELECT * FROM contacts")
            print(f"All contacts:")
            show_data(cur.fetchall())
        elif choice == 5:
            cur.execute("SELECT * FROM contacts LIMIT %s OFFSET %s", (filter[0], filter[1]))
            print(f"All contacts with limit and offset: ")
            show_data(cur.fetchall())
        elif choice == 6:
            name_pattern = f"%{filter[0]}%"
            phone_pattern = f"%{filter[1]}%"
            cur.execute("SELECT * FROM contacts WHERE name LIKE %s OR phone LIKE %s", (name_pattern, phone_pattern))
            show_data(cur.fetchall())


if __name__ == "__main__":  # это короч чтобы при импорте данного файла этот скрипт не робил
    connection = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="phonebook",
            user="postgres",
            password="1337"
        )
        create_table(connection)  # Создание таблицы
        read_from_file(connection, "prob.csv")
        while True:
            commands()  # Отображение команд
            choice = input("Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 6:
                    break
                elif choice == 5:
                    many_names = []
                    while True:
                        inputs = input("Enter name and phone number (separated by comma), enter 'stop' to complete:\n")
                        if inputs == "stop":
                            break
                        name, phone = inputs.split(',')
                        if phone.isdigit():
                            many_names.append((name.strip(),
                                           phone.strip()))  # strip убирает табуляции можно чета внутрь написать чтобы именно его убрать
                        else:
                            print("Please enter valid phone number")

                    add_many_person(connection, many_names)

                    print("added succecfully")

                elif choice == 1:
                    name = input("Enter your name: ")
                    phone = input("Enter your phone number: ")
                    if not person_exists(connection, name, phone):
                        add_person(connection, name, phone)
                        print("Person added successfully.")
                    else:
                        if not person_with_phone_exists(connection, name, phone):
                            update(connection, None, phone, name)
                            print("New phone added succecfully.")
                        else:
                            print("Person with this name and phone already exists")

                elif choice == 2:
                    updating = int(input("What you want update:\n1-name\n2-phone number\n"))
                    if updating == 1:
                        old_name = input("Enter old name: ")
                        new_name = input("Enter new name: ")
                        update(connection, new_name, None, old_name)
                    elif updating == 2:
                        name = input("Enter your name: ")
                        new_phone = input("Enter your new phone: ")
                        update(connection, None, new_phone, name)

                elif choice == 3:
                    deleting = input("Please enter name or phone that you want delete: ")
                    if person_exists(connection, deleting, deleting):
                        if deleting.isdigit():
                            delete(connection, None, deleting)
                        else:
                            delete(connection, deleting, None)

                    else:
                        print("person or phone does not exist")

                elif choice == 4:
                    filters = int(input(
                        "How you want filter\n1.by name that start with \n2.by phone that start with\n3.show phone that len is less than \n4.show all table\n5.show names and phones with limit and offset\n6.show name or phone like:\n "))

                    if filters == 1:
                        start_name = input("Enter letters that should with name start: ")
                        filter(connection, filters, start_name)
                    elif filters == 2:
                        start_phone = input("Enter numbers that should with phone start: ")
                        filter(connection, filters, start_phone)
                    elif filters == 3:
                        len_phone = input("Enter length that phone should be less than: ")
                        filter(connection, filters, len_phone)
                    elif filters == 4:
                        filter(connection, 4, None)
                    elif filters == 5:
                        limit = input("Enter limit:")
                        Offset = input("Enter offset: ")
                        filter(connection, 5, [limit, Offset])
                    elif filters == 6:
                        name = input("Enter name: ")
                        phone = input("Enter phone: ")
                        filter(connection, 6, [name, phone])





            else:
                print("Please enter a valid number.")

    except psycopg2.DatabaseError as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection is not None:
            connection.close()
