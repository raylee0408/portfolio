import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
    #can change image size with width=600

with col2:
    st.title("Ray Lee")
    content = """
    Hi, I am Ray, a Python developer with a keen interest in 
    building innovative applications. I have been working on 
    various projects, including a recent attempt to run a 
    Streamlit application. My experience involves navigating 
    through different environments and troubleshooting common 
    issues that arise during development. I am passionate about 
    learning and expanding my skills in Python, focusing on web 
    development and data analysis. With a strong foundation in 
    programming principles, I aim to contribute to projects 
    that leverage Python's versatility and efficiency.
    """
    st.info(content)
    #st.write just write the content, but .info give the nice background
