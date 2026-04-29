import streamlit as st

st.title("📞 Contact Me")

name = st.text_input("Rachel")
message = st.text_area("Your Message")

if st.button("Send"):
    st.success("Message Sent Successfully!")