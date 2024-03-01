file_name = "x-file.txt"
fd = open(file_name) # r is implicit
print("here are the contents of the file:")

# another way is to read line by line, has extra line in between (with "end" there are no lines in the middle)

for line in fd:
    # print(line, end="")
    # print(line.strip())
    print(line.replace("\n", ""))
# 3 methods to do the same thing
fd.close()

#close file and opne it again

fd = open(file_name)
print("here are the three letter words!")
for line in fd:
    words = line.split()
    for word in words:
        if len(word) == 3:
            print(word)
fd.close()

# instead of open and close
# with open(file_name) as fd:
