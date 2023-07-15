# Create a gui based form to take input from the user and then navigate to the particular site from 
# where the user came to know about the content

# for example:
# create a form where the user is enquiring about the respective course
# and in the form there is an option for asking where the user came to know about it, for eg: instagram ads 
# or YouTube ads

# and then when clicking the submit button
# take the user to the faq page of that site

from tkinter import *
from webbrowser import *

root = Tk(className= " Ads Survey")

root.geometry("450x270")
Label(root).pack()
nameLabel = Label(root, text="Name:").pack()
userName = Entry(root).pack()
contactLabel = Label(root, text="Contact:").pack()
userContact = Entry(root).pack()
Label(root).pack()
questionLabel = Label(master = root, text= "Where did you see this AD ?", font=("Poppins medium",15)).pack()
userChoice = StringVar(root)
userChoice.set("Select an Option")
checkBox = OptionMenu(root, userChoice, "Youtube Ads", "Instagram Ads").pack()
Label(root).pack()
def submitOnClick():
    if userChoice.get() == "Instagram Ads":
        open("https://help.instagram.com/537518769659039discord.com/hc/en-us/sections/200613688-FAQ")
    elif userChoice.get() == "Youtube Ads":
        open("https://www.youtube.com/intl/en-GB/ads/")
    root.destroy()
submitButton = Button(root,text = "Submit",command = submitOnClick).pack()
Label(root).pack()

root.mainloop()
