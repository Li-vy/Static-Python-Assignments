# 1) Implement the tkinter and webbrowser module

# 2) create a gui for taking input from the user and create a button to navigate to a browser site.

# 3) Also display the user entered text in the command prompt with message of navigating to "..." whichever site you chooses

# Note:
# [you cannot use Google search]

# you can use YouTube, etc.

# import tkinter as tk
from tkinter import *
from webbrowser import *

# root = tk.Tk()
root = Tk()
root.title("Navigate To Youtube")
# e = tk.Entry(root,font=("Times New Roman",25))
e = Entry(root,font=("Times New Roman",25))
e.grid()
def navi():
    print(f"Navigating to = {e.get()} on Youtube")
    query = "https://www.youtube.com/results?search_query="+e.get()
    open(query)
# b = tk.Button(root,text = "Search",
b = Button(root,text = "Search",
           font = ("Times New Roman",25),
           command = navi
        )
b.grid()    

root.mainloop()