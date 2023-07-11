# 1)Create a function named ds with parameters roll_no and name.
# 2)Add those parameters in the following data structures:
# list, tuple, sets and dictionaries
# 3) After adding values
# change the values during runtime
# 4)Delete these data structures

def ds(name, roll_no):
    
    # Assigning the initial values 

    lst = [name,roll_no]
    tup = (name,roll_no)
    sets = {name,roll_no}
    dic = {
        "Name":name,
        "Roll_no":roll_no
        }
    
    # Printing the initial values 
    
    print(lst)
    print(tup)
    print(sets)
    print(dic)
    
    # Taking input for new values 
    
    newName = str(input("Enter Name : "))
    newRoll_no = int(input("Enter Roll number : "))
    
    # Re-assigning the data structres with new values 
    
    lst[0] = newName
    lst[1] = newRoll_no
    tup = tuple(lst)
    set.update(set(lst))
    dic["Name"] = newName
    dic["Roll_no"] = newRoll_no
    
    # displaying the updated data structures 
    
    print("Updated data structures : ")
    print(lst)
    print(tup)
    print(sets)
    print(dic)
    
    # Deleting data structures
    
    print("Deleting the data structures...")
    del lst,tup,sets,dic
    print("Data Structures deleted.")
    print("Bye")

# Function call 

ds("Vishhal",115)