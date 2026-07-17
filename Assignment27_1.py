class Bookstore :

    NoofBook=0

    def __init__(self):
        self.Name=input("Enter the Name of book : ")
        self.Author = input("Enter the Author name : ")
        Bookstore.NoofBook=Bookstore.NoofBook+1

    def Display(self):
        print(f"{self.Name} by {self.Author}  No. of Books : {Bookstore.NoofBook}")

obj1=Bookstore()
obj1.Display()

obj2=Bookstore()
obj2.Display()
