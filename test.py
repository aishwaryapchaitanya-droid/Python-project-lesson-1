class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.is_borrowed =  False 

    def borrow(self):
        self.is_borrowed= True
        print(self.title, "has been borrowed ")

    def return_book(self):
        self.is_borrowed =  False 
        print(self.title, "has been returned")
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("A good girls guide to murder", "Holly Jackson")
book3 = Book("Once upon a broken heart", "Stephane Garber")


book1.borrow()
book2.borrow()
book2.return_book()
book3.borrow()