def main():
    x=input("Enter the file name : ")
    fobj=open(x,"r")
    Data= fobj.read()
    print("Total number of words is : ",len(Data))

if __name__=="__main__":
    main()
    