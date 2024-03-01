# 1
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a)

#2
print((3+10**2/2) or 70.0)

#3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)



# 6
string = "mammamia"
print(string[1])
# string[1] = "b"

list_s = [3, 4, 5, 8, 9]
list_s[3] = 6
print(list_s)

#7

import random

random_numbers = []

# Make a list of 10 random numbers between 1 and 100
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Print the list
print("List:", random_numbers)

# Replace the numbers greater than 80 with their corresponding negative values
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]

# Print the new list
print("New List:", random_numbers)

#9
def days_since_birthday(birthday):
    # Extract day, month, and year from the string
    day, month, year = map(int, birthday.split('-'))

    # Get the current date
    current_date = "01-01-2024"  # to be replaced with current date
    current_day, current_month, current_year = map(int, current_date.split('-'))

    # Find the number of years since birthday
    years_passed = current_year - year - 1

    # Find the days remaining in the this year
    days_remaining = (31 - day) + ((12 - month) * 31)  # Assuming all months have 31 days

    # Calculate days passed
    total_days_passed = (years_passed * 365) + days_remaining

    return total_days_passed

birthday = "10-05-2003"  # my birthday
days_passed = days_since_birthday(birthday)
print(f"Days passed since {birthday}: {days_passed}")

