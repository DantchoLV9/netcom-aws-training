import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


# Pseudo code

# 1. Generate a random number between 1 and 10 and store it as "number"
# 2. Ask user to guess a number between 1 and 10 and store it as "guess"
# 3. If "guess" is equal to "number" then tell the user they won, and exit the program
# 4. If "guess" is not equal to "number" then tell thhe user to try again, and jump back to step 2