

if number < 1000:
    print("your gross salary is", number - number * 0.1)
elif 1000 < number < 2000:
    print("your gross salary is", number - number * 0.12)
elif 2000 < number < 3000:
    print("your gross salary is", number - number * 0.14)








# 1. What does the following code print?
print(2 * 3 + 5 * 6)
#36 --> integer


# 2. What will the following code print?
print(3 + 10 ** 2/2)
# 53.0 --> float


# 3. Write a function that checks
# if the passed parameter is a valid URL or not
# Also explain your reasoning

import re
def is_valid_url(url):
    # Regular expression pattern for matching URLs
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|[A-Z]|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # domain...
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Check if the passed parameter matches the URL pattern
    if re.match(url_pattern, url):
        return True
    else:
        return False

# Example usage:
url1 = "https://www.example.com"
url2 = "invalid_url"

print("Is", url1, "a valid URL?", is_valid_url(url1))
print("Is", url2, "a valid URL?", is_valid_url(url2))

# The regular expression pattern url_pattern is constructed to match common URL formats,
# including http, https, and ftp protocols.
# It checks for the presence of a protocol followed by
# a domain name and optionally a path.

# The re.match() function is then used to match the URL pattern
# against the passed parameter.

# If the pattern matches,
# the function returns True,
# indicating that the parameter is a valid URL;
# otherwise, it returns False.




# 4. Here is some code:
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1,100))

#Continue by replacing the numbers greater than 80 with their
# corresponding negative value (90 will be replaced with -90)
# print the list at the end
# Continuation of the code...

for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]
print(random_numbers)




#5. What is the maximum values that this code can print?
# Give reasoning
import datetime
import random
today = datetime.date.today() #line gets the current date
start_of_year = datetime.date(today.year, 1, 1) # 1st day of current year
day_of_year = (today - start_of_year).days + 1 #line gets the day of the year

sum = 0
for i in range(day_of_year//10):
    sum += random.randint(1, day_of_year//7)
print(sum)
# --> So, to find the maximum possible value that this code can print,
# we can substitute day_of_year into the formula:
max_value = (day_of_year // 10) * (day_of_year // 7)
print(max_value)



#6. Here is a function that needs to determine if a number is
# smaller, greater, or equal to another number.
# I have written the beginning, please continue
# and paste the entire function in the answer box:
def compare(first, second):
    if first == second:
        print(f"{first} = {second}")
# Now the code is...
def compare(first, second):
    if first == second:
        print(f"{first} = {second}")
    elif first > second:
        print(f"{first} is greater than {second}")
    elif first < second:
        print(f"{first} is smaller than {second}")
first = int(input("Input first number:"))
second = int(input("Input second number:"))
compare(first, second)




#7. What will be the value of a at the end of the code?
a=6
a=a-2
print(a*2)
a=a*2
print(a+1)
a=a//3
# a is 2 (ignore the "print". esos no te dicen el valor de a
# estan ahi solo para confundirte




# 8. Here is a function that determines if a number
# is palindrome or not:
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
# which of the below is NOT A PALINDROME

#example (in the case of numbers, see that the same numbers are going up and down)
#"radar": This is a palindrome because it reads the same forwards and backwards.
# "level": This is a palindrome because it reads the same forwards and backwards.
# "hello": This is NOT a palindrome because it does not read the same forwards and backwards.
# "noon": This is a palindrome because it reads the same forwards and backwards.




# 9. Please explain what it means that a list is mutable
# and a string is not mutable
# Give some code that shows the difference

# Mutable objects: Lists, dictionaries, and sets are examples.
#This means that you can modify their elements or contents after they have been created.
# Mutable example - List
my_list = [1, 2, 3]
print("Original list:", my_list)

# Modify the list
my_list[0] = 100
print("Modified list:", my_list)
#In this example, we create a list [1, 2, 3] and then modify its first element to 100.
# Lists are mutable, so we can change their elements after creation.

# Immutable objects: Strings, tuples, and frozensets are examples.
# Once created, their contents cannot be modified or changed.
# Immutable example - String
my_string = "hello"
print("Original string:", my_string)

# Try to modify the string
try:
    my_string[0] = 'H'
except TypeError as e:
    print("Error:", e)
# we create a string "hello".
# Then, we attempt to modify its first character to 'H'.
# However, this operation raises a TypeError because strings are immutable,
# and their characters cannot be changed after creation.




# 10. Fill in what the code below prints (all the lines):
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
#This section gets the current date and extracts the day of the week
# (as an integer, where Monday is 0 and Sunday is 6)
# and the month of the year (as an integer, where January is 1 and December is 12).

a = a + day_of_week
b += month_of_year
# a is updated by adding the day of the week to its current value,
# and b is updated by adding the month of the year to its current value.

print(a)
print(b)
c = a+b
print(c)
d = "abc" * (c//3)
print(d)

#6 is a --> a can be between 3 and 9
#8 is b --> b can be between 4 and 16
#14 is c --> c is the sum of a and b
#abcabcabcabc --> d is the string "abc" repeated (c // 3) times





#extra:
# define a function that read you or else
# Here's a Python function that prompts the user to input a value.
# It will keep prompting until the user enters a valid input (i.e., not an empty string).
def read_input(prompt="Enter input: "):
    while True:
        user_input = input(prompt)
        if user_input.strip():  # Check if the input is not empty after stripping whitespace
            return user_input

# Example usage:
user_input = read_input("Please enter your name: ")
print("Hello,", user_input)
#This function continuously prompts the user to enter input until a non-empty string is provided.
# Once a valid input is received, it returns the input value.
# You can customize the prompt message by passing a string to the prompt parameter.







if number < 1000:
    print("your gross salary is", number - number * 0.1)
elif 1000 < number < 2000:
    print("your gross salary is", number - number * 0.12)
elif 2000 < number < 3000:
    print("your gross salary is", number - number * 0.14)


