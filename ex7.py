annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_deposit = total_cost * .2
current_savings = 0
annual_return = .04
monthly_salary_saved = (annual_salary / 12) * portion_saved

num_months = 0

while(current_savings < portion_deposit):
    current_savings += current_savings * annual_return / 12
    current_savings += monthly_salary_saved
    num_months += 1

print(f"Number of months: {num_months}")