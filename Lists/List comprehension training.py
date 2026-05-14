# numbers = int(input())
#
# my_list = [number * 2 for number in range(numbers)]
#
# print(my_list)

# numbers = int(input())
# my_list = []
#
# for iteration in range(numbers):
#     number = int(input())
#     my_list.append(number ** 2)
# print(my_list)

#
# n = int(input())
# all_numbers = [int(input()) for _ in range(n)]     # първо събираш
# big_numbers = [num for num in all_numbers if num > 50]   # после филтрираш
# print(big_numbers)


# words = ["кола", "мотор", "велосипед", "вагон", "автобус", "влак"]
# my_list = [word.upper() for word in words if len(word) > 5]
# print(my_list)


number = int(input())

numbers = [int(input()) for _ in range(number)]
positive_numbers = [number ** 2 for number in numbers if number >= 0]

print(positive_numbers)



