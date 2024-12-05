from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import string
from tkinter import messagebox
import json

letter = list(string.ascii_letters)
letter = letter + list(string.punctuation)

def generate_password():
    global letter
    pas = random.sample(letter, 14)
    password = "".join(pas)
    print(password)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)

# def in_pass(new_value):
#     if len(new_value) < 8:





    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()

    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="NAHH BRUH", message="YOU CAN'T LEAVE THE FEILDS EMPTY")
    else:
        try: 
            file = open("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY 29/storage.json","r")

        except FileNotFoundError:
            with open("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY 29/storage.json", "w") as file:
                json.dump(new_data, file, indent=4)
            
        else:   
            data = json.load(file)    #here once the file is opened json.load read the data inside the .json file, it reads the data as dictionary type
            data.update(new_data)     #hence the update method is used to add a new item to the dictionary
            with open("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY 29/storage.json", "w") as file:    
                json.dump(data, file, indent=4)
        finally:
            file.close()
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


def search_password():
    try:
        with open("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY 29/storage.json","r") as file:   # reads the data in the .json file as dictionary type 
            sea_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = "ERROR", message="No file exits")
    else:
        found = False    
        for x,y in sea_data.items():                        
            if x.upper() == web_entry.get().upper():        # checks if the website exits in the database i.e the dictionary from .json file here "sea_data"
                found = True
                message = ""
                for key in y:
                    message = message + f"{key}: {y[key]}\n"  # creating the message with email and password by running through the dictionary
                messagebox.showinfo(title=x, message=message)
        if found==False:
            messagebox.showinfo(title="ERROR", message=f"No details found for {web_entry.get()}")
            
        
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=25,pady=25)
img1 = PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY 29/logo.png")

canvas = Canvas(width=200,height=200)
canvas.create_image(100, 100, image=img1)
canvas.grid(row = 0, column = 1, columnspan=2)

#website label and Entry
website = Label(text="Website")
website.grid(row = 1, column = 0)
web_entry = Entry(width=21) 
web_entry.focus()
web_entry.grid(row = 1, column = 1, columnspan= 1, sticky="W")



#Email/Username using label and entry using Entry
user_name = Label(text="Email/Username")
user_name.grid(row=2, column=0)
user_entry = Entry(width = 35)
user_entry.insert(0, "ramulal@gmail.com")
user_entry.grid(row=2, column=1, columnspan = 2, sticky="W")

#Password label
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
pass_entry = Entry(width=21)
pass_entry.grid(row = 3, column = 1,  sticky="W")

# Add and generate numbers button
add = Button(text="Add",command = add_to_file,width=36)
add.grid(row=4, column=1, columnspan=2)

generate = Button(text="Generate", command=generate_password)
generate.grid(row = 3, column = 2)

#Search Button

search = Button(text="Search",width=17, command=search_password)
search.grid(row=1, column=2)





window.mainloop()