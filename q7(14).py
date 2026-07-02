def main():
    x=int(input("Enter the No. :"))

    div = lambda x: True if x%5==0 else False
    
    print(div(x))

if __name__=="__main__":
    main()