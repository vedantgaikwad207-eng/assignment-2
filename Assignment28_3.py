def main():
    x=input("Enter the file name : ")
    fobj=open(x,"r")
    Data=fobj.read()
    for i in Data :
        print(i , end="")

if __name__=="__main__":
    main()
    