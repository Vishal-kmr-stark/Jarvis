from tkinter import *
from  PIL import Image,ImageTk

vishal_root=Tk()

vishal_root.geometry("900x1200")

image=Image.open("new image.jpg")
photo=ImageTk.PhotoImage(image)

b_label=Label(text="Yo yo")
b_label.pack()

a_label=Label(image=photo)
a_label.pack()


vishal_root.mainloop()