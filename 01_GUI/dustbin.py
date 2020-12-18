from tkinter import *
root = Tk()
root.title("My Frist Pro")
root.geometry("1110x850")
root.minsize(1110, 850)
root.maxsize(1110, 850)

# Heading
H = Label(text="Daily News", font="Elephant 30 bold", bg="black", fg="white", borderwidth=3, padx=5, pady=5, relief=SUNKEN)
H.pack(fill=X)
# date
D = Label(text="Date:-07.06.2020", bg="black", fg="white", borderwidth=3, padx=5, pady=5, relief=SUNKEN)
D.place(x=1000, y=70)

# Left Text-1
T = Label(text='''Muzaffarpur is a city located in Muzaffarpur district in the Tirhut region of the Indian state of
                History. Muzaffarpur's significance in Indian civilisation is due to its position
                 Muzaffarpur Junction railway station is a main railway junction, with two suburban stations,
                  Ram Dayalu Nagar and Narayanpur Anant (Sherpur).''', bg="red", fg="white", padx=5, pady=5)
T.place(x=50, y=100)
# image
# photo = PhotoImage(file="001.png")
# P = Label(image=photo)
# P.place(x=650, y=70)

# Right Text-2
T2 = Label(text='''Muzaffarpur is the lychee bowl of India.According to the Union agriculture ministry,
                   300,000 metric tonne of lychees were produced from 32,000 hectare under cultivation in Bhar in 2017.
                   The children showed symptoms of acute encephalitis syndrome (AES), 
                   a neurological illness that involves inflammation of the brain''', bg="red", fg="white", padx=5, pady=5)
T2.place(x=450, y=275)
# image
# photo1 = PhotoImage(file="004.png")
# P1 = Label(image=photo1)
# P1.place(x=200, y=240)

# Left Text-3
T3 = Label(text='''This is a very famous nd popular temple in the North bihar.It is very neat nd clean. It's looking very 
                            beautiful. In Navratri temple is face very crowd.This is in front of Lic office.''', bg="red", fg="white", padx=5, pady=5)
T3.place(x=50, y=450)
# image
# photo2 = PhotoImage(file="003.png")
# P2 = Label(image=photo2)
# P2.place(x=650, y=430)

# Right Text-4
T3 = Label(text='''Baba Garibnath Temple situated in the center of the Muzaffarpur town is undoubtedly
                   one of the most famous "Lord Shiva" temples ! Its history goes like this-There was a
                   Landlord in ancient times who owned the land where the present temple is.
                   There was a huge Banyan tree in the premises of the temple which provided shade and relief to many people.
                   Unfortunately due to bad financial condition the Landlord had to sell his house to another person.
                   The new owner seemed not too interested in Banyan tree so he ordered it to be cut down to clean the premises.
                   While cutting the tree a "Shivling" was found within it, which got partly damaged due to the swing of the axe,
                   and red water started oozing out from the "Shivling"! The Landlord was quite disturbed after seeing
                   this and was not able to sleep for the entire night. In the morning "Baba Garibnath" appeared in his
                   dreams and said that he was Baba Garibnath-one who has great sympathy for poor.
                   He ordered him to establish the "Shivling" at the same place and call one ''', bg="white", fg="black", padx=5, pady=5)
T3.place(x=450, y=650)
# image
# photo3 = PhotoImage(file="005.png")
# P3 = Label(image=photo3)
# P3.place(x=200, y=675)
root.mainloop()