import streamlit as st 

st.title("Simple interest Calculator ")

Principle_amt=st.number_input("Principal Amount : ",value=0,step=1,key="Principle_Amount")
Rate=st.number_input("Rate of interest : ",value=0,step=1,key="Rate")
Time=st.number_input("Rate of interest : ",value=0,step=1,key="Time")


if st.button("Calculate"):
    result = Principle_amt*Rate*Time/100
    

    st.success("Simple interest : "+str(result))

