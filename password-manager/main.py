import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
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

    password_result = "".join(password_list)
    password_entry.insert(0, password_result)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_data = website_entry.get()
    em_data = email_entry.get()
    pass_data = password_entry.get()
    new_data = {
        web_data: {
            "email": em_data,
            "password": pass_data,
        }
    }
    messagebox.askokcancel(title="QA", message=f"These are details entered\n Website: {web_data}\n Email/Username: {em_data}\n Password: {pass_data}")
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- SEARCH BUTTON ------------------------------------ #

def search():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"{website} doesn't exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"{website} doesn't exist")


#----------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=logo_img)
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "artyom.aghekyan2006@gameil.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search)
search_button.config(width=14)
search_button.grid(row=1, column=2)
window.mainloop()
