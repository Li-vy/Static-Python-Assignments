import addEmp as a
import remEmp as r
import searchEmp as s
import showEmp as sh
import os

def empMain():
    
    condition = True
    while condition:
        print("Press 1 to Add Employees")
        print("Press 2 to Remove Employees")
        print("Press 3 to Search Employees")
        print("Press 4 to Show Employees")
        print("Press 5 to Exit")
        print()
        try:
            userChoice = int(input("Enter your choice : "))
            if userChoice == 1:
                os.system('cls')
                a.addEmp()
                print() 
            elif userChoice == 2:
                os.system('cls')
                r.remEmp()
                print()
            elif userChoice == 3:
                os.system('cls')
                s.searchEmp()
                print()
            elif userChoice == 4:
                os.system('cls')
                sh.showEmp()
                print()
            elif userChoice == 5:
                condition = False
            else:
                os.system('cls')
                print("Please Enter number between 1 to 5")
        except Exception:
            os.system('cls')
            print("Please Enter an integer")
            print()

