def main():
    

    x=input()
    fobj=open(x, "r")
    Data=fobj.readlines()
    a=0
    for i in range(len(Data)):
        a=a+1
    print(f"Total Number of lines in {a} is : ")

    
        

if __name__=="__main__":
    main()
