def main():
    x=int(input("Enter the No. : "))
    for i in range(x):
        print("\n")
        for i in range(x):
            print("*"," ",end="")
        x=x-1
        

if __name__=="__main__":
    main()