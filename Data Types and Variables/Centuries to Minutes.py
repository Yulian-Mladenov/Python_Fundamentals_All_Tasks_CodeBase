# reading input data - initial of the program:
centuries_in_number = int(input())

# variables used for calculations:
one_century_in_years = 100
one_year_in_days = 365.2422
one_day_in_hours = 24
one_hour_in_minutes = 60

# calculations:
years = centuries_in_number * one_century_in_years
days = int(years * one_year_in_days) # here the days (like data) is parsed to integer type,to avoid float number in  the next code lines.
hours = days * one_day_in_hours
minutes = hours * one_hour_in_minutes

# printing the result:
print(f'{centuries_in_number} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
















