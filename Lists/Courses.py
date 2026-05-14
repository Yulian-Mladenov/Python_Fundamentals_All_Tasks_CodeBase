# first approach
# list_with_courses_names = []
#
# for iteration in range(number_of_the_courses):
#     name_of_the_course = input()
#     list_with_courses_names.append(name_of_the_course)
#
# print(list_with_courses_names)

# second approach
# number = int(input())
#
# courses = []
#
# for _ in range(number):
#     courses.append(input())
#
# print(courses)

# third approach with comprehension
n = int(input())

my_list = [int(input()) for _ in range(n)]

print(my_list)
