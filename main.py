import pyperclip
import random
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    n_letters = random.randint(8,10)
    n_numbers = random.randint(2,4)
    n_symbols = random.randint(2,4)

    password = []

    for char in range(n_letters):
        password.append(random.choice(letters))
    for num in range(n_numbers):
        password.append(random.choice(numbers))
    for sym in range(n_symbols):
        password.append(random.choice(symbols))

    random.shuffle(password)
    passwrd = "".join(password)
    if password_input.get() != "":
        password_input.delete(0, END)
        generate_pass()
    else:
        password_input.insert(0, passwrd)
        pyperclip.copy(passwrd)



# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill every field")
    else:
        confirm = messagebox.askyesno(title="Save Passowrd", message=f"These are the details entered\n"
                                                           f"Website : {website}\n"
                                                           f"Email/Username : {email}\n"
                                                           f"Password : {password}")
        if confirm:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("SMK Pass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

#Lables
website_label = Label(text="Website")
website_label.grid(column=0, row=1, sticky=W)

email_label = Label(text="Email / Username")
email_label.grid(column=0, row=2, sticky=W)

password_label = Label(text="Password")
password_label.grid(column=0, row=3, sticky=W)

#Entries
website_input = Entry(width=42)
website_input.grid(column=1, row=1, columnspan=2, sticky=E)

email_input = Entry(width=42)
email_input.grid(column=1, row=2, columnspan=2, sticky=E)
email_input.insert(0, "sourabmkalliyanofficial@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Buttons
generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_pass)
generate_button.grid(column=2, row=3)

add_button = Button(width=39, text="Add Password", command=save)
add_button.grid(column=1, row=4, columnspan=2,sticky=E)

window.mainloop()
