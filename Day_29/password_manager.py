from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ----------------------------- SEARCH DATA --------------------------------- #
def search():
    website = website_input.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website].get("email")
            password = data[website].get("password")
            messagebox.showinfo(title=f"{website}", message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"You have not saved passwords from the {website}."
                                                       f"\nFill out the form and click the add button.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_data_to_json(new_data):
    with open("data.json", mode="w") as data_file:
        json.dump(new_data, data_file, indent=4)


def save():
    website = website_input.get().title()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
                                                              f" \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                write_data_to_json(new_data)
            else:
                data.update(new_data)

                write_data_to_json(data)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=33)
website_input.grid(column=1, row=1)
website_input.focus()
username_input = Entry(width=51)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(END, "murat@gmail.com")
password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# Button
add_button = Button(text="Add", width=44, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)
generate_password_button = Button(text="Generate Password", width=14, highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3)
search_button = Button(text="Search", width=14, highlightthickness=0, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
