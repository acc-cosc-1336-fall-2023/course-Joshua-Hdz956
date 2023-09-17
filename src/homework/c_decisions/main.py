import decisions
#while loop to force user to input an integer instead of giving an error.
while True:
    try:
        options = int(input(" Input your option: "))
        break
    except ValueError:
        print ("That option is invalid. Input an integer for your option. ")
while True:
    try:
        total = int(input(" Enter your Total: "))
        break
    except ValueError:
        print ("That total is invalid. Input an integer for your total. ")

result = decisions.get_options_ratio(options, total)

print("Your rating is: " + decisions.get_faculty_rating(result))


