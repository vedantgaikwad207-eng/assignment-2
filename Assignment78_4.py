import streamlit as st 

st.title("Student Result Calculator")

a=st.text_input("Name of student : ",value="Name")
b=st.number_input("Marks of first subject : ",value=0,step=1,key="First")
c=st.number_input("Marks of second subject : ",value=0,step=1,key="second")
d=st.number_input("Marks of third subject : ",value=0,step=1,key="third")


if st.button("Check"):
    total_marks= b+c+d
    percen= (total_marks/300)*100
    if(b>=40 and c>=40 and d>=40):

    

        st.success(f"""\n
        Name of student : {a} \n
        Total marks obtained : {total_marks}/300 \n 
        Percentage : {percen} \n
        Result : Pass
                    """)

    else : 
        
        st.success(f"""\n
        Name of student : {a} \n
        Total marks obtained : {total_marks}/300 \n
        Percentage : {percen} \n
        Result : Unsuccessful 
                    """)
