# number = int(input())
# print("even" if number % 2 == 0 else "odd")

# my_list =[]
# numbers = [3, -7, 0, 5, -1, 8]
# for number in numbers:
#     if number >= 0:
#         my_list.append = []
#     else:
#         my_list.append = []

numbers = [3, -7, 0, 5, -1, 8]
my_list = ['+' if number >= 0 else '-' for number in numbers]
print(my_list)

