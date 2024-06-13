import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ----------------------------- SEARCH PASSWORD --------------------------------- #
def find_password():
    web = website.get().title()
    try:
        with open("password_manager.json", 'r') as file:
            # Reading lod data
            json_data = json.load(file)
            details = json_data[web]
    except FileNotFoundError:
        messagebox.showinfo(title="No data", message="No data file found!")
    except KeyError:
        messagebox.showinfo(title="No data", message="No details for the website exists.")
    else:
        messagebox.showinfo(title=web, message=f"Email: {details["email"]} \nPassword: {details["password"]}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letter = [choice(letters) for letter in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    pass_num = [choice(numbers) for number in range(randint(2, 4))]

    password_list = pass_letter + pass_symbols + pass_num
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global data
    web = website.get().title()
    email = email_entry.get()
    passw = password_entry.get()

    new_data = {
        web: {
            "email": email,
            "password": passw,
        }
    }

    if len(web) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=web, message=f'These are the details enetered:'
        #                                                   f' \nEmail: {email} \nPassword: {passw} \n Is it ok to save?')
        # if is_ok:
        try:
            with open("password_manager.json", 'r') as file:
                # Reading load data
                data = json.load(file)
        except FileNotFoundError:
            with open("password_manager.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("password_manager.json", 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_text = Label(text="Website:")
website_text.config(padx=3, pady=3)
website_text.grid(column=0, row=1)
username_text = Label(text="Email/Username:")
username_text.config(padx=3, pady=3)
username_text.grid(column=0, row=2)
pass_text = Label(text="Password:")
pass_text.config(padx=3, pady=3)
pass_text.grid(column=0, row=3)

# Entries
website = Entry(width=35)
website.grid(column=1, row=1, columnspan=2, sticky=EW)
website.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
email_entry.insert(0, "@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=EW)

# Buttons
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3, sticky=EW)
add = Button(text="Add", width=36, command=save)
add.config(padx=3, pady=3)
add.grid(column=1, row=4, columnspan=2, sticky=EW)
search = Button(text="Search", command=find_password)
# search.config(padx=3, pady=3)
search.grid(column=2, row=1, sticky=EW)

window.mainloop()
