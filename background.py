from tkinter import *
import random

root = Tk()

root.geometry("600x600")
root.title("Random Backgroud colour")

random_colours = {
    1:"orange",
    2:"blue",
    3:"red",
    4:"white",
    5:"yellow",
    6:"purple",
    7:"green",
    8:"black",
    9:"pink",
    10:"grey",
    11:"brown",
    12:"pink",
    13:"purple",    
}


def Random():
    random_index = random.randint(0, 13)
    random_colour = random_colours[random_index]
    root.configure(bg=random_colour)


btn = Button(root, text="Click here for random background" ,bg="black", fg="white", command=Random)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()