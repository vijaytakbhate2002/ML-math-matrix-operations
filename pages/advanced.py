import numpy as np
import streamlit as st
from processes.matrix_reader import reader
import logging
from processes.quick_help import user_guide

st.sidebar.page_link("app.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/basics.py", label="Basic Operations [Matrix]", icon="1️⃣")
st.sidebar.page_link("pages/advanced.py", label="Advanced Topics [Matrix]", icon="2️⃣")

logger = logging.getLogger(__name__)
logging.basicConfig(filename='log_file.log', encoding='utf-8')
col1, col2 = st.columns(2)

with col1:
    user_input = st.text_area(label="Enter matrix 1")
    try:
        user_input = reader(user_input.split('\n'))
    except:
        user_guide()
    st.session_state.mtx = user_input
    st.sidebar.subheader("Input Matrix", divider='gray')
    st.sidebar.write(user_input)

st.subheader("Transpose and Inversion [Matrix]", divider='gray')
col1, col2= st.columns(2)
st.subheader("Eigenvectors, Eigenvalues [Matrix]", divider='gray')
col3, col4 = st.columns(2)
st.subheader("Trace, Rank and Determinant [Matrix]", divider='gray')
col5, col6, col7 = st.columns(3)
st.subheader("Singular Value Decomposition [Matrix]", divider='gray')
col8, col9, col10 = st.columns(3)

with col1:
    try:
        st.text("Matrix Transpose")
        st.write(np.matrix.transpose(user_input))
    except:
        st.info(f"Could not compute for this input")


with col2:
    try:
        st.text("Matrix Inverse")
        st.write(np.linalg.inv(user_input))
    except:
        st.info(f"Could not compute for this input")

with col3:
    try:
        st.text("Eigenvalues")
        eigenvalues = np.linalg.eigvals(user_input)
        st.write(eigenvalues)
    except:
        st.info(f"Could not compute for this input")

with col4:
    try:
        st.text("Eigenvectors")
        eigenvectors = np.linalg.eig(user_input)[1]
        st.write(eigenvectors)
    except:
        st.info(f"Could not compute for this input")

with col5:
    try:
        st.text("Trace")
        trace1 = np.trace(user_input)
        st.write(trace1)
    except:
        st.info(f"Could not compute for this input")

with col6:
    try:
        st.text("Rank")
        rank1 = np.linalg.matrix_rank(user_input)
        st.write(rank1)
    except:
        st.info(f"Could not compute for this input")

with col7:
    try:
        st.text("Determinant")
        determinant1 = np.linalg.det(user_input)
        st.write(determinant1)
    except:
        st.info(f"Could not compute for this input")

try:
    U1, S1, VT1 = np.linalg.svd(user_input)
except:
    st.info(f"Could not compute for this input")
    
with col8:
    try:
        st.text("U (Orthogonal matrix)")
        st.write(np.matrix(U1))
    except:
        st.info(f"Could not compute for this input")

with col9:
    try:
        st.text("Diagnoal matrix")
        st.write(S1)
    except Exception as e:
        st.info(f"Could not compute for this input")

with col10:
    try:
        st.text("V transpose (Orthogonal matrix)")
        st.write(VT1)
    except Exception as e:
        st.info(f"Could not compute for this input")

st.write("---")