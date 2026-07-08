from MarvellousNum import ChkPrime
def main():
    x=int(input("Enter the No. of the elements :"))
    Result=[]
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        Result.append(x)
    ChkPrime(Result)

if __name__=="__main__":
    main()

