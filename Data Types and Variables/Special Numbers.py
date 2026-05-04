# ▪ Write a program that reads an integer n. For all numbers in the
# range 1…n print the number and if it is special or not (True / False)
# ▪ A number is special when the sum of its digits is 5, 7, or 11

# number = int(input())

# digits_sum_1 = 5
# digits_sum_2 = 7
# digits_sum_3 = 11
#
# sum = 0
#
# for index in range(1, number + 1):
#     if index > 9:

number = int(input())

for index in range(1, number + 1):
    sum_of_digits = 0
    digits = index

    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)

    if (sum_of_digits == 5) or (sum_of_digits == 11) or (sum_of_digits == 7):
        print(f'{index} -> True')
    else:
        print(f'{index} -> False')



