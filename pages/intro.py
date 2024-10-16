import streamlit as st

st.sidebar.page_link("app.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/basics.py", label="Basic Operations [Matrix]", icon="1️⃣")
st.sidebar.page_link("pages/advanced.py", label="Advanced Topics [Matrix]", icon="2️⃣")
st.sidebar.page_link("pages/contact_page.py", label="Developer", icon="3️⃣")

st.title("Welcome to the Matrix Operations")
st.divider()
st.markdown("""
### Understanding Matrix Operations and Real-Life Applications

Matrices are fundamental tools in various fields, ranging from computer science and engineering to economics and physics. They offer a structured way to handle complex data, making operations such as transformation, optimization, and solving linear equations more efficient. This web application is designed to give you hands-on experience with both basic and advanced matrix operations, using Python’s powerful NumPy library.

#### Why Are Matrices Important?
Matrices are integral to many real-world applications:
- **Computer Graphics**: Used for transforming objects (rotation, scaling, translation) in 3D space.
- **Machine Learning**: Matrices handle data in algorithms, especially for operations like matrix multiplication in neural networks.
- **Physics and Engineering**: Represent systems of linear equations to model phenomena such as electrical circuits and mechanical systems.
- **Economics**: Used to analyze input-output models and interdependent markets.

---

### Matrix Operations in This Application

The application consists of three sections: **Home**, **Basic Operations**, and **Advanced Topics**, each offering different levels of matrix manipulation.

#### 1. Basic Matrix Operations

The basic operations page allows you to perform essential matrix operations:
- **Matrix Addition**: Add two matrices element-wise.
- **Matrix Subtraction**: Subtract one matrix from another element-wise.
- **Dot Product**: Multiply two matrices.
- **Matrix Division**: Perform element-wise division (though rare in practical scenarios).

---

### Real-World Application: Image Brightness Adjustment (Example)

Consider an image as a matrix where each element represents a pixel value. To adjust brightness (increasing means adding values to each pixel), we perform matrix addition.

Suppose we have a simple 3x3 matrix representing an image:

**Matrix A** (original image):
```
[[50, 80, 90], 
 [60, 70, 100], 
 [85, 95, 120]]
```

If we want to increase brightness by adding 10 to each pixel, we use:

**Matrix B** (brightness adjustment):
```
[[10, 10, 10], 
 [10, 10, 10], 
 [10, 10, 10]]
```

After matrix addition, the result is:
```
[[60, 90, 100], 
 [70, 80, 110], 
 [95, 105, 130]]
```

This simple operation is commonly used in image processing and highlights how basic matrix operations have real-world applications.

---

#### 2. Advanced Matrix Operations

For more complex tasks, the advanced operations page provides:
- **Matrix Transposition**: Flip the matrix over its diagonal (rows become columns).
- **Matrix Inversion**: Calculate the inverse, crucial for solving systems of linear equations.
- **Matrix Determinant**: Useful in determining if a matrix is invertible.
- **Eigenvalues and Eigenvectors**: Essential in data science and physics.
- **Matrix Trace**: Sum of diagonal elements, used in optimization algorithms.
- **Matrix Rank**: Shows the number of independent rows/columns.
- **Singular Value Decomposition (SVD)**: Breaks down matrices for dimensionality reduction and data compression.

---

### Case Study: Eigenvalues and Eigenvectors in Google PageRank

Google’s PageRank algorithm uses **eigenvalues** and **eigenvectors** to rank web pages. The web can be represented as a giant matrix where each element reflects the likelihood of moving from one webpage to another. The eigenvectors reveal the importance of each page in this matrix.

---

### Example: Eigenvalue and Eigenvector Calculation

Consider a simple 2x2 matrix:
```
[[2, 1], 
 [1, 2]]
```

The eigenvalues and eigenvectors of this matrix are:
- **Eigenvalues**: λ = 3, 1
- **Eigenvectors**:
  - For λ = 3: [1, 1]
  - For λ = 1: [-1, 1]

This illustrates the core concept of eigenvalues and eigenvectors, widely used in physics, machine learning, and other fields.

---

### Conclusion: Why This Application Matters

This application brings the power of matrices to your fingertips, allowing you to understand and manipulate them with ease. From basic operations like matrix addition to advanced computations like SVD and eigenvalue decomposition, this tool provides a comprehensive introduction to matrix theory and its practical applications.
""")

