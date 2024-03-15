import pygame
from random import randint, choice
import psycopg2
from datetime import datetime
import json

# короче где то тут я apple два раза видимо добавляю из за этого score в два раза больше еще тут из багов яблоко внутри стены может чисто из за того что
# я чекаю чтобы стены не появились в яблоках или в змее но не чекаю чтобы яблоки не появились внутри стен
# мб база данных тупит временами
connection = psycopg2.connect(
    host="localhost",
    database="snake_game",
    user="postgres",
    password="1337"
)

pygame.init()

width, height = 600, 600
previous_key = pygame.K_UP  # начальное направление
speed_of_snake = 5  # скорость перемещение х у для элементов Snake
size_of_segments = 20
segments = [(width // 2, height // 2)]
apples = []
apples_gold = []
walls = []
rect_of_head = pygame.Rect(0, 0, 0, 0)
snake_length = 2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
walls_count = 2
timer_walls = 0
timer_wall_bool = False

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
game_over = pygame.image.load("game_over.png")
background = pygame.image.load("background.png")

font = pygame.font.SysFont("vrinda", 50)
score = 0
last_score = 0
apple = None
gold_check = 0

game = True
loser = False
gold_eaten = False
gold_timer = False
timer = 0

Enter_name = pygame.image.load("ENTER_NAME.png")
font_user = pygame.font.Font(None, 32)
font_table = pygame.font.SysFont(None, 24)
font_snake = pygame.font.SysFont(None, 25)
input_box_color = pygame.Color('Blue')
text_color = pygame.Color('pink')
input_box = pygame.Rect(width // 2 - 90, width // 2 + 28, 1,
                        30)  # ну ширина потом полибому поменяется поэтому без разницы какой будет
user_text = ''
active = False
enter_game = True

pause_image = pygame.image.load("pause.png")
pause_menu = pygame.image.load("pause.menu.png")
pause_box = pygame.Rect(width - pause_image.get_width(), 0, pause_image.get_width(), pause_image.get_height())
pause = False
save_rect_collided = False
continue_rect = pygame.Rect(119, 135, 95, 130)
save_rect = pygame.Rect(250, 190, 137, 110)
exit_rect = pygame.Rect(407, 194, 130, 119)
saved_games_rect = pygame.Rect(162, 475, 312, 60)
DATA_rect = pygame.Rect(145, 450, 314, 48)
DATA_rect_collided = False
# Отступы
padding = 10
header_height = 50
palette_colors = [
    (0, 0, 0),  # Черный
    (0, 255, 0),  # Зеленый
    (0, 0, 255),  # Синий
    (0, 255, 255),  # Голубой (Циан)
    (255, 0, 255),  # Пурпурный (Маджента)
]


class Snake:
    def __init__(self, segment):
        self.speed = speed_of_snake
        self.segment = segment  # массив с кортежами для каждого элемента змеи начиная с головы
        self.length = snake_length  # начальная длина змеи
        self.direction = previous_key  # начальное направление змеи

    def move(self):
        global rect_of_head, loser, gold_eaten, gold_check
        x, y = self.segment[0]  # начальные координаты змеи до движение
        new_head = 0
        if self.direction == pygame.K_UP:
            new_head = (x, y - self.speed)  # координаты для головы меняются
        elif self.direction == pygame.K_DOWN:
            new_head = (x, y + self.speed)
        elif self.direction == pygame.K_LEFT:
            new_head = (x - self.speed, y)
        elif self.direction == pygame.K_RIGHT:
            new_head = (x + self.speed, y)

        rect_of_head = pygame.Rect(new_head, (size_of_segments, size_of_segments))
        self.segment.insert(0, new_head)  # добавляю новые координаты головы а старые координаты превращаются в его тело
        if len(self.segment) != self.length and not gold_eaten:  # если в длине сегмента по сути сбор голов не равен реальной длине змеи то значит она не сьела яблоко
            self.segment.pop()  # и соответственно надо убрать самую первую голову а значит хвост данной змеи
        if gold_eaten:
            gold_check += 1
        if gold_check == 10:  # счетчик чтобы при сьеданий золотой размер змеи увеличилась на 10 сегментов
            gold_eaten = False
            gold_check = 0
        # print(len(self.segment))

        if new_head in self.segment[1:]:
            loser = True  # если обнаружено столкновение
            lose()
            return  # Выхожу чтобы предотвратить дальнейшее движение

    def grow(self, weight):
        global snake_length
        self.length += weight
        snake_length += weight
        # print(f"segment :  {len(self.segment)}")
        # print(f"length :  {self.length}")

    def draw(self):
        for i, segmenta in enumerate(
                self.segment):  # рисую каждый элемент в сегмент а значит каждый блок змеи начиная с головы
            pygame.draw.rect(screen, pygame.Color("Green"),
                             pygame.Rect(segmenta[0], segmenta[1], size_of_segments, size_of_segments))
            text_for_snake = font_snake.render(f"{i}", True, (255, 255, 255))
            screen.blit(text_for_snake, (segmenta[0], segmenta[1]))


class Apple:
    def __init__(self, segments, color, weight):
        collision = True
        while collision:
            collision = False
            self.x = randint(size_of_segments, width - size_of_segments)
            self.y = randint(size_of_segments, height - size_of_segments)
            self.rect = pygame.Rect(self.x, self.y, size_of_segments, size_of_segments)
            self.color = color
            self.weight = weight
            for segment in segments:
                if self.rect.colliderect(
                        pygame.Rect(segment[0], segment[1], size_of_segments, size_of_segments)):
                    collision = True
                    break

        if (weight == 1):
            apples.append(self)
        elif (weight == 5):
            apples_gold.append(self)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


class Wall:
    def __init__(self):
        collision = True
        while collision:
            collision = False
            self.length_x = randint(size_of_segments, 50)
            self.length_y = randint(size_of_segments, 50)
            self.x = randint(0, width - self.length_x)
            self.y = randint(0, height - self.length_y)
            self.rect = pygame.Rect(self.x, self.y, self.length_x, self.length_y)
            self.color = pygame.Color("Grey")
            if is_too_close_to_snake_head(self.x, self.y):
                collision = True
                continue

            for segment in segments:
                if self.rect.colliderect(
                        pygame.Rect(segment[0], segment[1], size_of_segments, size_of_segments)):
                    collision = True
                    break
            for apple in apples:
                if self.rect.colliderect(apple.rect):
                    collision = True
                    break
            for apple in apples_gold:
                if self.rect.colliderect(apple.rect):
                    collision = True
                    break
        walls.append(self)

    def draw(self):
        global loser
        if self.rect.colliderect(rect_of_head):
            loser = True
            lose()
        else:
            pygame.draw.rect(screen, self.color,
                             (self.x, self.y, self.length_x , self.length_y))


def lose():
    global segments, snake, previous_key, apples, score, last_score, gold_eaten, gold_timer, timer, apples_gold, user_text, speed_of_snake, snake_length,walls,walls_count
    screen.fill(pygame.Color("Black"))
    segments = [(width // 2, height // 2)]
    previous_key = pygame.K_UP
    score_text = font.render(f"{score // 2}", True, (255, 255, 255))
    with connection.cursor() as cur:
        cur.execute("SELECT score FROM users WHERE name=%s", (user_text,))
        result = cur.fetchone()
        if result is not None:
            if score > result[0]:
                cur.execute(f"UPDATE users  SET score={score / 2} WHERE name=%s", (user_text,))
        connection.commit()

    speed_of_snake = 5
    snake_length = 2
    score = 0
    last_score = 0
    snake = Snake(segments)
    apples = []
    apples_gold = []
    screen.blit(game_over, (0, 0))
    screen.blit(score_text, (292, 280))
    gold_eaten = False
    gold_timer = False
    timer = 0
    last_score = 0
    walls_count=2
    walls.clear()

def is_too_close_to_snake_head(x, y, radius=100):
    head_x, head_y = segments[0]
    distance = ((head_x - x) ** 2 + (head_y - y) ** 2) ** 0.5
    return distance < radius



def save_game(player_name):
    game_state = {
        "snake_position": segments,
        "direction": previous_key,
        "score": score / 2,
        "speed": speed_of_snake,
        "length": snake_length
    }
    save_date = datetime.now()
    with connection.cursor() as cur:
        state_json = json.dumps(game_state)
        cur.execute(
            "INSERT INTO saved_games (player_name, state, save_date, score) VALUES (%s, %s, %s, %s)",
            (player_name, state_json, save_date, game_state['score'])
        )
        connection.commit()


def draw_table(data):
    # Отрисовка заголовка
    screen.fill(WHITE)
    name_text = font_table.render("Name", True, BLACK)
    date_text = font_table.render("Date", True, BLACK)
    score_text = font_table.render("Score", True, BLACK)
    # Вычисление позиций для заголовков столбцов
    name_x = padding
    date_x = width // 3
    score_x = width // 3 * 2

    # Отрисовка заголовков столбцов
    screen.blit(name_text, (name_x, header_height))
    screen.blit(date_text, (date_x, header_height))
    screen.blit(score_text, (score_x, header_height))

    # Отрисовка строк таблицы
    y = header_height * 2
    for entry in data:
        name, save_date, score = entry
        date_str = save_date.strftime("%Y-%m-%d %H:%M")

        name_text = font_table.render(name, True, BLACK)
        date_text = font_table.render(date_str, True, BLACK)
        score_text = font_table.render(str(score), True, BLACK)

        screen.blit(name_text, (name_x, y))
        screen.blit(date_text, (date_x, y))
        screen.blit(score_text, (score_x, y))

        y += font.get_height() + padding


def check_click_on_table(mouse_pos, data):
    global enter_game, save_rect_collided, DATA_rect_collided, pause
    # Позиция клика
    mx, my = mouse_pos

    # Позиции строк
    row_y = header_height * 2
    row_height = font.get_height() + padding

    for i, entry in enumerate(data):
        # Определение границ строки
        if row_y <= my < row_y + row_height:
            load_saved_game(entry[0], i)
            DATA_rect_collided = False
            enter_game = False
            save_rect_collided = False
            pause = False
            return None
        row_y += row_height

    return None  # Ничего не выбрано


def get_data():
    with connection.cursor() as cur:
        cur.execute("SELECT player_name, save_date, score FROM saved_games ORDER BY save_date DESC")
        return cur.fetchall()[::-1]


def load_saved_game(name, id):
    global user_text, segments, previous_key, score, speed_of_snake, snake_length
    user_text = name
    with connection.cursor() as cur:
        cur.execute("SELECT state FROM saved_games WHERE id = %s ", (id + 1,))
        result = cur.fetchone()
        if result:
            game_state = result[0]
            segments = game_state["snake_position"]
            previous_key = game_state["direction"]
            score = int(game_state["score"]) * 2
            speed_of_snake = game_state["speed"]
            snake_length = game_state["length"]
            snake.segment = segments
            snake.direction = previous_key
            snake.speed = speed_of_snake
            snake.length = snake_length
            return None


snake = Snake(segments)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            connection.close()
            pygame.quit()
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and enter_game:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
            if saved_games_rect.collidepoint(event.pos):
                save_rect_collided = True
            if save_rect_collided:
                data = get_data()
                draw_table(data)
                check_click_on_table(event.pos, data)

        elif event.type == pygame.MOUSEBUTTONDOWN and not enter_game:
            if pause_box.collidepoint(event.pos):
                pause = True
                screen.blit(pause_menu, (0, 0))

            elif continue_rect.collidepoint(event.pos) and pause:
                pause = False

            elif save_rect.collidepoint(event.pos) and pause:
                save_game(user_text)


            elif exit_rect.collidepoint(event.pos) and pause:
                connection.close()
                pygame.quit()
                game = False

            elif (DATA_rect.collidepoint(event.pos) and pause) or DATA_rect_collided and pause:
                data = get_data()
                draw_table(data)
                check_click_on_table(event.pos, data)
                DATA_rect_collided = True


        elif event.type == pygame.KEYDOWN:
            if active and enter_game:
                if event.key == pygame.K_RETURN:
                    with connection.cursor() as cur:
                        # Проверяем, существует ли уже пользователь с таким именем в базе данных
                        cur.execute("SELECT * FROM users WHERE name = %s", (user_text,))
                        result = cur.fetchone()
                        # Если пользователь не найден, добавляем его с начальным счетом 0
                        if result is None:
                            cur.execute("INSERT INTO users (name, score) VALUES (%s, %s)", (user_text, 0))
                            connection.commit()
                    active = False
                    enter_game = False
                    loser = False

                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

            if not loser:
                if event.key == pygame.K_UP and previous_key != pygame.K_DOWN:
                    previous_key = pygame.K_UP
                    snake.direction = pygame.K_UP
                elif event.key == pygame.K_DOWN and previous_key != pygame.K_UP:
                    previous_key = pygame.K_DOWN
                    snake.direction = pygame.K_DOWN
                elif event.key == pygame.K_LEFT and previous_key != pygame.K_RIGHT:
                    previous_key = pygame.K_LEFT
                    snake.direction = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and previous_key != pygame.K_LEFT:
                    previous_key = pygame.K_RIGHT
                    snake.direction = pygame.K_RIGHT
            elif loser and not enter_game:
                if event.key == pygame.K_SPACE:
                    loser = False

    if enter_game and not save_rect_collided:
        screen.blit(Enter_name, (0, 0))
        txt_surface = font.render(user_text, True, text_color)
        input_box.w = max(200,
                          txt_surface.get_width() + 10)  # короч тут если он напишет очень много то видх текста станет куда больше а если убрать 200 то он будет супер маленьким попасть тяжко будет
        pygame.draw.rect(screen, input_box_color, input_box)
        screen.blit(txt_surface, (input_box.x, input_box.y))

    if not loser and not pause and not enter_game:
        screen.blit(background, (0, 0))
        screen.blit(pause_image, (pause_box[0], pause_box[1]))
        if not apples:
            apples.append(
                Apple(snake.segment, pygame.Color("red"), 1))  # Теперь добавляем экземпляр класса Apple в список4

        for ap in apples:
            ap.draw()
            if ap.rect.colliderect(rect_of_head):
                apples.remove(ap)  # Удаляем яблоко из списка
                snake.grow(ap.weight)
                score += 1
        if not apples_gold:
            if randint(0, 10000) > 9600:
                apples_gold.append(Apple(snake.segment, pygame.Color("Gold"), 5))
                timer = 100
                gold_timer = True
        if gold_timer and timer > 0:
            timer -= 1
        elif gold_timer and timer <= 0:
            apples_gold.clear()  # Удаляем золотое яблоко после истечения времени
            gold_timer = False
        for app in apples_gold:
            app.draw()
            if app.rect.colliderect(rect_of_head):
                apples_gold.remove(app)  # Удаляем яблоко из списка
                snake.grow(app.weight)
                gold_eaten = True
                gold_timer = False
                score += 3

        if (rect_of_head.right > width or rect_of_head.left < 0 or
                rect_of_head.bottom > height or rect_of_head.top < 0):
            loser = True
            lose()

        if len(walls) != walls_count:
            Wall()
            timer_walls = 1000

        if timer_walls > 0:
            timer_walls -= 1
        elif timer_walls <= 0:
            timer_wall_bool = True
            walls.clear()

        if score > last_score + 20:
            walls.clear()
            walls_count += 2
            last_score = score
            snake.speed += 2
            speed_of_snake += 2

        snake.move()
        if not (loser or pause):  # без него он рисует и змейка остается когда игра уже закончилась
            snake.draw()
            for wall in walls:
                wall.draw()

    pygame.display.update()
    pygame.time.Clock().tick(60)
