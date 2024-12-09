income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = income - monthly_expenses
rate = 0.05
Projected_Savings =int(monthly_savings * 12 + monthly_savings * 12 * rate)

print("Your monthly savings is: $", monthly_savings)
print(f"Projected savings after one year, with interest, is ${Projected_Savings}")