# Take input from the user of 5 numbers and store it in a list.
# Perform below operations:
# 1) Calculate the sum of all the elements in the list
# 2) Find the smallest number
# 3) Find the largest number
# 4) Display list in ascending order
# 5) Display list in descending order
# 6) Convert list into tuple
# 7) Delete the list

lst = list()
for i in range(5):
    lst.append(float(input(f"Enter Number {i+1} : "))) 

# sum

print()
print("Sum of list numbers : ",sum(lst))

# smallest number 

print()
print("Minimum among list numbers : ",min(lst))

# largest number 

print()
print("Maximum among list numbers : ",max(lst))

# ascending order 

print()
lst.sort()
print("List in ascending order : ",lst)

# desending order 

print()
lst.reverse()

# or 

lst.sort(reverse=True)
print("List in desending order : ",lst)

# convert list in tuples 

print()
t = tuple()
t = lst
print("List in Tuple : ",t)

# delete list 

print()
del lst
print("List Deleted")