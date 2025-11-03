monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - total_monthly_expenses
annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

print(f"Projected Savings = {projected_savings}")