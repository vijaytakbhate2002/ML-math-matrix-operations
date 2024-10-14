import numpy as np
import streamlit as st
from processes.matrix_reader import reader
import logging
import sys
sys.path.append('\\'.join(__file__.split('\\')[:-2]))
from processes.quick_help import user_guide

st.sidebar.page_link("app.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/basics.py", label="Basic Operations [Matrix]", icon="1️⃣")
st.sidebar.page_link("pages/advanced.py", label="Advanced Topics [Matrix]", icon="2️⃣")

logging.basicConfig(filename='log_file.log', encoding='utf-8')
col1, col2 = st.columns(2)

with col1:
    user_input1 = st.text_area(label="Enter matrix 1")
    try:
        user_input1 = reader(user_input1.split('\n'))
    except:
        user_guide()
    st.session_state.mtx1 = user_input1

with col2:
    user_input2 = st.text_area(label="Enter matrix 2")
    try:
        user_input2 = reader(user_input2.split('\n'))
    except:
        user_guide()
    st.session_state.mtx2 = user_input2

st.sidebar.subheader("Input Matrices", divider='gray')
col3, col4 = st.sidebar.columns(2)
st.subheader("Arithmetic Operations [Matrix]", divider='gray',)
col1, col2 = st.columns(2)
st.write("---")

if 'mtx1' in st.session_state:
    mtx1 = st.session_state.mtx1
else:
    mtx1 = np.matrix([0])

if 'mtx2' in st.session_state:
    mtx2 = st.session_state.mtx2
else:
    mtx2 = np.matrix([0])

with col3:
    st.text("Matrix 1")
    st.write(mtx1)
with col4:
    st.text("Matrix 2")
    st.write(mtx2)

with col1:
    try:
        st.text("Addition")
        st.write(mtx1 + mtx2)
    except:
        st.info(f"Could not compute for this input")
        
    try:
        st.text("Dot Product")
        st.write(np.dot(mtx1,mtx2))
        st.text("Element-wise Multiplicatin")
        st.write(np.multiply(mtx1, mtx2))
    except:
        st.info(f"Could not compute for this input")
        
with col2:
    try:
        st.text("Subtraction")
        st.write(mtx1 - mtx2)
    except:
        st.info(f"Could not compute for this input")
        
    try:
        st.text("Division")
        st.write(mtx1 / mtx2)
    except:
        st.info(f"Could not compute for this input")
        
