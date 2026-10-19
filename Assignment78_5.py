import streamlit as st 

st.title("Conversion of temperature from celsius to fahrenheit")

a=st.number_input("Enter the temperature in Celsius : ",value=0,step=1)

if st.button("Convert"):
    result = (9/5)*a+32
    

    st.success("Temperature in Fahrenheit is : "+str(result))

