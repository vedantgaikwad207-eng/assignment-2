import streamlit as st 

st.title("Check Even or odd for two numbers ")

a=st.number_input("Enter the first no. : ",value=0,step=1)
b=st.number_input("Enter the second no. : ",value=0,step=1)

if st.button("Check"):
    if a%2==0:

        st.success("Even no. is : "+str(a))
    else : 
        st.success("odd no. is : "+str(a))

    if b%2==0:
        st.success("Even no. is : "+str(b))
    else :
        st.success("odd no. is : "+str(b))

    
        
