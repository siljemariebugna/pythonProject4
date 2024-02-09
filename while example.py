import random
lives = 3
while lives > 0:
    print("You have", lives, "lives left.")
    # roll the dice
    dice = random.randint(1,6)
    print("You rolled a", dice)
    #check if u win
    if dice == 6:
        print("\n\nYOU WIN!\n\n")
        break
    else:
        lives -= 1
else:
    print("\n\nyou lose my friend\n\n")

print("thank you for playing. Ciao.")

