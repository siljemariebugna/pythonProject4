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

#4

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

input_word = "16237434848585"
result = palindrome(input_word)
print(f"Is '{input_word}' a palindrome? {result}")

#5
def count_bob(text):
    # Initialize a counter for the number of occurrences
    occurrences = 0

    # Iterate through the characters in text
    for i in range(len(text) - 2):
        # Check if the current character is 'b'
        if text[i] == 'b':
            # Check if the next characters form the pattern "Bob"
            if text[i+1:i+4] == "ob":
                # Increment the occurrences counter
                occurrences += 1

    return occurrences

text_to_search = "Bob is a bobcat, and Bobby loves Bob's burgers. Bob is the best!"
result = count_bob(text_to_search)
print(f"Number of occurrences of the pattern 'b...Bob': {result}")

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

#8
import re

def is_valid_url(url):
    # Define a regular expression pattern for a simple URL validation
    url_pattern = re.compile(
        r'^(https?|ftp):\/\/'  # Scheme (http, https, ftp)
        r'([a-zA-Z0-9.-]+)'    # Domain (may include subdomains)
        r'(\.[a-zA-Z]{2,})'     # Top-level domain (e.g., .com, .org)
        r'(:\d{1,5})?'          # Port (optional)
        r'(\/[^\s]*)?$'         # Path (optional)
    )

    # Check if the provided URL matches the pattern
    return bool(re.match(url_pattern, url))

# Test cases
url1 = "https://www.example.com"
url2 = "ftp://ftp.example.org"
url3 = "invalid-url"
url4 = "http://localhost:8080/path/to/page"

print(f"Is '{url1}' a valid URL? {is_valid_url(url1)}")
print(f"Is '{url2}' a valid URL? {is_valid_url(url2)}")
print(f"Is '{url3}' a valid URL? {is_valid_url(url3)}")
print(f"Is '{url4}' a valid URL? {is_valid_url(url4)}")

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




