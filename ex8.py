annual_salary = float(input("Enter your annual salary: "))
semi_annual_raise = float(input("Enter your semi-annual raise percentage, as a decimal: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_deposit = total_cost * .2
current_savings = 0
annual_return = .04
num_months = 0

while(current_savings < portion_deposit):
    current_savings += current_savings * annual_return / 12
    current_savings += (annual_salary / 12) * portion_saved
    num_months += 1
    if(num_months % 6 == 0):
        annual_salary += annual_salary * semi_annual_raise

print(f"Number of months: {num_months}")