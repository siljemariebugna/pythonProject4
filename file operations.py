file_name = "x-file.txt"
fd = open(file_name, "a")  # a append w write r read
while True:
    line = input("enter a line (or just press enter to quit): ")
    if line:
        fd.write(line + "\n")
    else:
        break

fd.close()

