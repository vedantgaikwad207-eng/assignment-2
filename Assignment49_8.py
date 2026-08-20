def main():
    # 1-> Positive
    # 0 -> Negative
    actual=[1,1,1,1,0,0,0,0]
    predicted=[1,1,0,1,0,1,0,0]
    TN=0
    TP=0
    FN=0
    FP=0
    for i in range(len(actual)):
        if(actual[i]==1 and predicted[i]==1):
            TP=TP+1
        if(actual[i]==1 and predicted[i]==0):
            FN=FN+1
        if(actual[i]==0 and predicted[i]==1):
            FP=FP+1
        if(actual[i]==0 and predicted[i]==0):
            TN=TN+1
    print("True negative :",TN)
    print("True positive ",TP)
    print("False positive ",FP)
    print("False negative ",FN)


if __name__=="__main__":
    main()
    