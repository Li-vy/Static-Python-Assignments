# n1 = float(input("Enter number 1 : "))
# n2 = float(input("Enter number 2 : "))
# n3 = float(input("Enter number 3 : "))
# nums = [None] * 3
sum = 0;
for i in range(3):
    # nums[i] = float(input("Enter number {i} : "))
    # nums.append(float(input("Enter number {i} : ")))
    # print(i)
    sum = sum + float(input("Enter number "+ str(i+1) +" : "))
    print()

# print("The average of n1,n2 and n3 is "+str((n1+n2+n3)/3))  
# print("The average of n1,n2 and n3 is "+str(sum/len(nums)))
print("The average of n1,n2 and n3 is ", str(sum/3))