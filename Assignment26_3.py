class Arithmetic :
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter the first no. : "))
        self.Value2=int(input("Enter the second no. : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self ):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1*self.Value2
    
    def Division(self):
        try :

            print(self.Value1/self.Value2)
        except ZeroDivisionError :
            print("Division by zero not possible ")

obj1=Arithmetic()
obj1.Accept()
print("Addition is : ", obj1.Addition())
print("Subtraction is : ", obj1.Subtraction())
print("Division is : ", end="")
obj1.Division()
print("Multiplication is : ", obj1.Multiplication())

    

    
