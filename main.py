# 1. import the random module to help us generate random numbers
import random

# 2. use the randint() to get a random number. It however would take two values which would represent the range of numbers. randrange() equally does same thing.
num = random.randint(1, 14)

# 3. welcome our user, ask for their name and capitalize the first letter incase they forget
username = input("Welcome to the Number Guessing Game, Tell us your name: ")
username = username.capitalize()
print(username, "I'm thinking of a number between 1 and 14 can you guess. Your have 3 trys")

# 4. initialize the number of guess user can make
guessessTaken = 0
while True:
    try:
        while guessessTaken <= 2:
            guess = int(input("Take a guess: "))
            guessessTaken += 1
            if guess > num:
                print("Your guess is high")
            if guess < num:
                print("Your guess is low")
            if guess == num:
                break
        if guess == num:
            guessessTaken = str(guessessTaken)
            print(
                f"Great job {username} You guessed my number after {guessessTaken} guesses")
        if guess != num:
            num = str(num)
            print(f"Nope, The number was {num}")
    except (ValueError):
        print("It has to be a whole number")
    else:
        break
