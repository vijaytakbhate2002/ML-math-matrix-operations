import streamlit as st

st.sidebar.page_link("app.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/basics.py", label="Basic Operations [Matrix]", icon="1️⃣")
st.sidebar.page_link("pages/advanced.py", label="Advanced Topics [Matrix]", icon="2️⃣")
st.sidebar.page_link("pages/contact_page.py", label="Developer", icon="3️⃣")

st.title("Hiring? Contact Me")

st.markdown("""
## Vijay Dipak Takbhate
👋 **Machine Learning Engineer | Data Scientist | Data Analyst**

Welcome to my contact page! I'm actively seeking opportunities where I can leverage my expertise in Data Science, Python development, and data analysis to drive impactful solutions. Let's connect and explore how we can collaborate!

---

### Get in Touch

- 📞 **Phone**: +91 8767363681
- 📧 **Email**: [vijaytakbhate20@gmail.com](mailto:vijay.takbhate@gmail.com)
- 🌐 **LinkedIn**: [Vijay Dipak Takbhate](https://www.linkedin.com/in/vijay-takbhate-b9231a236/)

---

### Download My Resume
[📄 Download Resume](statics/Resume.pdf)

---

### Featured Article:
🚀 [**The Essential Yet Overlooked Concept in Machine Learning: The Matrix**](https://www.linkedin.com/pulse/essential-yet-overlooked-concept-machine-learning-matrix-takbhate-wrzqc/)

Check out my article where I dive deep into the role of matrices in machine learning and why this fundamental concept deserves more attention!
""")
