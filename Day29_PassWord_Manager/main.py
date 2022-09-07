#!/usr/bin/python3
import json
from tkinter import *
# from prettytable import PrettyTable as pt
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def data_saver():
    web_name = website_entry.get()
    user_name = user_entry.get()
    password = password_entry.get()
    new_data = {
        web_name: {
            "email": user_name,
            "password": password
        }
    }
    # table = pt()
    # table.get_string(title="Password Manager")
    # table.field_names = ["Website", "Email-Username", "Password"]
    # table.add_row([web_name, user_name, password])
    if len(web_name) == 0 or len(password) == 0 or len(user_name) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
    else:
        try:
            with open("Data.json", "r") as data_file:
                # Read
                data = json.load(data_file)
        except FileNotFoundError:
            with open('Data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update
            data.update(new_data)

            with open('Data.json', 'w') as data_file:
                # saving
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search Password ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("Data.json") as saved_data:
            json_data = json.load(saved_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        if website in json_data:
            email_add = json_data[website]["email"]
            password = json_data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email:{email_add}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No data found for {website}")
    #     messagebox.showwarning(title=f"{website}", message=f"Email: {user}\n Password: {password}")
    #
    # elif website in saved_data:
    #     messagebox.showwarning(title="Error", message="No data found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
picture = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=picture)
canvas.grid(column=2, row=1)

website_entry = Entry(window, font=("Calibre", 10), width=21)
website_entry.grid(column=1, row=2, columnspan=3)
website_entry.focus()

web_label = Label(text="Website:")
web_label.grid(column=1, row=2, )

user_entry = Entry(window, font=("Calibre", 10), width=35)
user_entry.grid(column=2, row=3, columnspan=3)
user_entry.insert(END, "Tkinter@Python.com")

user_label = Label(text="Email/Username:")
user_label.grid(column=1, row=3)

password_entry = Entry(window, font=("Calibre", 10), width=21)
password_entry.grid(column=1, row=4, columnspan=3)

passwd_label = Label(text="Password:")
passwd_label.grid(column=1, row=4)

add_button = Button(text="Add", bg="#124be6", width=33, command=data_saver)
add_button.grid(column=2, row=5, columnspan=4)

pass_button = Button(text="Generate Password", bg="#124be6", font=("Calibre", 9), command=password_generator)
pass_button.grid(column=3, row=4)

search_button = Button(text="Search", bg="#124be6", font=("Calibre", 9), command=find_password, width=10)
search_button.grid(row=2, column=3)

window.mainloop()
