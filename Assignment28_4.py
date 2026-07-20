def main():
    x=input("Enter the First file name : ")
    fobj= open(x,"r")
    Data= fobj.read()
    y=input("Enter the second File name where to copy the contents ")

    cobj = open(y,"w")
    cobj.write(Data)
    print(f"Contents of {x} copied into {y}")
    

if __name__=="__main__":
    main()
