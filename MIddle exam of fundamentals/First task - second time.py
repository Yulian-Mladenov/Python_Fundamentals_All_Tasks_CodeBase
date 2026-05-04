days_of_the_vacantion = int(input())
budget = float(input())
number_of_people = int(input())
price_for_fuel_per_km = float(input())
food_cost_per_person_per_day = float(input())
hotel_night_cost_per_day_per_person = float(input())

total_price_food_acomodation = (food_cost_per_person_per_day * number_of_people) + (hotel_night_cost_per_day_per_person * number_of_people)
fuel_costs = price_for_fuel_per_km

if number_of_people > 10:
    total_price_food_acomodation -= total_price_food_acomodation * 0.25

for index in range(days_of_the_vacantion):






