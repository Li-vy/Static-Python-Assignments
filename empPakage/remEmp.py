# removes the latest emp

def remEmp():

    fileAppend = open("C:/Users/ADMIN/Desktop/Imp/Study/Internship/Python/Static-Python-Assignments/empPakage/empData.txt","a")
    fileRead = open("C:/Users/ADMIN/Desktop/Imp/Study/Internship/Python/Static-Python-Assignments/empPakage/empData.txt","r")
    data = fileRead.readlines()
    data = data[:-1]
    fileRead.truncate(0)
    fileAppend.writelines(data)

