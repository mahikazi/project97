import random
x = random.randint(1, 9)
guess = int(input("Enter a number from 1 to 9: "))
while x != "guess":
    print
    if guess < x:
        print("The guess is low.")
        guess = int(input("Enter a number from 1 to 9: "))
    elif guess > x:
        print("The guess is high.")
        guess = int(input("Enter a number from 1 to 9: "))
    else:
        print("You guessed the number!")
        break

