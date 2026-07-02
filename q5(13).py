def main():
    ret=list()
    print("Enter the marks in five subjects ")
    a=0
    for no in range(5):
        x=int(input())
        ret.append(x)
        a=a+x
    a=a/5
    if(a>=75):
        print("Distinction")
    elif(60<=a<75):
        print("First Class")
    elif(50<=a<60):
        print("Second Class")
    else:
        print("Fail")

if __name__=="__main__":
    main()
    