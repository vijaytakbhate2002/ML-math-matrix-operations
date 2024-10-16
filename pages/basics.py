import numpy as np
import streamlit as st
from processes.matrix_reader import reader
import sys
sys.path.append('\\'.join(__file__.split('\\')[:-2]))
from processes.quick_help import user_guide

st.sidebar.page_link("app.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/basics.py", label="Basic Operations [Matrix]", icon="1️⃣")
st.sidebar.page_link("pages/advanced.py", label="Advanced Topics [Matrix]", icon="2️⃣")
st.sidebar.page_link("pages/contact_page.py", label="Developer", icon="3️⃣")

col1, col2 = st.columns(2)

with col1:
    user_input1_text = st.text_area(label="Enter matrix 1")
    try:
        user_input1 = reader(user_input1_text.split('\n'))
    except:
        user_guide()

with col2:
    user_input2_text = st.text_area(label="Enter matrix 2")
    try:
        user_input2 = reader(user_input2_text.split('\n'))
    except:
        user_guide()

st.sidebar.subheader("Input Matrices", divider='gray')
col3, col4 = st.sidebar.columns(2)
st.subheader("Arithmetic Operations [Matrix]", divider='gray',)
col1, col2 = st.columns(2)
st.write("---")

with col3:
    st.text("Matrix 1")
    st.write(user_input1)
with col4:
    st.text("Matrix 2")
    st.write(user_input2)

with col1:
    try:
        st.text("Addition")
        st.write(user_input1 + user_input2)
    except:
        st.info(f"Could not compute for this input")
        
    try:
        st.text("Dot Product")
        st.write(np.dot(user_input1, user_input2))
        st.text("Element-wise Multiplicatin")
        st.write(np.multiply(user_input1, user_input2))
    except:
        st.info(f"Could not compute for this input")
        
with col2:
    try:
        st.text("Subtraction")
        st.write(user_input1 - user_input2)
    except:
        st.info(f"Could not compute for this input")
        
    try:
        st.text("Division")
        st.write(user_input1 / user_input2)
    except:
        st.info(f"Could not compute for this input")
        
