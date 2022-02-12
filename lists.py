#Create list 
my_list = ["A","B","C","D"]
print(my_list)

#Append new item 
my_list.append("E")
print(my_list)

#Find length of a list
print("length =", len(my_list))

#Find values of items by their position in the list (their "index"). The list index starts at 0 (first item = position 0)
print("first item = ", my_list[0])
print("last item = ", my_list[len(my_list) - 1])

#Search a list - 2 ways 
#1. in = Whether an item is in a list or not
print("A" in my_list) #returns True or False

#2. index() = Where an item is in a list
print(my_list.index("C"))

#User input testing
favfood = []

while len(favfood) <= 2:
    userfav = input("What is one of your favorite foods?")
    favfood.append(userfav)
    print(favfood)

srch = (input("Enter a food to see if it's one of your favorites: ")) in favfood
if srch == True:
    print("That's one of your favorite foods!")
else:
    print("That's not one of your favorite foods.")

#Finding the middle of a list
list1 = ['A','B','C','D','E','F','G','H','I', 'J']
length = len(list1)
half = length//2
print(half)
print(list1[half])