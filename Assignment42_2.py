import math

def Euc(p1,p2):
    Ans = math.sqrt((p1["X"]-p2["X"])**2+(p1["Y"]-p2["Y"])**2)
    return Ans 

def Userdefined(NX,NY):
    border="*"*50
    Data=[
        {"Point":"A","X":1,"Y":2,"Label":"Red"},
        {"Point":"B","X":2,"Y":3,"Label":"Red"},
        {"Point":"C","X":3,"Y":1,"Label":"Blue"},
        {"Point":"D","X":6,"Y":5,"Label":"Blue"}

    ]
    print(border)
    print("The Data is : ")
    for i in Data :
        print(i)
    print(border)
    
    new_point={"X":NX,"Y":NY}
    for d in Data:
        d["distance"]=Euc(d,new_point)
    print(border)

    print("Data with distance is : ")
    for i in Data:
        print(i)
    print(border)

    sorted_data=sorted(Data , key=lambda item : item["distance"])
    print("Sorted data is : ")
    for i in sorted_data:
        print(i)
    print(border)
    K_values=[1,3,5]
    for k in K_values:
        sorted_data=sorted_data[:k]

        votes={}
        for d in sorted_data:
            label=d["Label"]
            votes[label]=votes.get(label,0)+1
        print(border)

        print("Resulting votes are :",votes)
        print(border)

        a=0
        name='' 
        for d in votes:
            if(votes[d]>a):
                a=votes[d]
                name=d
        print(f"Final prediction for k value {k} is : {name}")
        print(border)








def main():
    x=int(input("Enter X coordinate"))
    y=int(input("Enter Y coordinate"))
    Userdefined(x,y)


if __name__=="__main__":
    main()