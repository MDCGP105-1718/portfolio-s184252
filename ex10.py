def fizzBuzz(low, high):
    """
    Prints to the screen the results of
    FizzBuzz:
    if a number is divisible by 3, prints "Fizz"
    if a number is divisible by 5, prints "Buzz"
    if a number is divisible by 15, prints "FizzBuzz"
    otherwise, prints the number
    """
    for n in range(low, high + 1):
        if(n % 15 == 0):
            print("FizzBuzz")
        elif(n % 5 == 0):
            print("Buzz")
        elif(n % 3 == 0):
            print("Fizz")
        else:
            print(n)

fizzBuzz(int(input("Enter low number: ")), int(input("Enter high number: ")))
