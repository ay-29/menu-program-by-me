from tkinter import *
import subprocess

root = Tk()

root.title("Welcome to GUI program")
root.configure(bg="black")

L1 = Label(root, text="MENU PROGRAM", font="Arial 16 bold", bg="red", fg="black")
L1.pack(side=TOP, fill=X, pady=20)


def fun1():
    subprocess.run(["libreoffice", "--writer"])


def fun2():
    subprocess.run(["gnome-terminal", "--", "bluetooth-sendto"])


def fun3():
    subprocess.run(["google-chrome", "gmail.com"])


def fun4():
    subprocess.run(["onboard"])


def fun5():
    subprocess.run(["gnome-control-center", "sound"])


def fun6():
    subprocess.run(["google-chrome", "googledrive.com"])


def fun7():
    subprocess.run(["gnome-terminal", "--", "cheese"])


def fun8():
    subprocess.run(["nautilus", "/"])


def fun9():
    subprocess.run(["gnome-control-center", "user-accounts"])


def fun10():
    subprocess.run(["gnome-terminal", "--", "gnome-volume-control"])


def fun11():
    root.destroy()


b1 = Button(root, text="Screen Keyboard", relief=RAISED, font="Arial 16 bold", pady=3, padx=17, command=fun4)
b1.pack(pady=4)

b2 = Button(root, text="Bluetooth Transfer", relief=RAISED, padx=12, font="Arial 16 bold", command=fun2)
b2.pack(pady=3)
b3 = Button(root, text="Gmail", relief=RAISED, padx=75, font="Arial 16 bold", command=fun3)
b3.pack(pady=4)
b4 = Button(root, text="System Properties", relief=RAISED, padx=13, font="Arial 16 bold", command=fun5)
b4.pack(pady=4)
b5 = Button(root, text="LibreOffice", relief=RAISED, padx=62, font="Arial 16 bold", command=fun1)
b5.pack(pady=4)
b6 = Button(root, text="Google Drive", relief=RAISED, padx=42, font="Arial 16 bold", command=fun6)
b6.pack(pady=4)
b7 = Button(root, text="Click for Picture", relief=RAISED, padx=27, font="Arial 16 bold", command=fun7)
b7.pack(pady=4)
b8 = Button(root, text="C Drive", relief=RAISED, padx=68, font="Arial 16 bold", command=fun8)
b8.pack(pady=4)
b9 = Button(root, text="User Account Access", relief=RAISED, font="Arial 16 bold", command=fun9)
b9.pack(pady=4)
b10 = Button(root, text="Audio Properties", relief=RAISED, padx=22, font="Arial 16 bold", command=fun10)
b10.pack(pady=4)

b11 = Button(root, text="Exit", relief=SUNKEN, font="Arial 16 bold", command=fun11)
b11.pack(pady=40)

root.mainloop()
