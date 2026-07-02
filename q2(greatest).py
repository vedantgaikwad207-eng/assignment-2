def main():
    def ChkGreater():
        print("Enter the two no.")
        x=int(input())
        y=int(input())
        if(x>y):
            print(x,"is greater")
        elif(y>x):
            print(y,"is greater")
        else:
            print("Both are equal")

    ChkGreater()
if __name__=="__main__":
    main()


