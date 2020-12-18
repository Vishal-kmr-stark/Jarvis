from tkinter import *

root=Tk()

canvas_width=800
canvas_height=500
root.geometry(f"{canvas_width}x{canvas_height}")

root.title("vishaal")
can_widg=Canvas(root,width=canvas_width,height=canvas_height)
can_widg.pack()

# can_widg.create_line(0,70,400,90)
can_widg.create_rectangle(10,20,300,400,fill="#00ffff")
can_widg.create_text(150,200,text="vishaal",font="helvetica,20,bold")
can_widg.create_oval(10,20,300,400)




root.mainloop()
