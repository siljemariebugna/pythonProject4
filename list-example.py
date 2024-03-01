import random
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.extend(["elderberry", "fig", "grape"])
fruits += ["honeydew", "kiwi", "lemon"]

print(fruits)
random_fruit = random.choice(fruits)

while True:
    fruit = random.choice(fruits)
    like = input(f"Do you like the {fruit}? (yes/no) ")
    if like.lower() == "yes":
        new_fruit = input(f"name of another fruit to add: ")
        fruits.append(new_fruit)
    elif like.lower() == "no":
        print(f"removing {fruit} from the list")
        fruits.remove(fruit)
    elif like.lower() == "stop":
        break

with open("fruits.txt", "w") as fd:
    for fruit in fruits:
        fd.write(fruit + "\n")
