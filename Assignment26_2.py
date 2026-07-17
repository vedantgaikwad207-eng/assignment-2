class Circle :
    
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        self.Radius=float(input("Enter the Value of Radius : "))

    def CalculateArea(self):
        self.Area=self.Radius*self.Radius*Circle.PI

    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius

    def Display(self):
        print("Radius is :",self.Radius)
        print("Area is :",self.Area)
        print("Circumference is :" , self.Circumference)


obj1=Circle()
obj1.Radius
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()


        
