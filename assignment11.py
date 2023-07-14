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

questionLabel = Label(master = root, text= "Where did you see this AD ?", font=("Poppins bold",15))
questionLabel.grid()
userChoice = StringVar(root)
userChoice.set("Select an Option")
checkBox = OptionMenu(root,userChoice,"Youtube Ads", "Instagram Ads")
checkBox.grid()
submitButton = Button(root,text = "Submit").grid()


root.mainloop()
# # Function to open the FAQ page based on the selected option
# def open_faq_page():
#     selected_option = option.get()
    
#     if selected_option == "Instagram Ads":
#         webbrowser.open("https://www.example.com/faq/instagram")
#     elif selected_option == "YouTube Ads":
#         webbrowser.open("https://www.example.com/faq/youtube")
#     # Add more options and corresponding FAQ page URLs as needed

# # Create the main window
# window = tk.Tk()
# window.title("Course Enquiry Form")

# # Create a label and entry field for the user's name
# name_label = tk.Label(window, text="Name:")
# name_label.pack()
# name_entry = tk.Entry(window)
# name_entry.pack()

# # Create a label and option menu for where the user came to know about the course
# option_label = tk.Label(window, text="Where did you hear about the course?")
# option_label.pack()
# option = tk.StringVar()
# option_menu = tk.OptionMenu(window, option, "Instagram Ads", "YouTube Ads")
# option_menu.pack()

# # Create a submit button to navigate to the FAQ page
# submit_button = tk.Button(window, text="Submit", command=open_faq_page)
# submit_button.pack()

# # Start the GUI main loop
# window.mainloop()
