from tkinter import *
from tkinter import messagebox

root = Tk()
#Creates login window and sets specifications
class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("512x512")
        self.bg = PhotoImage(file="school-icons-clipart.png")
        self.label1 = Label(self.master, image=self.bg)
        self.label1.place(x=0, y=0)
        self.username = StringVar()
        self.password = StringVar()
        self.setup_login()
#Setups up bows for user inputs
    def setup_login(self):
        Label(self.master, text="Username:").grid(row=0, column=0)
        Label(self.master, text="Password:").grid(row=1, column=0)
        Entry(self.master, textvariable=self.username).grid(row=0, column=1)
        Entry(self.master, textvariable=self.password, show="*").grid(row=1, column=1)
        Button(self.master, text="Login", command=self.login).grid(row=2, column=1)
#sets password and username
    def login(self):
        if self.username.get() == "admin" and self.password.get() == "password1":
            self.master.destroy()
            GradesWindow()
        else:
            messagebox.showerror("Error", "Incorrect Username or Password")
#Creates window for grades and sets specifications
class GradesWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("512x512")
        self.bg = PhotoImage(file="538738.png")
        self.label1 = Label(self.root, image=self.bg)
        self.label1.place(x=0, y=0)
        self.grad = StringVar()
        self.clas = StringVar()
        self.classes = []
        self.grades = []
        self.setup_grades()
#Sets up boxes for grades and classes entry
    def setup_grades(self):
        Entry(self.root, textvariable=self.clas).grid(row=0, column=0)
        Entry(self.root, textvariable=self.grad).grid(row=0, column=1)
        Button(self.root, text="Add class and Grade", command=self.add).grid(row=0, column=2)

        self.root.mainloop()
#creates button for calculating GPA
    def add(self):
        grade = self.grad.get()
        classs = self.clas.get()
        self.grades.append(grade)
        self.classes.append(classs)
        self.grad.set("")
        self.clas.set("")
        for x in range(len(self.classes)):
            lexll = f"class: {self.classes[x]} score: {self.grades[x]}"
            Label(self.root, text=lexll).grid(row=1 + x)

        Button(self.root, text="Calculate GPA", command=self.calc).grid(row=len(self.classes) + 1)
#Algorithm to determine GPA 
    def calc(self):
        total_points = sum([int(x) for x in self.grades])
        num_classes = len(self.grades)
        gpa = total_points / num_classes / 20
        gpa = round(gpa, 2)
        Label(self.root, text="Your GPA is " + str(gpa)).grid(row=len(self.classes) + 2, column=2)

app = LoginWindow(root)
root.mainloop()