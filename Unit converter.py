str_greeting = "Welcome to unit converter! Unit converter will convert kilometers in to miles."
str_prompt = "Enter distance in kilometers: "
str_miles1 = "That is "
str_miles2 = " miles."
str_replay = "Would you like to do another conversion (yes/no)? "
str_replay_response = ""
str_error = "I'm sorry, wrong input. Please try again."
replay = True
replay_prompt = True


print(str_greeting)

while replay == True:
    kilometers = input(str_prompt)
    print()
    str_miles_amount = str(int(kilometers)/1.609344)
    print(f"{str_miles1} {str_miles_amount} {str_miles2}")
    print()
    replay_prompt = True

    while replay_prompt == True:
        str_replay_response = input(str_replay)
        if str_replay_response.lower() == "no":
            replay = False
            break
        elif str_replay_response.lower() == "yes":
            replay_prompt = False
        else:
            print(str_error)
