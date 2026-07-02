def main():
    x=int(input("Enter the No. :"))

    odd = lambda x : True if not(x%2==0) else False

    print(odd(x))
    

if __name__=="__main__":
    main()