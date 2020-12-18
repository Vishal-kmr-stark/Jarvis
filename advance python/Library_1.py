class library:

    def __init__(self,listofBook):
        self.book=listofBook

    def displayBooks(self):
        print("The following books are available :-")
        for book in self.book:
            # print("\t")
            print("-> "+ book)

    def borrowBooks(self,bookName):
        if bookName in self.book:
            print(f"Your book {bookName} is issued")
            self.book.remove(bookName)
            return True
        else:
            print("Book is not available now, issued by someone else ")
            return False
    def returnBooks(self,bookName):
        self.book.append(bookName)
        print("Thanks for returning book ")

class Student:
    def borrowBooks(self):
        self.book= input("Enter the book name: ")
        return self.book
    def returnBooks(self):
        self.book= input("Enter the book name: ")
        return self.book

if __name__ == '__main__':

   CentralLibrary=library(["Thermodynamics","Newton's law","Python","Data science"])
   # book1.displayBooks()
   stud=Student()
  

   while(True):

      wlcmsg="""---------------------<~(Welcome to Central library)~>----------------------
      Press 1 to Display books
      Press 2 to Borrow books
      Press 3 to Return/Add books
      Press 4 to Exit
      """
      print(wlcmsg)

      # try:
      A=int((input("Enter your choice: ")))
      # except:
      #     print("Invalid choiice")
      if A==1:
          CentralLibrary.displayBooks()

      elif A==2:

          CentralLibrary.borrowBooks(stud.borrowBooks())


      elif A==3:
          CentralLibrary.returnBooks(stud.returnBooks())

      elif A==4:
          print("Thanks for choosing Central library")
          exit()

      elif A==str():
          print("Invalid")
      else:
          print("Invalid choice")

   print(wlcmsg)

