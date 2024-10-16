import numpy as np
import streamlit as st
from processes.matrix_reader import reader

st.title("Matrix Operations")
st.divider()

st.sidebar.page_link("app.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/basics.py", label="Basic Operations [Matrix]", icon="1️⃣")
st.sidebar.page_link("pages/advanced.py", label="Advanced Topics [Matrix]", icon="2️⃣")

st.switch_page('pages\\intro.py')
