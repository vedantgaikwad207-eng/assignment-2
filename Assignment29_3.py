import sys
def main():
    x=sys.argv[1]
    fobj=open(x,"r")
    Data=fobj.read()
    y=sys.argv[2]
    dobj=open(y,"w")
    dobj.write(Data)
    print(f"contentx of {x} successfully copied into {y}")

if __name__=="__main__":
    main()
