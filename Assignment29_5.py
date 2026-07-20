import sys

def main():
    a=0
    x=sys.argv[1]
    fobj=open(x,"r")
    Data=fobj.read()
    y=sys.argv[2]
    for i in Data :
        if(i==y):
            a=a+1
    print("Frequency of letter repeated is :",a )


if __name__=="__main__":
    main()