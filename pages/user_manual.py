import streamlit as st
import sys
sys.path.append('\\'.join(__file__.split('\\')[:-2]))

st.sidebar.page_link("app.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/basics.py", label="Basic Operations [Matrix]", icon="1️⃣")
st.sidebar.page_link("pages/advanced.py", label="Advanced Topics [Matrix]", icon="2️⃣")
st.sidebar.page_link("pages/contact_page.py", label="Developer", icon="3️⃣")

st.title("User Guide for Matrix Operations Web Application")

st.markdown("""
Welcome to the Matrix Operations Web Application! This guide will help you understand how to use the features of the site, particularly focusing on how to input matrices for calculations.
""")

st.header("Inputting Matrices")

st.markdown("""
To perform operations on matrices, you need to input them in a specific format. Here are the steps to guide you through the process:

1. **Matrix Format**: You should represent the matrix by entering space-separated values for each row, with each row on a new line.

   For example, to input the following matrix:
   ```
   [[1, 2, 3],
    [4, 5, 6]]
   ```
   You would enter it as:
   ```
   1 2 3
   4 5 6
   ```

2. **Input Fields**: There are two text areas provided on the **Basic Operations** page where you can enter your matrices. Ensure that you follow the format described above.

3. **Example**: Here’s an example of how to input two matrices:
   - **Matrix A**:
   ```
   1 2 3
   4 5 6
   ```
   - **Matrix B**:
   ```
   9 8 7
   6 5 4
   ```
   
   Input these in their respective fields and click the operation you wish to perform.

4. **Snapshot**: To give you a clearer idea of how to input values, refer to the snapshot below:
""")

st.image("user_guide/input_rules.PNG", caption="Matrix Input Example", use_column_width=True)

st.markdown("""
After entering the matrices, you can proceed to perform operations such as addition, subtraction, dot product, and more. Make sure the matrices you input are compatible for the operations you wish to perform.

If you have any further questions or need assistance, please feel free to reach out!
""")


