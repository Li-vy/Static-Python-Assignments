import os
os.system('cls')
class Opreations:
    string = str()
    def __init__(self, string):
        condition = True
        while(condition):
            self.string = string
            if len(self.string.split()) != 1:
                try:
                    raise Words
                except Words as w:
                    print(w.args[0])
                finally:
                    if int(input("Press 1 to continue or press any other key to exit\n")) == 1:
                        os.system('cls')
                        Opreations(input("Enter a String : "))
                    else:
                        condition = False
            else:
                print("Number of letter in the String are : ",self.countLetters())
                print("String in uppercase : ",self.upperString())
                print("String in lowercase : ",self.lowerString())
                print("Reverse String : ",self.reverseString())
                print("String to ASCII : ",self.stringAscii())
                print("String to char array : ",self.stringToCharArray())
                condition = False
    
    def countLetters(self):
        return len(self.string)
    
    def reverseString(self):
        return self.string[::-1]
    
    def upperString(self):
        return self.string.upper()

    def lowerString(self):
        return self.string.lower()
    
    def stringAscii(self):
        return [ord(c) for c in self.string]
    
    def stringToCharArray(self):
        return [*self.string]
    
class Words(Exception):
    def __init__(self):
        super().__init__("Please enter one word no more no less.") 