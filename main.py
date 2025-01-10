from textwrap import indent
from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice,randint,shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    password_char = [choice(letters) for char in range(randint(2, 4))]
    password_sym = [choice(symbols) for sym in range(randint(2, 4))]
    password_num = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_char + password_sym + password_num

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0,f"{password}")
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = site_entry.get()
    mail = mail_entry.get()
    passw = pass_entry.get()
    new_data = {
                   site:
                   {
                    "email": mail,
                    "password": passw,
                     }
                }
    if len(site) == 0 or len(passw) == 0:
        messagebox.showinfo(title="No entry",message="Do not leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
        finally:
            site_entry.delete(0, "end")
            pass_entry.delete(0, "end")

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = site_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data Found")
    else:
        if website in data:
            password = data[website]["password"]
            messagebox.showinfo(title="Details", message=f"Website: {website}\n"
                                                         f"Password: {password}")
        else:
            messagebox.showinfo(message="No details for website exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")
canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)
#Labels
website = Label(text="Website:",fg="black",bg="white")
website.grid(column=0,row=1)
email = Label(text="Email/Username:",fg="black",bg="white")
email.grid(column=0,row=2)
password = Label(text="Password:",fg="black",bg="white")
password.grid(column=0,row=3)
#Buttons
generate = Button(text="Generate Password",highlightbackground="white",command=generate_password)
generate.grid(column=2,row=3)
add_button= Button(text="Add",highlightbackground="white",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)
search_but = Button(text="Search",highlightbackground="white",command=find_password)
search_but.grid(column=2,row=1,columnspan=2)
#Entries
site_entry = Entry(width=35,fg="black",bg="white",highlightthickness=0,insertbackground="black")
site_entry.grid(column=1,row=1)
site_entry.focus()
mail_entry = Entry(width=35,fg="black",bg="white",highlightthickness=0,insertbackground="black")
mail_entry.grid(column=1,row=2,columnspan=1)
mail_entry.insert(0,"aasonibare@gmail.com")
pass_entry = Entry(width=35,fg="black", bg="white", highlightthickness=0,insertbackground="black")
pass_entry.grid(column=1, row=3)



window.mainloop()