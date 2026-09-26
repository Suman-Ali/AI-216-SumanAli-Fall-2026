# Input: food, transport, other expenses and daily budget
# Processing: calculate total and remaining budget, compare with budget
# Output: total expense, remaining budget, and status

food_expense = 450
transport_expense = 200
other_expense = 150
daily_budget = 1000

total_expense = food_expense + transport_expense + other_expense
remaining_budget = daily_budget - total_expense

print(f"Total expense: {total_expense}")
print(f"Remaining budget: {remaining_budget}")

if total_expense < daily_budget:
    print("Status: Within budget")
elif total_expense == daily_budget:
    print("Status: Exactly at budget")
else:
    print("Status: Over budget")