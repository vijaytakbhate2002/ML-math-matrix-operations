import numpy as np
import streamlit as st
from processes.matrix_reader import reader
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='log_file.log', encoding='utf-8')
col1, col2 = st.columns(2)

with col1:
    mtx1 = st.text_area(label="Enter matrix 1")
    mtx1 = reader(mtx1.split('\n'))
    st.write(mtx1)

with col2:
    mtx2 = st.text_area(label="Enter matrix 2")
    mtx2 = reader(mtx2.split('\n'))
    st.write(mtx2)

