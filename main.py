from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password ="".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def button_clicked():
    user_web = web_entry.get()
    user_email = email_entry.get()
    user_pass = pass_entry.get()
    new_data ={
        user_web: {
            "email": user_email,
            "password": user_pass,
        }
    }

    if len(user_web)==0 or len(user_pass)==0 or len(user_web)==0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            web_entry.delete(0, END)
            email_entry.delete(0 ,END)
            pass_entry.delete(0, END)

def find_password():
    try:
        with open("data.json", "r") as file:
            user_data = web_entry.get()
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")

    else:
        if user_data in data:
            messagebox.showinfo(message=(f"website name: {user_data}\n"
                                         f"password: {data[user_data]['password']}\n"
                                         f"email: {data[user_data]['email']}"))
        else:
            messagebox.showerror(title="Error", message=f"No details for {user_data} exist")



# ---------------------------- UI SETUP ---------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_txt = Label(text="Website:")
web_txt.grid(column=0, row=1)
email_txt = Label(text="Email/Username:")
email_txt.grid(column=0, row=2)
pass_txt = Label(text="Password:")
pass_txt.grid(column=0, row=3)

web_entry = Entry(width=21)
web_entry.grid(column=1, row=1)
web_entry.focus()
search = Button(text="Search", width=10, command=find_password)
search.grid(column=2, row=1)


email_entry = Entry(width=35)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0, "moo@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)
pass_gen = Button(text="Generate Password", width=10, command=generate_password)
pass_gen.grid(column=2, row=3)
add = Button(text="Add", width=33, command=button_clicked)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()
