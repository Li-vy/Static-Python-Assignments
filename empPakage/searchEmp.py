def searchEmp():
    id = int(input("Enter the id of the employee : "))
    fileRead = open("C:/Users/ADMIN/Desktop/Imp/Study/Internship/Python/Static-Python-Assignments/empPakage/empData.txt","r")
    print(fileRead.readlines()[id])
    
