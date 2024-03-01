text = "abcdefghilmnop"
print(dir(text))
help(text.isupper())
print(text.isupper())
print("ABC".isupper()) # is text upper case?
print(text.upper())   # convert text to upper case
print(text.upper().isupper()) # is the text all upper case

new_text = text.upper()
print(text, new_text)

print("banananananana".count("n"))  # counting substrings
print("banananananana".index("b")) # where is a certain letter
print("banananananana".replace("ana", "XYXYXX")) #replace smt with smt

sentence = "Hello kind-sir; how many! I be of service today?"

print(sentence.replace(",", "").replace(";", "").replace("!", "").replace("-", "").replace("?", ""))
punctuation = ".,;!?"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)

print("this is a sentence i want the words".split(" "))
text = "Bob goes to school. Bob likes to play tennis. I a friends with Bob. Such a nice guy Bob"

i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1


