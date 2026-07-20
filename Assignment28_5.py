def main():
    x=input("Enter the First file name : ")
    fobj= open(x,"r")
    
    y=input("Enter the word to find : ")

    Data=fobj.read()
    if y in Data :
    
        print(f"{y} is found in {x} file ")
    else :
        print(f"{y} is not found in {x} file ")

    
if __name__=="__main__":
    main()

    
            

            
