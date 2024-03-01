text = "abcdefghilmn"
for letter in text:
    print(letter)

i = len(text) -1
while i >= 0:
    print(text[i], end="")
    i -= 1


print()
i = 0
while i < len(text):
    print(text[len(text)-i-1], end="")
    i += 1


string = "mammamia"
string[1]
string[1] = "b"


