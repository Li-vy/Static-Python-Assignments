def addEmp():

    fileAppend = open("C:/Users/ADMIN/Desktop/Imp/Study/Internship/Python/Static-Python-Assignments/empPakage/empData.txt","a")
    fileRead = open("C:/Users/ADMIN/Desktop/Imp/Study/Internship/Python/Static-Python-Assignments/empPakage/empData.txt","r")
    print("Previous Data : ")
    for i in fileRead.readlines():
        print(i)
    print()
    print("Enter the details of the Employee : ")
    id = int(input("Enter Id : "))
    name = str(input("Enter Name : "))
    salary = int(input("Enter Salary : "))
    designation = str(input("Enter Designation : "))
    fileAppend.write(f"\nid: {id} -> name: {name} -> salary: {salary} -> designation: {designation}")
