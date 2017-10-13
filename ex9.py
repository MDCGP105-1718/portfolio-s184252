starting_salary = float(input("Enter the starting salary: £"))

current_salary = starting_salary
semi_annual_raise = .07
annual_return = .04
house_cost = 1000000
deposit_percentage = .25
down_payment = house_cost * deposit_percentage
num_months = 36
current_savings = 0
num_steps = 0
low = 0
high = 10000

# check to see if it is possible to save value at all to avoid binary search
for month in range(num_months):
    current_savings += current_savings * annual_return / 12
    current_savings += current_salary / 12
    if(month + 1 % 6 == 0):
        current_salary += current_salary * semi_annual_raise

if(current_savings < down_payment - 100):
    print("It is not possible to pay the down payment in three years")
    exit()

if(current_savings >= down_payment - 100 and current_savings <= down_payment + 100):
    print(f"Best savings rate: 100%\ncurrent_savings: {current_savings}")
    print(f"Steps in bisection search: {num_steps}")
    exit()

guess = int((high + low) / 2)
portion_saved = guess / 10000

while(low != guess):
    num_steps += 1
    current_salary = starting_salary
    current_savings = 0

    for month in range(num_months):
        current_savings += current_savings * annual_return / 12
        current_savings += (current_salary / 12) * portion_saved
        if(month + 1 % 6 == 0):
            current_salary += current_salary * semi_annual_raise

    if(current_savings >= down_payment - 100 and current_savings <= down_payment + 100):
        print(f"Best savings rate: {portion_saved * 10}%")
        print(f"Steps in bisection search: {num_steps}")
        exit()

    if(current_savings < down_payment - 100):
        low = guess
    else:
        high = guess

    guess = int((high + low) / 2)
    portion_saved = guess / 10000

# this takes care of a salary so large that the guesses are not accurate
# enough to result in savings +/-£100 of the down payment
print(f"Best savings rate: ~{((guess + .5) / 1000)}%")
print(f"Steps in bisection search: {num_steps}")
exit()