class Calculator:
    def calculate():
        n1=1
        lst = list(range(1,5))
        while n1 == 1:

            print("\n This is menu driven program")
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

