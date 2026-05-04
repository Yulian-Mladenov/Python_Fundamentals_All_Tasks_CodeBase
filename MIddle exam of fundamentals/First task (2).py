days = int(input())
budget = float(input())
people = int(input())
fuel_price_per_km = float(input())
food_per_person_per_day = float(input())
hotel_price_per_person_per_night = float(input())

total_food_expenses = days * people * food_per_person_per_day
total_accommodation_expenses = days * people * hotel_price_per_person_per_night

if people > 10:
    total_accommodation_expenses *= 0.75


current_expenses = total_food_expenses + total_accommodation_expenses

for day in range(1, days + 1):
    distance = float(input())
    daily_fuel_cost = distance * fuel_price_per_km
    current_expenses += daily_fuel_cost

    if day % 3 == 0 or day % 5 == 0:
        current_expenses += 0.4 * current_expenses

    if day % 7 == 0:
        current_expenses -= current_expenses / people

    if current_expenses > budget:
        money_needed = current_expenses - budget
        print(f"Not enough money to continue the trip. You need {money_needed:.2f}$ more.")
        break
else:
    money_left = budget - current_expenses
    print(f"You have reached the destination. You have {money_left:.2f}$ budget left.")


