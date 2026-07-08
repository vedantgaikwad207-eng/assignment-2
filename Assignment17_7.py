def main():
    x=int(input("Enter the No. :"))
    for i in range(1,x+1):
        print(end="\n")
        for i in range(1,x+1):
            print(i," ",end="")


if __name__=="__main__":
    main()