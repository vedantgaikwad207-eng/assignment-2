def ChkPrime(No):
    count=1
    sum=0
    for i in No:
        if(i%count==0):
            count=count+1
            sum = sum + i
    print("The Addition of prime no. is : ", sum)

