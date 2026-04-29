import streamlit as st

st.title("💡My Skills")
st.write("This page shows my skills, talents, and abilities that help me grow academically and personally.")

st.subheader("🎯Core Skills")

st.write("🎨Arts")
st.progress(95)

st.write("🖌️Design")
st.progress(89)

st.write("🤝Teamwork")
st.progress(90)

st.write("💬Communication")
st.progress(93)

st.write("🏳️‍⚧️English language")
st.progress(90)

st.subheader("✨ What I Can Do")

col1, col2 = st.columns(2)

with col1:
    st.success("🎨 Create artworks and creative ideas")
    st.success("🖌 Make poems and simple and writing story")
    st.success("🤝 Cooperate well in group activities")

with col2:
    st.info("💬 Express ideas clearly")
    st.info("🇬🇧 Understand and use English well")
    st.info("🌟 Adapt and learn quickly")

st.subheader("📚 Skills in Action")

st.markdown("""
- Participated in school art and design projects  
- Worked with classmates during group tasks  
- Presented reports in front of class  
- Used English in writing and speaking activities  
- Created creative outputs for assignments  
""")


st.subheader("🚀 Skills to Improve More")

st.markdown("""
- Advanced designing  
- Better public speaking  
- Stronger leadership  
- More confidence in English speaking  
""")

st.subheader("💬 Motivation")

st.info("Skills become stronger through practice and experience.")
