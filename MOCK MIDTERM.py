# 2 + 3 # int
 # how can python tell u what function is beign used IDLE!!!!!!!!!!!!!!!!!!!!!
# 6/2                is float cause dividing in phytin the result is always a float
# 2 ! = 3            (not equal) is bool, bool is true or false
# 5 or 6             is int
# print(2*2)         is a nontype, because the function return differently
# "abc".find         function
# "bubu"*2           string
# "bubu"*(4/2)       this is an error, u cant multiply with float
# ["abc", 2]         is a simple list
# (2)          is an int

# indicate result of options (also use IDLE)
# 6/2              is 3.0
# 2 != (not equal) 3           is false (true and false is spelled with capitals)
# 5 or 6             result is 5
# 5 and 6            result is 7 (and is last or is first)
# [1,2,3].append("Jhon")           result is none (return value is none, append is for lists)
# bubu* 4/2          cant moliply string with float
# len(("abc", 2)) result is 2, 2 is leghts of list
# 2 + 3 * 2 **2 the result is 14, reason: order of operation

# instead of sep, end is parameter called end, replaces final new line, allows to change new line
# +=      is addition
# a == 5   is not stored anywhere
# abc * 4-3 = abc
# if abc * 0       the result is an empty string

# write the function that takes the name of a text file as a parameter, print out the three letter words that start with b
# write a function that takes an integer as parameter and returns a list of all the divisors of that number
# eg 47 -> [1,47], 28 -> [1,2,4,7,14,28]

# write a function that forces the user to enter a multiple of 6 number use try and except to find invalid inpits
def m6():
    """
    a function that returns a multiple of 6
    :return: the multiple of 6 number entered by the user
    """

    while True:
        try:
            # first we need to read a number
            number = input("Please give me a multiple of 6 number ") #string to convert to integer
            number = int(number)
        except ValueError:
            # is number is not valid print error and retry
            print("Thats not a number. Retry")
            continue
        # check if number is multiple of 6
        if number % 6 == 0:
            # return the value
             return number
        # print an error and try again
        print("That number is not a multiple of 6. Retry")
# testing out function by calling it
print("A multiple of 6 number is", m6())


#justifications in the code


def words_b(filename):
    """
    Find 3 lettrs words in the file and print them
    :param filename: name of the file
    :return: nothing
    """
    punctuation = ",!?."
    # open file
    with open(filename, "r") as file:
        # go over file line by line
        for line in file:
            for p in punctuation:
                line = line.replace(p, "") #replace punctuation with nothing
            # get the words in line
            words = line.split(" ")
            for word in words:
                if len(word) == 3 and word.startswith("b"):
                    print(word)
    return
# call function
words_b("txt.file.midt")








