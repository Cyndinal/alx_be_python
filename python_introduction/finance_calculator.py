monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)
rate = 0.05
Projected_Savings =int(monthly_savings * 12 + monthly_savings * 12 * rate)

"""
contain monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\))

"""

print("Your monthly savings is: $", monthly_savings)
print(f"Projected savings after one year, with interest, is ${Projected_Savings}")