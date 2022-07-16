import random


secret = random.randint(1, 30)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")


age = int(input("Please enter your age: "))

if age > 12 and age < 20:
    print("You are a teenager!")

print("END")


if 12 < age < 20:
    print("You are a teenager!")

print("END")

name = input("Please enter your name: ")

if name == "Tina" or name == "TINA":
    print("Hello, Tina!")
