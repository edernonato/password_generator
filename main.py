from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


def find_password():
    search = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            file = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo("Error", message="File Does Not Exists")
    else:
        if search in file:
            messagebox.showinfo(f"{search}", message=f"Email: {file[search]['email']}"
                                                     f"\nPassword: {file[search]['password']}")
            pyperclip.copy(file[search]['password'])
        else:
            messagebox.showinfo("Error", message=f'No "{search}" password saved.')


def write_to_file(data_new):
    with open("data.json", "w") as data_file:
        json.dump(data_new, data_file, indent=4)


def save_values():
    website = website_entry.get()
    username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Error", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            write_to_file(new_data)

        else:
            data.update(new_data)
            write_to_file(data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# Entries

website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_username_entry = Entry(width=55)
email_username_entry.insert(0, "edernonato47@hotmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(width=47, text="Add", command=save_values)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
