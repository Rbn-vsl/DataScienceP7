"""
https://discuss.streamlit.io/t/are-you-using-html-in-markdown-tell-us-why/96/25
"""
import streamlit as st
import os

def local_css(file_name):
    # Get the current working directory
    cwd = os.getcwd()
    name = "style.css"
    file_name = os.path.join(cwd, name)
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
