import streamlit as st 

st.title("Addition of two numbers ")

a=st.number_input("Enter the first no. : ",value=0,step=1)
b=st.number_input("Enter the second no. : ",value=0,step=1)

if st.button("Addition"):
    result = a+b
    

    st.success("Addition is : "+str(result))

