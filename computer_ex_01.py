import random


def guess(x):
    Random_number = random.randint(1,x)
    guess = 0
    while guess != Random_number:
        guess = int(input(f"Guess an number bettween 1 to {x}: "))
        if guess < Random_number:
            print(f"Sorry ! but your Guess too low")
        elif guess >Random_number:
            print("Sorry!but your Guess is too high ")
    print(f"yey!!!! your have Guessed number {Random_number} corrently")


guess(10)