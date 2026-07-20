import os 

def main():
    x=input("Enter the file name : ")
    fobj= os.path.exists(x)
    if(fobj==True ):
        print(f"{x} file exists ")
    else : 
        print(f"{x} file doesnt exists ")

if __name__=="__main__":
    main()

    
