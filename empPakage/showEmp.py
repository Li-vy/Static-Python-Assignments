def showEmp():
    fileRead = open("C:/Users/ADMIN/Desktop/Imp/Study/Internship/Python/Static-Python-Assignments/empPakage/empData.txt","r")
    for i in fileRead.readlines():
        print(i)
    print()
