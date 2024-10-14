import streamlit as st
from PIL import Image
import sys
sys.path.append('\\'.join(__file__.split('\\')[:-2]))

def user_guide(img_path:str="user_guide\\input_rules.PNG") -> None:
    st.warning("invalid input from the user; please checkout the user guide below.")
    with st.expander("User Guid"):
        image = Image.open(img_path)
        st.image(image)
        st.page_link("pages\\user_manual.py", label="For more information, click me. ")
