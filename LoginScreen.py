#Kalen Evans
#1/2021
#Login Screen
from tkinter import *
class App(Frame):
    def __init__(self,master):
        super(App,self).__init__(master)
        self.infoIndex = 0
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        Label(self,
              text="Username"
              ).grid(row=0, column=0, columnspan=1, sticky=W)
        self.username = Entry(self)
        self.username.grid(row=0, column=1, columnspan=2, sticky=W)

        Label(self,
              text="Password"
              ).grid(row=1, column=0, columnspan=1, sticky=W)
        self.password = Entry(self)
        self.password.grid(row=1, column=1, columnspan=2, sticky=W)

        Button(self,
               text="Submit",
               command=self.login
               ).grid(row=2, column=1, pady=10)


    def login(self):
        try:
            textFile = open("Users/Users.txt", "r")
        except:
            print("That file did not exist")
            textFile = open("Users/test.txt", "w+")

        text = textFile.readlines()
        for line in text:
            if self.username.get() == line:
                try:
                    textFile = open("Users/Passwords.txt", "r")
                except:
                    print("That file did not exist")
                    textFile = open("Users/test.txt", "w+")

                text1 = textFile.readlines()
                for line in text:
                    if self.password.get() == line:
                        print("good")
                    else:
                        print("bad")
            else:
                print("bad")

        try:
            textFile = open("Users/Passwords.txt", "r")
        except:
            print("That file did not exist")
            textFile = open("Users/test.txt", "w+")

        text1 = textFile.readlines()
        for line in text:
            if self.password.get() == line:
                print("good")
            else:
                print("bad")

def main():
    root = Tk()
    root.title("Password Entry")
    root.geometry("250x200")
    root.attributes("-fullscreen",False)
    app = App(root)
    root.mainloop()

main()