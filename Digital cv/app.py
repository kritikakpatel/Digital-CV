from pathlib import Path

import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if"__file__" in locals() else Path.cwd()
css_file = current_dir / "styles"/ "main.css"
resume_file = current_dir / "assests" / "Kritika Patel CV doc.pdf"
profile_pic = current_dir / "assests" / "Image.jpeg"





# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Kritika Patel"
PAGE_ICON = ":wave:"
NAME = "Kritika Patel"
DESCRIPTION = """
Purpose driven Software Developer with experience in App Development, Databases and Website Development. 
"""
EMAIL = "kritikakpatel2000@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/kritika-patel143/",
    "GitHub": "https://github.com/kritikakpatel",
}
PROJECTS = {
    "🏆 Machine Learning-based model for Early Prediction of Breast Cancer Survival": "https://github.com/kritikakpatel/Machine-Learning-based-Model-for-Early-Prediction-of-Breast-Cancer-Survival",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")
   # --- Education 1
st.write("🚧", "** MSc Computer Science **")
st.write("University of Greenwich | UK, England, London | 2023")

# --- Education 2
st.write("🚧", "** Bachelor Computer Engineering **")
st.write("Charotar University of Science and Technology (CHARUSAT) | Anand, Gujarat, India | 2022")


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: C/C++, Java, .NET, XML, Servlets, SQL
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Web Development: HTML, CSS, Javascript, PHP
- 🗄️ Development Tools: Sublime Text, Eclipse, Visual Studio, GitHub, Microsoft Azure
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Analyst Intern | Capgemini**")
st.write("January 2022 - April 20222, Maharastra, Mumbai ")
st.write(
    """
- ► Facilitating the manager about the tweaks and changes to be made in a high-profile project.
- ► Fixing the bugs prompted while the project was in motion.
- ► Testing and coding of the software using Microsoft Azure, JavaScript and WildFly server.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Application Development Intern | Employa Technologies**")
st.write("May 2021 - June 2021, Gujarat, Vadodara")
st.write(
    """
- ► Creation of a website and transferring it into an application on Android and MacOS.
- ► Using PHP, MySQL, Google Firebase to perform tasks on the live projects.
- ► Point of contact to the clients for the changes to be made in the project and the application developed.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
