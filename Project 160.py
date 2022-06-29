from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("500x500")
root.title("Project 160")
root.configure( bg = "teal")

open1 = ImageTk.PhotoImage(Image.open("open.png"))
save1 = ImageTk.PhotoImage(Image.open("save.png"))
exit1 = ImageTk.PhotoImage(Image.open("exit.jpg"))
label_name = Label(root, text = "File Name : ")
label_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)
input1 = Entry(root)
input1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
text1 = Text(root, height = 5, width = 20, bg = "white", fg = "blue")
text1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()