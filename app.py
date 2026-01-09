import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="\U0001f468\u200d\U0001f4bb",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .header-title {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77e5;
        margin-bottom: 0.5rem;
    }
    .skill-tag {
        display: inline-block;
        background-color: #e8f4f8;
        padding: 0.5rem 1rem;
        margin: 0.3rem;
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("Navigation")
    page = st.radio("", ["Home", "About", "Projects", "Skills", "Contact"])

if page == "Home":
    st.markdown('<p class="header-title">Hi! Welcome</p>', unsafe_allow_html=True)
    st.write("A passionate developer building amazing projects")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Projects", "15+")
    with col2:
        st.metric("Experience", "3+ Years")
    with col3:
        st.metric("Happy Clients", "20+")
    with col4:
        st.metric("Commits", "1000+")

elif page == "About":
    st.title("About Me")
    st.write("I am a passionate developer with expertise in Python, web development, and data science.")
    st.info("Key Skills: Full-stack Development, Problem Solving, Learning & Collaboration")

elif page == "Projects":
    st.title("My Projects")
    projects = [
        {"title": "E-Commerce Platform", "tech": ["Python", "Flask", "React"]},
        {"title": "AI Chat Assistant", "tech": ["Python", "TensorFlow", "Streamlit"]},
        {"title": "Data Dashboard", "tech": ["Python", "Pandas", "Plotly"]}
    ]
    for project in projects:
        st.subheader(project["title"])
        st.write(f"Tech: {', '.join(project['tech'])}")

elif page == "Skills":
    st.title("Skills")
    skills = {"Backend": ["Python", "Django", "Flask"], "Frontend": ["React", "HTML/CSS"], "Databases": ["PostgreSQL", "MongoDB"]}
    for category, skill_list in skills.items():
        st.subheader(category)
        for skill in skill_list:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

elif page == "Contact":
    st.title("Get In Touch")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message", height=150)
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thanks for your message!")

st.divider()
st.markdown("<div style='text-align: center'><p>2024 | Built with Streamlit</p></div>", unsafe_allow_html=True)
