from tkinter import *
import smtplib

# Window setup

window = Tk()
window.geometry("420x210")
window.title("Email Spammer")
window.resizable(width=False, height=False)
window.config(background="Black")
server = smtplib.SMTP_SSL("Smtp.gmail.com", 465)
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)


# functions

def spam():
    while True:
        email = entry.get()
        server.login("robertjonathan0033", "JoeRogan1")
        server.sendmail("robertjonathon0033", email, "You are being spammed")


# Button, entry, label

label = Label(window, text="Warning you are about to spam this persons email!\n"
                           "If the window is not responding that means its working.",
              font=("Ariel", 12, "bold"),
              fg="Green",
              bg="Black")
label.pack()

entry = Entry(window, font=("Ariel", 20))

entry.place(x=40, y=100)

button = Button(window,
                text="Enter",
                fg="white",
                bg="Black",
                activeforeground="white",
                activebackground="black",
                command=spam,
                padx=9,
                pady=6.5)
button.place(x=360, y=100)

window.mainloop()
