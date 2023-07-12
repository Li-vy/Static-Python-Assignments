# 1) Create a function with a default parameter "file" storing the file path

def fileHandle(file):
    
# 2) Open the "file" in append mode

    f = open(file,"a")

# 3) Use writelines() method to add your roll number, name, and class

    f.writelines("Roll number - 115, Name - Vishhal, Class - CO3")

# 4) Use readines() method to print your data in the prompt
    f.close()
    f = open(file,"r")
    print(f.readlines())

fileHandle("assignment7.txt")