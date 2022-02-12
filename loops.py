# #Loops 

# #While Loops
# favorites = []
# more_items = True 
# while more_items:
#     user_input = input("Enter something you like: ")
#     if user_input == '':
#         more_items = False 
#     else:
#         favorites.append(user_input)

# print("Here are all the things you like!")
# print(favorites)

# #For-each Loops

# #Basic for-each
# def print_nicely_unordered(to_print):
#     for item in to_print:
#         print("* " + (str(item)).capitalize())

# print_nicely_unordered(favorites)

# #For-each -- Using a Counter
# def print_nicely_ordered_counter(to_print):
#     i = 1
#     for item in to_print:
#         print((str(i)) + ". " + (str(item)).capitalize())
#         i = i + 1

# print_nicely_ordered_counter(favorites)

# #For-each -- Using Range
# def print_nicely_ordered_range(to_print):
#     for i in range(len(to_print)):
#         print(str(i + 1) + ". " + str((to_print[i]).capitalize()))

# print_nicely_ordered_range(favorites)

# #For-each -- Using Enumerate
# def print_nicely_ordered_enumerate(to_print):
#     for index, value in enumerate(to_print, 1):
#         print(str(index) + ".", (str(value)).capitalize())

# print_nicely_ordered_enumerate(favorites)

# #Nesting - a loop inside a loop
# for i in range(1,11):
#     factors = []
#     for j in range(1, i + 1):
#         if i % j == 0:
#             factors.append(j)
#     print("The factors of " + str(i) + " are: " + str(factors))

# #Infinite while loops 
# def add(num1, num2):
#     sum = int(num1) + int(num2)
#     print(sum)

# while True:
#     add(input("Number 1: "), input("Number 2: "))

# # Write a script that displays a multiplication table from 1 * 1 to 10 * 10. Here is what the top-left corner should look like:
# # 1 2 3 4
# # 2 4 6 8
# # 3 6 9 12
# # 4 8 12 16

# for x in range(1,11):
#     nums = []
#     for y in range(1,11):
#         sum = x * y
#         nums.append(sum)
#     print(*nums)

#Use enumerate and the % operator to print every third word in this list:
#['alpha','beta','gamma','delta','epsilon','zeta','eta']

letters = ['alpha','beta','gamma','delta','epsilon','zeta','eta']

for index, letter in list(enumerate(letters)):
    if (index + 1) % 3 == 0:
        print(letter)