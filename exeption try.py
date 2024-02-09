name = input("what is your name?\n")
age = input("How old are you?\n")
try:
    age = int(age) # convert string to integer
    birth_year = 2024 - age
    print(name, ", you were born in ", birth_year, ".", sep="")
    number = input("give me a number to divide the age ")
    number = int(number)
    print(age/number)
except ValueError:
    print("invalid age. please enter a number")
except ZeroDivisionError:
    print("you cannot divide by zero. ")
except:
    print("some error i did not forsee")
else:
    print("no exceptions were raised")
finally:
    print("bye")