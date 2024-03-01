def words_b(filename):
    """
    Find 3 lettrs words in the file and print them
    :param filename: name of the file
    :return: nothing
    """
    punctuation = ",!?.\n"
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

# last words becasue end of line has one word more 4 instead of 3, add \n to punctuation to make them appear