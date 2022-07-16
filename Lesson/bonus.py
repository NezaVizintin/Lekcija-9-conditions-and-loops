str_one = "Happy"
str_two = "Day"

print("%s %s" % (str_one, str_two))
print("{0} {1}".format(str_one, str_two))
print("{first_str} {second_str}".format(first_str=str_one, second_str=str_two))
print(f"{str_one} {str_two}") #f-string method - newest

#The preferred options are using the .format() method or using f-strings.