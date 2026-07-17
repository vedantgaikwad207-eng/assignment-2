class BankAccount :
    ROI=10.5

    def __init__(self):
        self.Name=input("Account Holder Name : ")
        self.Amount= int(input("Account Balance : "))

    def Display(self):
        print("Accoutn Holder Name is : ", self.Name)
        print("Account Balance is :", self.Amount)

    def Deposit(self):
        self.x=int(input("Amount to be Deposit : "))
        self.Amount = self.Amount + self.x


    def Withdraw(self):
        self.y=int(input("Amount to be withdraw : "))
        self.Amount= self.Amount - self.y

    def CalculateInterest(self):
        self.Interest=(self.Amount*BankAccount.ROI)/100
        return self.Interest
    
obj1=BankAccount()
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
print("Interest is : ")
print(obj1.CalculateInterest())

