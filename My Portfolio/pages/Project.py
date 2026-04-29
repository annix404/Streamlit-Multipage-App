import streamlit as st

st.title("📂 Projects")

project = st.selectbox("Choose a Project", [
    "Python Activities",
    "Networking Assignment"
    "School Activities"
])

st.success(f"You selected: {project}")