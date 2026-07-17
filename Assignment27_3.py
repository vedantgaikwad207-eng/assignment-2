class Numbers :
    def __init__(self):
        self.Value=int(input("Enter the No. : "))

    def ChkPrime(self):
        print("Is the No. Prime No ? ")

        a=0
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                a=a+1
        if(a==2):
            print("True")
        else :
            print("False ")

    def ChkPerfect(self):
        print("Is the No. Perfect No. ? ")
        a=0
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                a=a+i
        if(self.Value==a):
            print("True")
        else :
            print("False ")

    def Factors(self):
        print("Factors are : ")
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                print(i,end=" ")
    
    def SumFactors(self ):
        a=0
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                a=a+i
        print(end="\n")

        print("Sum of Factors is : ", a)

obj1=Numbers()
obj1.ChkPrime()
obj1.ChkPerfect()
obj1.Factors()
obj1.SumFactors()
