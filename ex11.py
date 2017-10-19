from random import randint

def numberGuess():
    number = randint(0, 1000)
    guess = int(input("Guess the number! 0 to 1000: "))

    while(guess != number):
        if(guess < number):
            print("Too low! The number is higher")
            guess = int(input("Guess the number! 0 to 1000: "))
        elif(guess > number):
            print("Too high! The number is lower")
            guess = int(input("Guess the number! 0 to 1000: "))

    print(f"Correct! The number is {number}")


numberGuess()
