from tkinter import *

root=Tk()
root.geometry("800x500")

root.title("Vishal Industry")

f1=Frame(root,bg="light green",borderwidth=7,relief=RIDGE)
f1.pack(side=LEFT,fill="y")

f3=Frame(root,bg="light green",borderwidth=7,relief=RIDGE,pady=150)
f3.pack(side=BOTTOM,fill="x")

f2=Frame(root,bg="light green",borderwidth=7,relief=RAISED,pady=30)
f2.pack(fill="x")

l1=Label(f1,text="New\t\t>\n\n New project \t > \n\n file\t\t > \n\n Open\t\t > \n\n Save \t\t > \n\n Settings\t > ",bg="light green",pady=120,font="Helvetica 8 bold")
l1.pack()
l2=Label(f2,text="PY CHARM",bg="light green",font="Helvetica 40 bold", pady=22)
l2.pack(fill="y")
l3=Label(f3,text="by Vishaal",bg="light green",font="Helvetica 16 bold", pady=22)
l3.pack(fill="y",side=RIGHT)


root.mainloop()