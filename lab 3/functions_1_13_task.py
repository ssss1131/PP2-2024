from random import randint

def guesses(number,name):
    guess = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n"))
    overall = 1
    while guess != number:
        if guess < number:
            guess = int(input("Your guess is too low.\nTake a guess.\n"))
        elif guess > number:
            guess = int(input("Your guess is too high.\nTake a guess.\n"))
        overall += 1
    return overall

'''
number = randint(1, 20)
name = input("Hello! What is your name?\n")
overall= guesses(number,name)

print(f"Good job, {name}! You guessed my number in {overall} guesses!")
'''