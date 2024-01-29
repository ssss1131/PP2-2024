from itertools import permutations


# 1
def gramm_to_ounces(dict_1):
    x = dict_1.values()
    for i in x:
        print(i * 28.3495231)


dict_1 = {
    "sugar": 10,
    "sodium": 15,
    "uranium": 200,
    "water": 1000
}
"""gramm_to_ounces(dict_1)
"""


# 2
def f_to_t(F):
    return (5 / 9) * (F - 32)


'''
F=273
print(f"{F} Fahrenheit to temperature is {f_to_t(F)}")
'''


# 3
def solve(numheads, numlegs):
    if numheads * 2 != numlegs:
        return f"number of rabbits {(numlegs - numheads * 2) / 2} and chickens {numheads - (numlegs - numheads * 2) / 2} "
    else:
        return f"number of chickens {numheads} and no rabbits"


# print(solve(35,94))

# 4
list_of_numbers = [2, 3, 4, 5, 6, 100, 200, 300, 17, 97, 60, 50]


def only_prime(lists):
    list_prime = []
    for i in range(0, len(lists) - 1):
        x = lists[i]
        if (x == 2):
            list_prime.append(x)
        elif (x == 3):
            list_prime.append(x)

        for i in range(2, int(x ** 0.5) + 1):
            if x % i != 0:
                if (i == int(x ** 0.5)):
                    list_prime.append(x)
                continue

            else:
                break
    return list_prime


# print(only_prime(list_of_numbers))

# 5
string_2 = "What is love"


def string(str):
    list_of_string = list(str.split(" "))
    perm = permutations(list_of_string)
    stri = ""
    for i in perm:
        for j in i:
            stri += j+" "
        print (stri)
        stri=""

string(string_2)


# 6

# string_1 = "One piece is real"


def reverse(string):
    list_of_string = list(string.split(" "))
    list_of_string = list_of_string[::-1]
    string_reversed = ""
    for i in list_of_string:
        string_reversed += i
        string_reversed += " "
    return string_reversed

# print(reverse(string_1))


