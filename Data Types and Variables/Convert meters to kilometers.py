# this code is giving 100 from 100 points in Judge:
# distance_in_meters = int(input())
#
# meters_converted_in_kilometers = distance_in_meters / 1000
#
# print(f'{meters_converted_in_kilometers:.2f}')



# this code is modified by me:
distance_in_meters = int(input('Please write the distance in meters: '))

KILOMETERS_CONSTANT_VALUE_FOR_DIVIDING = 1000
meters_converted_in_kilometers = distance_in_meters / KILOMETERS_CONSTANT_VALUE_FOR_DIVIDING

print(f'Here are your meters converted in kilometers: {meters_converted_in_kilometers:.2f}')