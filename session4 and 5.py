name = input("what is your name?\n")
age = input("How old are you?\n")
# print("hello, ", name, "!")
age = int(age) # convert string to integer
birth_year = 2024 - age
print(name, ", you were born in ", birth_year, ".", sep="")
print("Hello, " + name + "!")