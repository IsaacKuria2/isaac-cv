import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Isaac Kuria | CV",
    page_icon="logo2.png",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

  /* ── Global Reset ─────────────────────────────────────── */
  html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #eaeaea;
  }

  /* ── Page Background ──────────────────────────────────── */
  .stApp {
    background: linear-gradient(135deg, #f0f4ff 0%, #fafbff 50%, #f5f0ff 100%);
    background-attachment: fixed;
  }

  /* ── Hero Banner ──────────────────────────────────────── */
  .hero-banner {
    background: linear-gradient(135deg, #0f1e6b 0%, #1a3a8f 40%, #2563eb 100%);
    border-radius: 20px;
    padding: 48px 52px;
    margin-bottom: 8px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(15, 30, 107, 0.3);
  }
  .hero-banner::before {
    content: "";
    position: absolute;
    top: -80px; right: -80px;
    width: 320px; height: 320px;
    background: radial-gradient(circle, rgba(255,255,255,0.07) 0%, transparent 70%);
    border-radius: 50%;
  }
  .hero-banner::after {
    content: "✈";
    position: absolute;
    bottom: -10px; right: 40px;
    font-size: 130px;
    opacity: 0.07;
    line-height: 1;
  }
  .hero-name {
    font-family: 'DM Serif Display', serif;
    font-size: 3.4rem;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 6px;
  }
  .hero-title {
    font-size: 1.05rem;
    font-weight: 400;
    color: rgba(255,255,255,0.8);
    letter-spacing: 0.04em;
    margin-bottom: 20px;
  }
  .hero-contacts {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 18px;
  }
  .hero-contact-pill {
    background: rgba(255,255,255,0.13);
    border: 1px solid rgba(255,255,255,0.22);
    border-radius: 30px;
    padding: 6px 16px;
    color: #fff;
    font-size: 0.82rem;
    font-weight: 500;
    text-decoration: none;
    backdrop-filter: blur(4px);
  }
  .hero-contact-pill:hover { background: rgba(255,255,255,0.22); }

  /* ── Metric Chips ─────────────────────────────────────── */
  .metric-row {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-top: 20px;
  }
  .metric-chip {
    background: #fff;
    border-radius: 14px;
    padding: 16px 22px;
    flex: 1;
    min-width: 130px;
    box-shadow: 0 2px 12px rgba(15, 30, 107, 0.09);
    border-top: 3px solid #2563eb;
    text-align: center;
  }
  .metric-chip .val {
    font-family: 'DM Serif Display', serif;
    font-size: 1.55rem;
    color: #0f1e6b;
  }
  .metric-chip .lbl {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #6b7280;
    margin-top: 2px;
  }

  /* ── Section Headers ──────────────────────────────────── */
  .section-header {
    font-family: 'DM Serif Display', serif;
    font-size: 1.75rem;
    color: #0f1e6b;
    margin-bottom: 4px;
    padding-bottom: 10px;
    border-bottom: 2px solid #e0e7ff;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  /* ── Cards ────────────────────────────────────────────── */
  .card {
    background: #fff;
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 16px;
    box-shadow: 0 2px 16px rgba(15, 30, 107, 0.07);
    border-left: 4px solid #2563eb;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 28px rgba(15, 30, 107, 0.13);
  }
  .card-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.2rem;
    color: #0f1e6b;
    margin-bottom: 2px;
  }
  .card-meta {
    font-size: 0.8rem;
    color: #6b7280;
    font-weight: 500;
    margin-bottom: 12px;
  }
  .card-meta a { color: #2563eb; text-decoration: none; }
  .card ul { padding-left: 18px; margin: 0; }
  .card li { margin-bottom: 5px; font-size: 0.92rem; color: #374151; }

  /* ── Skill Tags ───────────────────────────────────────── */
  .skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 8px;
  }
  .skill-tag {
    background: linear-gradient(135deg, #eff6ff, #e0e7ff);
    color: #1e40af;
    border: 1px solid #bfdbfe;
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 0.8rem;
    font-weight: 600;
  }

  /* ── Profile Block ────────────────────────────────────── */
  .profile-box {
    background: linear-gradient(135deg, #eff6ff 0%, #f5f3ff 100%);
    border-radius: 16px;
    padding: 24px 28px;
    border: 1px solid #e0e7ff;
    font-size: 0.97rem;
    line-height: 1.7;
    color: #374151;
  }

  /* ── Chat Window ──────────────────────────────────────── */
  .chat-intro {
    background: linear-gradient(135deg, #0f1e6b, #2563eb);
    color: #fff;
    border-radius: 14px;
    padding: 18px 24px;
    margin-bottom: 16px;
    font-size: 0.93rem;
  }

  /* ── Road Damage Section ──────────────────────────────── */
  .damage-class-card {
    background: #fff;
    border-radius: 12px;
    padding: 16px 20px;
    box-shadow: 0 2px 10px rgba(15,30,107,0.07);
  }
  .damage-class-card li { margin-bottom: 7px; font-size: 0.88rem; }

  /* ── Footer ───────────────────────────────────────────── */
  .footer {
    text-align: center;
    padding: 24px;
    font-size: 0.8rem;
    color: #9ca3af;
    letter-spacing: 0.03em;
  }

  /* ── Streamlit overrides ──────────────────────────────── */
  .stMetric { display: none !important; }   /* hide default metrics, we replace them */
  div[data-testid="stMetricValue"] { font-family: 'DM Serif Display', serif; color: #0f1e6b; }
  .stDivider { border-color: #e0e7ff !important; }
  [data-testid="stFileUploader"] { border: 2px dashed #bfdbfe; border-radius: 12px; padding: 12px; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-banner">
  <div class="hero-name">Isaac Kuria</div>
  <div class="hero-title">Data Analyst &nbsp;·&nbsp; ICT Support Specialist &nbsp;·&nbsp; MSc Data Science Candidate</div>
  <div class="hero-contacts">
    <a class="hero-contact-pill" href="mailto:i.kuria@hotmail.com">✉ i.kuria@hotmail.com</a>
    <a class="hero-contact-pill" href="https://www.linkedin.com/in/kuriaspace/" target="_blank">🔗 linkedin.com/in/kuriaspace</a>
    <span class="hero-contact-pill">📍 Aberdeen, Scotland, UK</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="metric-row">
  <div class="metric-chip"><div class="val">9+</div><div class="lbl">Years Experience</div></div>
  <div class="metric-chip"><div class="val">1st</div><div class="lbl">Class Honours BSc</div></div>
  <div class="metric-chip"><div class="val">MSc</div><div class="lbl">Data Science (RGU)</div></div>
  <div class="metric-chip"><div class="val">✈</div><div class="lbl">Aviation Domain</div></div>
</div>
""", unsafe_allow_html=True)

st.write("")

# ══════════════════════════════════════════════════════════
# PROFILE
# ══════════════════════════════════════════════════════════
st.markdown('<div class="section-header">👤 Profile</div>', unsafe_allow_html=True)
st.markdown("""
<div class="profile-box">
Data Analyst, Computer Vision Enthusiast &amp; ICT Support Specialist,
currently completing an MSc Data Science dissertation at Robert Gordon University.
Experienced in supporting safety-critical aviation systems and applying data-driven
approaches to solve real-world problems. Unique combination of deep technical
support expertise and emerging data science capability, with a rare background in
regulated aviation environments.
</div>
""", unsafe_allow_html=True)

st.write("")

# ══════════════════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════════════════
st.markdown('<div class="section-header">🛠️ Technical Skills</div>', unsafe_allow_html=True)
st.write("")

import plotly.graph_objects as go

col1, col2 = st.columns([3, 2], gap="large")

with col1:
    skills = {
        "IT Support": 90,
        "Python": 85,
        "SQL": 80,
        "Data Pipelines / ETL": 75,
        "MySQL / databases": 75,
        "Machine Learning": 70,
        "Big Data Analytics": 65,
        "Computer Vision": 60,
    }

    colors = ["#1e40af" if v >= 80 else "#2563eb" if v >= 70 else "#3b82f6" if v >= 60 else "#93c5fd"
              for v in skills.values()]

    fig = go.Figure(go.Bar(
        x=list(skills.values()),
        y=list(skills.keys()),
        orientation='h',
        marker=dict(
            color=colors,
            line=dict(width=0)
        ),
        text=[f"{v}%" for v in skills.values()],
        textposition='outside',
        textfont=dict(size=12, color="#374151", family="DM Sans"),
    ))

    fig.update_layout(
        xaxis=dict(range=[0, 108], showgrid=False, zeroline=False, visible=False),
        yaxis=dict(tickfont=dict(size=13, family="DM Sans", color="#374151")),
        height=340,
        margin=dict(l=0, r=40, t=10, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        bargap=0.35,
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("""
    <div style="background:#fff; border-radius:16px; padding:22px 24px;
                box-shadow:0 2px 16px rgba(15,30,107,0.07); height:100%;">
      <div style="font-family:'DM Serif Display',serif; font-size:1.1rem; color:#0f1e6b; margin-bottom:14px;">
        Core Competencies
      </div>
      <div class="skill-tags">
        <span class="skill-tag">Data Analysis &amp; EDA</span>
        <span class="skill-tag">ETL &amp; Data Engineering</span>
        <span class="skill-tag">Incident Management</span>
        <span class="skill-tag">IT Systems Support</span>
        <span class="skill-tag">Data Warehousing</span>
        <span class="skill-tag">OLAP &amp; Relational Modelling</span>
        <span class="skill-tag">Big Data Technologies</span>
        <span class="skill-tag">Computer Vision</span>
        <span class="skill-tag">YOLOv8 Object Detection</span>
        <span class="skill-tag">ICT Security Compliance</span>
        <span class="skill-tag">Cross-Functional Collaboration</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ══════════════════════════════════════════════════════════
# EXPERIENCE
# ══════════════════════════════════════════════════════════
st.markdown('<div class="section-header">💼 Work Experience</div>', unsafe_allow_html=True)
st.write("")

experiences = [
    {
        "title": "IT Support Assistant",
        "company": "East African School of Aviation (KCAA)",
        "url": "https://easa.ac.ke/",
        "period": "Jan 2025 – Aug 2025",
        "bullets": [
            "Supported enterprise IT systems across classrooms, labs, and administrative offices",
            "Assisted with system configuration, backups, updates, and data integrity checks",
            "Troubleshot infrastructure and application issues supporting operational continuity",
        ]
    },
    {
        "title": "Technical Support Specialist",
        "company": "Kenya Civil Aviation Authority (KCAA)",
        "url": "https://www.kcaa.or.ke/",
        "period": "Feb 2015 – Dec 2024",
        "bullets": [
            "Provided technical support for systems across multiple departments in a safety-critical regulated environment",
            "Supported databases, applications, and networked systems ensuring operational continuity",
            "Assisted with system upgrades, data backups, and ICT security compliance",
            "Collaborated with cross-functional teams to resolve incidents and improve reliability",
        ]
    },
    {
        "title": "Freelance IT Support Consultant",
        "company": "Self-Employed",
        "url": None,
        "period": "Jan 2017 – Oct 2024",
        "bullets": [
            "Delivered remote and onsite IT support for individual and business clients",
            "Installed, configured, and maintained computer systems, databases, and networks",
            "Diagnosed and resolved technical issues, reducing downtime and improving stability",
        ]
    },
]

for exp in experiences:
    company_html = (f'<a href="{exp["url"]}" target="_blank">{exp["company"]}</a>'
                    if exp["url"] else exp["company"])
    bullets_html = "".join(f"<li>{b}</li>" for b in exp["bullets"])
    st.markdown(f"""
    <div class="card">
      <div class="card-title">{exp["title"]}</div>
      <div class="card-meta">🏢 {company_html} &nbsp;|&nbsp; 📅 {exp["period"]}</div>
      <ul>{bullets_html}</ul>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ══════════════════════════════════════════════════════════
# EDUCATION
# ══════════════════════════════════════════════════════════
st.markdown('<div class="section-header">🎓 Education</div>', unsafe_allow_html=True)
st.write("")

edu_col1, edu_col2, edu_col3 = st.columns(3, gap="medium")

with edu_col1:
    st.markdown("""
    <div class="card" style="border-left-color:#7c3aed; height:100%;">
      <div class="card-title">MSc Data Science</div>
      <div class="card-meta">📍 <a href="https://www.rgu.ac.uk/" target="_blank">Robert Gordon University</a> &nbsp;|&nbsp; 📅 2025 – Present</div>
      <p style="font-size:0.9rem;color:#374151;margin:0;">
        Currently at dissertation stage, focusing on machine learning and computer vision for road damage detection using YOLOv8.
      </p>
    </div>
    """, unsafe_allow_html=True)

with edu_col2:
    st.markdown("""
    <div class="card" style="border-left-color:#059669; height:100%;">
      <div class="card-title">BSc (Hons) Computer Science</div>
      <div class="card-meta">📍 <a href="https://www.spu.ac.ke/" target="_blank">St Paul's University, Kenya </a>&nbsp;|&nbsp; 📅 2019 – 2022</div>
      <p style="font-size:0.9rem;color:#374151;margin:0;">
        <strong style="color:#059669;">First Class Honours</strong> — top distinction awarded for academic excellence.
      </p>
    </div>
    """, unsafe_allow_html=True)

with edu_col3:
    st.markdown("""
    <div class="card" style="border-left-color:#d97706; height:100%;">
      <div class="card-title">Diploma in Computer Studies</div>
      <div class="card-meta">📍 Kenya National Youth Service Engineering Institute &nbsp;|&nbsp; 📅 2012 – 2014</div>
      <p style="font-size:0.9rem;color:#374151;margin:0;">
        Foundation in computer systems and engineering principles.
      </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ══════════════════════════════════════════════════════════
# VOLUNTEER
# ══════════════════════════════════════════════════════════
st.markdown('<div class="section-header">🤝 Volunteer Experience</div>', unsafe_allow_html=True)
st.write("")

vol_col1, vol_col2 = st.columns(2, gap="medium")

with vol_col1:
    st.markdown("""
    <div class="card" style="border-left-color:#10b981;">
      <div class="card-title">Sustainability Retail Assistant</div>
      <div class="card-meta">📍 GoGreen KEIM Shop, RGU &nbsp;|&nbsp; 📅 Sep 2025 – Present</div>
      <p style="font-size:0.9rem;color:#374151;margin:0;">
        Tracked inventory and sales data to support stock decisions and sustainability reporting.
      </p>
    </div>
    """, unsafe_allow_html=True)

with vol_col2:
    st.markdown("""
    <div class="card" style="border-left-color:#f59e0b;">
      <div class="card-title">Community Engagement Support Assistant</div>
      <div class="card-meta">📍 Re-engage Volunteering &nbsp;|&nbsp; 📅 Sep 2025 – Present</div>
      <p style="font-size:0.9rem;color:#374151;margin:0;">
        Monitor participation data and feedback to support service improvement initiatives.
      </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
# ══════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════
st.write("")
st.markdown("""
<div class="footer">
  &nbsp;&nbsp; Isaac Kuria © 2026 &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/kuriaspace/" style="color:#2563eb; text-decoration:none;">LinkedIn</a>
</div>
""", unsafe_allow_html=True)