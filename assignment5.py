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
sum = float(0)
for i in range(5):
    n = float(input(f"Enter Number {i+1} : "))
    lst.append(n)
    sum += n 
# sum
print(sum)

# smallest and largest numbers 
