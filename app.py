import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Isaac Kuria | CV",
    page_icon="logo2.png",
    layout="wide"
)

# --- HEADER ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Isaac Kuria")
    st.subheader("Data Analyst | ICT Support Specialist | MSc Data Science")
    st.write("📧 i.kuria@hotmail.com")
    st.write("📱 +44 7349 688 208")
    st.write("🔗 [linkedin.com/in/kuriaspace](https://www.linkedin.com/in/kuriaspace/)")

with col2:
    st.metric("Experience", "9+ Years")
    st.metric("Degree", "BSc First Class")
    st.metric("Current", "MSc Data Science")

st.divider()

# --- PROFILE ---
st.header("👤 Profile")
st.write("""
Data Analyst, Computer Vision Enthusiast & ICT Support Specialist, 
currently completing an MSc Data Science dissertation at Robert Gordon University. 
Experienced in supporting safety-critical aviation systems and applying data-driven 
approaches to solve real-world problems.
""")

import plotly.graph_objects as go

# --- SKILLS ---
st.header("🛠️ Technical Skills")

col1, col2 = st.columns([1, 1])

with col1:
    skills = {
        "Python": 85,
        "SQL": 80,
        "Data Pipelines / ETL": 75,
        "Machine Learning": 70,
        "Big Data (Hadoop/Spark)": 65,
        "Computer Vision": 60,
        "MySQL / Relational DBs": 75,
        "IT Support / Networking": 90,
    }

    fig = go.Figure(go.Bar(
        x=list(skills.values()),
        y=list(skills.keys()),
        orientation='h',
        marker=dict(color='#1f77b4')
    ))

    fig.update_layout(
        xaxis=dict(range=[0, 100], title="Proficiency (%)"),
        height=400,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Core Competencies")
    st.write("✅ Data Analysis & EDA")
    st.write("✅ ETL & Data Engineering")
    st.write("✅ Incident Management")
    st.write("✅ IT Systems Support")
    st.write("✅ Data Warehousing")
    st.write("✅ OLAP & Relational Modelling")
    st.write("✅ Big Data Technologies")
    st.write("✅ Computer Vision")

st.divider()

# --- EXPERIENCE ---
st.header("💼 Work Experience")

def experience_card(title, company, period, bullets):
    st.subheader(f"{title}")
    st.caption(f"🏢 {company}  |  📅 {period}")
    for bullet in bullets:
        st.write(f"• {bullet}")
    st.write("")

experience_card(
    "IT Support Assistant",
    "[East African School of Aviation (KCAA)](https://easa.ac.ke/)",
    "Jan 2025 – Aug 2025",
    [
        "Supported enterprise IT systems across classrooms, labs, and administrative offices",
        "Assisted with system configuration, backups, updates, and data integrity checks",
        "Troubleshot infrastructure and application issues supporting operational continuity",
    ]
)

experience_card(
    "Technical Support Specialist",
    "[Kenya Civil Aviation Authority (KCAA)](https://www.kcaa.or.ke/)",
    "Feb 2015 – Dec 2024",
    [
        "Provided technical support for systems across multiple departments",
        "Supported databases, applications, and networked systems in regulated environments",
        "Assisted with system upgrades, data backups, and ICT security compliance",
        "Collaborated with cross-functional teams to resolve incidents and improve reliability",
    ]
)

experience_card(
    "Freelance IT Support Consultant",
    "Self-Employed",
    "Jan 2017 – Oct 2024",
    [
        "Delivered remote and onsite IT support for individual and business clients",
        "Installed, configured, and maintained computer systems, databases, and networks",
        "Diagnosed and resolved technical issues, reducing downtime and improving stability",
    ]
)

st.divider()

################

# --- EDUCATION ---
st.header("🎓 Education")

col1, col2 = st.columns(2)

with col1:
    st.subheader("MSc Data Science")
    st.caption("📍 [Robert Gordon University](https://www.rgu.ac.uk/) |  📅 2025 – Present")
    st.write("Currently at dissertation stage, focusing on machine learning and computer vision.")

    st.write("")

    st.subheader("BSc (Hons) Computer Science")
    st.caption("📍 St Paul's University, Kenya  |  📅 2019 – 2022")
    st.write("First Class Honours")

with col2:
    st.subheader("Diploma in Computer Studies")
    st.caption("📍 Kenya National Youth Service Engineering Institute  |  📅 2012 – 2014")
    st.write("Foundation in computer systems and engineering principles.")

st.divider()

# --- VOLUNTEER ---
st.header("🤝 Volunteer Experience")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sustainability Retail Assistant")
    st.caption("📍 GoGreen KEIM Shop, RGU  |  📅 Sep 2025 – Present")
    st.write("Tracked inventory and sales data to support stock decisions and reporting.")

with col2:
    st.subheader("Community Engagement Support Assistant")
    st.caption("📍 Re-engage Volunteering  |  📅 Sep 2025 – Present")
    st.write("Monitored participation data and feedback to support service improvement initiatives.")

st.divider()
#####
# --- CHATBOT ---
st.header("🤖 Ask About My CV")
st.write("Ask me anything about my experience, skills, or background!")

def cv_chatbot(question):
    q = question.lower()

    if any(w in q for w in ["skill", "know", "technology", "tech", "tools"]):
        return "Isaac is skilled in Python, SQL, ETL, data pipelines, MySQL, Hadoop, Spark, machine learning, and computer vision. He also has 9+ years of IT support and networking experience."

    elif any(w in q for w in ["experience", "work", "job", "career"]):
        return "Isaac has 9+ years of experience. He worked as a Technical Support Specialist at Kenya Civil Aviation Authority (2015–2024), IT Support Assistant at East African School of Aviation (2025), and as a Freelance IT Consultant (2017–2024)."

    elif any(w in q for w in ["education", "degree", "study", "university", "qualification","background"]):
        return "Isaac holds a BSc (Hons) Computer Science with First Class Honours from St Paul's University, Kenya. He is currently completing an MSc Data Science dissertation at Robert Gordon University, Aberdeen."

    elif any(w in q for w in ["aviation", "kcaa", "airline"]):
        return "Isaac spent nearly a decade supporting IT systems at the Kenya Civil Aviation Authority — a safety-critical, regulated environment. This gives him unique insight into aviation technology operations."

    elif any(w in q for w in ["data science", "machine learning", "ml", "ai", "computer vision"]):
        return "Isaac is currently pursuing an MSc in Data Science at Robert Gordon University, with a focus on machine learning and computer vision techniques for real-world problem solving."

    elif any(w in q for w in ["contact", "email", "phone", "reach", "hire"]):
        return "You can reach Isaac at i.kuria@hotmail.com or +44 7349 688 208. Connect on LinkedIn at linkedin.com/in/kuriaspace/"

    elif any(w in q for w in ["location", "based", "where", "country", "live"]):
        return "Isaac is currently based in Aberdeen, Scotland, UK, and is open to relocation for the right opportunity."

    elif any(w in q for w in ["volunteer", "community"]):
        return "Isaac volunteers as a Sustainability Retail Assistant at GoGreen KEIM Shop (RGU) and as a Community Engagement Support Assistant at Re-engage Volunteering, both since September 2025."

    elif any(w in q for w in ["python", "sql", "hadoop", "spark", "mysql"]):
        return "Yes! Isaac works with Python and SQL for data analysis and ETL, MySQL for relational databases, and Hadoop and Spark for big data processing."

    elif any(w in q for w in ["strength", "best", "good at", "speciality", "specialist"]):
        return "Isaac's key strengths are bridging IT support with data science, working in regulated environments, and turning data into actionable insights. His aviation background is a rare differentiator."

    else:
        return "Great question! For more details you can reach Isaac directly at i.kuria@hotmail.com or connect on LinkedIn at linkedin.com/in/kuriaspace/"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me something... e.g. 'What are your skills?'")

if user_input:
    response = cv_chatbot(user_input)
    st.session_state.chat_history.append(("you", user_input))
    st.session_state.chat_history.append(("isaac", response))

for sender, message in st.session_state.chat_history:
    if sender == "you":
        with st.chat_message("user"):
            st.write(message)
    else:
        with st.chat_message("assistant"):
            st.write(message)

st.divider()

# --- FOOTER ---
st.caption("Built with Python & Streamlit  |  Isaac Kuria © 2026")