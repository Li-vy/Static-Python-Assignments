# 1) Create 2 classes for single inheritance named respectively A(base class) and B(derived class)

# 2) Create 3 data members in class A: a(private), b(protected) and c(public) initialise their values in 
# a parameterized constructor

# 3) Create a method known as display in both the classes, to display the values of a,b and c

# 4) While accessing the private member an exception should be raised and a personalized message should 
# be displayed and the exception should be handled properly so that the rest of the code can get executed

class A:
    a = None
    _b = None
    __c = None
    def __init__(self,a,b,c):
        self.a = a
        self._b = b
        self.__c = c

    def display(self):
        print("Class A")
        print(f"a : {self.a}, b = {self._b}, c = {self.__c}")
    
class B (A):
    def display(self):
        print("Class B")
        print(f"a = {self.a}, b = {self._b}",end = " ")
        try:
            print(f"c = {self.__c}")
        except Exception:
            print("\nException at line 29 of assignment8.py, \'__c\' cannot be accesed because it is a private variable of class A")
    
b = B("Vishhal","Narkar","CO3")
b.display()

    