from tkinter import *
win = 20
def check():
    user_guess = int(guess.get())
    if user_guess  == win:
        msg = "YOU WIN..!!!"
    elif user_guess > win:
        msg = "Too High..!!"
    elif user_guess < win:
        msg = "Too Low..!!"
    else:
        print("Something wrong..!!")
    l2["text"] = msg

root= Tk()
l1 = Label(root, text="Welcome to the guessing Game!")
l2 = Label(root, text="Good Luck!")
b1 = Button(root, text="Check",fg="green", command=check )
b2 = Button(root, text="reset",fg="red", command=root.quit )
guess= Entry(root, width=3)
l1.pack()
l2.pack()
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
guess.pack()
root.mainloop()
root.destroy()


