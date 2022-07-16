prompt = "Enter a number between 1 and 100: "

number = 1
number_user = int(input(prompt))

while number <= number_user:
    if number%3 == 0 and number%5 == 0:
        print("fizzbuzz")
    elif number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    else:
        print(number)
    number = number + 1
