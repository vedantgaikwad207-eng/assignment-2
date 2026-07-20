def main():
    x=input("Enter file name : ")
    fobj=open(x,"r")
    Data=fobj.read()
    print(Data)

if __name__=="__main__":
    main()
    