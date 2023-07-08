print("Menu driven program Calculator")

class Calculator:
    def calculate():
        n1=1
        lst = list(range(1,5))
        while n1 == 1:

            print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n")
            num=int(input("Enter your choice: "))

            if num in lst:
                x=float(input("Enter first value :"))
                y=float(input("Enter second value :"))
            
                if num == 1:
                    print("Addition is : ",(x+y))
            
                elif num==2:
                    print("Subtraction is : ",(x-y))
            
                elif num==3 :
                    print("Multiplication is : ",(x*y))
            
                elif num==4:
                    print("Division is : ",(x/y))
            else:
                print("Wrong choice")
            
            n=input("If you want to continue press 1 \notherwise press any key \n")
            if n!="1":
                exit()
            n1=int(n)
            
    
c=Calculator
c.calculate()


# Take 3 inputs and show the user the smallest and largest among those useing nested if 

print("\n\nCode to Take 3 inputs and show the user the smallest and largest among those useing nested if ")
x = float(input("Enter first value :"))
y = float(input("Enter second value :"))
z = float(input("Enter third value :"))

def compareEquals(a,b,c):
        if (a == b):
            print(c," is the largest number. \nOther two numbers are same.")

def compare(a,b,c):
    if (a > c):
          print(a," is the largest number.")
          if (b > c):
            print(c," is the smallest number.")
          else :
            print(b," is the smallest number.")
    else :
        print(c," is the largest number.")
        print(b, "is the smallest number.")

if (x == y == z):
    print("All numbers are same.")
elif (x == y or y == z or x == z):
    compareEquals(x,y,z)
    compareEquals(y,z,x)
    compareEquals(x,z,y)
elif (x > y):
     compare(x,y,z)
elif (y > z):
    compare(y,x,z)
elif (z > x):
    compare(z,x,y)
elif (z > y):
    compare(z,y,x)