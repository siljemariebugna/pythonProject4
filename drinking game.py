import random

drinks = ["vodka", "tequila", "rum", "pisco", "rakia", "akvavit", "arak", "ouzo", "gin", "beer", "wine", "malibu", "amaro del capo", "aperol"]
try:
    name = input("what is your name? ")
    age = input("How old are you? ")
    age = int(age) # convert string to integer
except ValueError:
    print("Invalid age. Please enter a number. ")
else:
    # now we have a good age to play with
    if age < 0 or age > 140:
        print("you are not a human")
    elif age > 120:
        print("you are not human")
    elif age < 18:
        print("You are a minor: you cannot play the drinking game. ")
    elif (country == "USA" or country == "UAE") and age < 21:
        print("you are not allowed to drink in UAE or USA. You cant play the awsome game")
    else:
        print("You are an adult. You can play the awsome drinking game my friend. ")
        print("have some", random.choice(drinks), "and enjoy the game mate")
