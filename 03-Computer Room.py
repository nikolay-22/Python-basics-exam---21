month = input()
hours = int(input())
people = int(input())
time = input()

if month == "march" or month == "april" or month == "may":
    if time == "day":
        price_hour = 10.50
    elif time == "night":
        price_hour = 8.40
elif month == "june" or month == "july" or month == "august":
    if time == "day":
        price_hour = 12.60
    elif time == "night":
        price_hour = 10.20

if people >= 4:
    price_hour *= 0.90
if hours >= 5:
    price_hour *= 0.50

total_cost = price_hour * hours * people

print(f"Price per person for one hour: {price_hour:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")
