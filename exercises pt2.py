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


