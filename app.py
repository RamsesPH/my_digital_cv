from pathlib import Path
import streamlit as st
from PIL import Image


# ---- PATH SETTINGS ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir/"assets"/"profile-pic.png"
# KIT = "36a4585365"

# ---- GENERAL VARIABLES ---

PAGE_TITLE = "DIGITAL CV |  Pedro R. Hernandez"
PAGE_ICON = ":wave:"
NAME = "Pedro R. Hernandez"
DESCRIPTION = """
System Administrator and Python Programmer"""

EMAIL = "pedro.hernandez@geolander.ao"
SOCIAL_MEDIA = {
    "LinkedIn ": "https://www.linkedin.com/in/pedro-r-hernandez-416076134/",
    "GitHub": "https://github.com/RamsesPH"
}
PROJECTS = {
    "Watermark": "https://github.com/RamsesPH/Photo_watermark-",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
# st.title("I am in business")


st.markdown("""
<script src="https://kit.fontawesome.com/{KIT}.js" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)


# ---- LOAD CSS, PDF & PROFILE PIC ----

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- Hero Section -----

col1, col2 = st.columns(2, gap='small')

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📰  Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧 ", EMAIL)


# ---- SOCIAL LINKS -----------
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})({index})")

links = "  ".join([f'<a href="{link}" class="link">{platform}</a>' for platform, link in SOCIAL_MEDIA.items()])
st.markdown(links, unsafe_allow_html=True)

# icons = {
#     "LinkedIn": "fa-brands fa-linkedin",
#     "GitHub": "fa-brands fa-github",
# }
#
# links = " ".join([f'<a href="{link}"><i class="{icons[platform]}"></i> {platform}</a>' for platform, link in SOCIAL_MEDIA.items()])
#
# st.markdown(links, unsafe_allow_html=True)

# ----- EXPERIENCE  & QUALIFICATIONS ----------
st.write("#")
st.subheader("Experience & Qualification")
# the "-" will be recognized as an unordered list
st.write(
    """
    - ✅ 7 years  managing experience at Sony Corporation.
    - ✅ 15 experience as System Administrator. 
    - ✅ 5 years experience Data Centers installation and administration. 
    - ✅ 1 year experience Python Programming
    - ✅ Excellent team player and displaying strong sense of initiative on tasks
    """
)

# ---- SKILLS ---------
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 📚 Programing : Python, HTML, CSS, Bash, SQL
    - 📊 Data Visualization: Plotly, MS Excel
    - 🗄 DataBase: Postgres, SQLight
    - 💻 OS : RedHat, MacOS,  Ubuntu   
    """
)

# --------  WORK HISTORY ---------------
st.write("#")
st.subheader("Work History")
st.write("---")

# ---- JOB 1 -----
st.write("💻 IT Manager | Geolander Angola ")
st.write("09/2019 - Present")
st.write(
    """
    - > Data Processing Equipment Consultancy, Installation and configuration of Seismic Tape readers,
    - > Purchasing, configuration and Support  NAS servers and IT infrastructure. 
    - > Design and implementation of the Company Web Site.   
    """
)

# ---- JOB 2 -----
st.write("#")
st.write("💻 Senior System Administrator & Consultant | SCHLUMBERGER ( WesternGeco ) ")
st.write("05/2008 - 11/2014")
st.write(
    """
    - > Development & implementation of Disaster Recovery Procedures including 
        Security and Physical Audits.
    - > Deal with local & International Vendors. 
    - > Westerngeco end-user Technical Support. 
    - > Configuration & maintenance of the Company Backups.
    - > Normal Administrative System support. 
    - > Installation & Support to Seismic Media Readers For Angola State Company (Sonangol).
    - > Installation & Support of a HSM Data Center for GAD dept. at Sonangol. 
    - > Technical support for NDG company.  
    """
)

# ---- JOB 3 -----
st.write("#")
st.write("💻 System Specialist and Administrator | Western Atlas & Western Geophysical")
st.write("05/1997 - 05/2008")
st.write(
    """
    - > Installation, Maintenance and Support for Datacenters at
        Caracas, Colombia and Trinidad.
    - > Worked under AIX, IRIX, Solaris and Linux Environments as Junior Sys Admin. 
    - > Hardware Installation & repairs, Magnetic Readers, Disks & Servers.  
    """
)

# ---- JOB 4 -----
st.write("#")
st.write("💻 Production & Engineering Manager | TecnoCircuitos BR. ")
st.write("09/1987 - 04/1997")
st.write(
    """
    - > Coordination of Production & Quality Control Processes of PCB's.
    - > Installation & Maintenance of CNC machines. 
    - > Maintenance & repairs of various PCB production Machines.  
    """
)

# ---- JOB 5 -----
st.write("#")
st.write("📺 Junior Administration Manager | Sony Corporation Venezuela ")
st.write("09/1985 - 07/1987")
st.write(
    """
    - > Warehouse coordinator and Project manager.
    - > Inventory Coordination.   
    - > Liaison between the Production and Administration Dept.
    - > Personnel Manager.
    - > Project Management.
    """
)

# ---- JOB 6 -----
st.write("#")
st.write("📺 Chief of Audio and Engineering Dept. | Sony Corporation Venezuela ")
st.write("08/1981 - 08/1985")
st.write(
    """
    - > Audio Engineer and Production Assistant until Dec 1981.
    - > Coordination Speaker and Audio Equipment Production as Chief Audio.
    - > Project and Completion of Integration of Local parts to manufacturing process, 
        as Power cord, Plastic cabinets & Transformers.
    - > 
    """
)

#
# # --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")