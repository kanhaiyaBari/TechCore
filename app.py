import streamlit as st

st.set_page_config(
    page_title="TechCore | Smart Water Purification",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- GLOBAL STYLE ----------
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        max-width: 1300px;
    }

    body, .stApp {
        background: linear-gradient(180deg, #EAF3F8 0%, #F7FBFD 40%, #FFFFFF 100%);
    }

    /* Top nav bar */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 14px 6px 18px 6px;
        border-bottom: 1px solid #E3ECF0;
        margin-bottom: 24px;
    }
    .navbar-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .navbar-logo {
        width: 44px; height: 44px;
        background: #0A2E45;
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        color: #4FD1C5; font-weight: 700; font-size: 18px;
    }
    .navbar-title { font-size: 22px; font-weight: 800; color: #0A2E45; line-height: 1.1; }
    .navbar-sub { font-size: 11px; color: #7A8B92; letter-spacing: 0.5px; }
    .navbar-links { display: flex; gap: 26px; font-size: 15px; color: #37474F; font-weight: 500; }
    .navbar-links a { color: #37474F; text-decoration: none; }
    .navbar-links a:hover { color: #0F6E8C; }
    .navbar-tags { font-size: 13px; color: #6E8288; }

    /* Hero */
    .hero-eyebrow-line { width: 46px; height: 3px; background: #4FD1C5; margin: 10px 0 16px 0; }
    .hero-title { font-size: 40px; font-weight: 800; color: #0A2E45; line-height: 1.25; margin-bottom: 4px; }
    .hero-title-sub { font-size: 22px; font-weight: 600; color: #0F6E8C; margin-bottom: 14px; }
    .hero-desc { font-size: 15.5px; color: #4C5C61; line-height: 1.7; max-width: 480px; margin-bottom: 22px; }

    .feature-row { display: flex; gap: 26px; margin-top: 10px; }
    .feature-item { text-align: center; width: 90px; }
    .feature-icon {
        width: 52px; height: 52px; border-radius: 50%;
        border: 1.5px solid #B7D8E0; display: flex; align-items: center;
        justify-content: center; font-size: 22px; margin: 0 auto 8px auto;
        background: white;
    }
    .feature-label { font-size: 12.5px; color: #34474D; font-weight: 600; line-height: 1.3; }

    /* Water drop hero graphic */
    .drop-wrap { display: flex; justify-content: center; align-items: center; height: 100%; }
    .drop-shape {
        width: 260px; height: 320px;
        background: linear-gradient(160deg, #1E8FA8 0%, #0A5C74 60%, #073B4C 100%);
        border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
        clip-path: polygon(50% 0%, 100% 65%, 84% 90%, 50% 100%, 16% 90%, 0% 65%);
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 20px 40px rgba(10,92,116,0.25);
    }
    .drop-inner { color: white; font-size: 40px; font-weight: 800; opacity: 0.9; }

    /* Role card panel */
    .role-panel {
        background: white;
        border-radius: 16px;
        padding: 26px 28px;
        box-shadow: 0 10px 30px rgba(10,46,69,0.08);
        border: 1px solid #EDF3F5;
    }
    .role-panel-title { font-size: 21px; font-weight: 800; color: #0A2E45; margin-bottom: 2px; }
    .role-panel-sub { font-size: 13.5px; color: #7A8B92; margin-bottom: 18px; }

    .footer-strip {
        background: #0A2E45;
        margin-top: 50px;
        padding: 28px 30px;
        border-radius: 14px;
        display: flex;
        justify-content: space-between;
        color: #DCE9EC;
    }
    .footer-item { text-align: left; font-size: 13px; }
    .footer-item b { display: block; font-size: 14.5px; color: white; margin-bottom: 2px; }

    .stButton>button {
        width: 100%;
        text-align: left;
        border-radius: 10px;
        padding: 16px 18px;
        border: 1px solid #E3ECF0;
        font-weight: 600;
        font-size: 15px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- NAVBAR ----------
st.markdown("""
<div class="navbar">
    <div class="navbar-left">
        <div class="navbar-logo">TC</div>
        <div>
            <div class="navbar-title">TechCore</div>
            <div class="navbar-sub">INNOVATE &nbsp;·&nbsp; BUILD &nbsp;·&nbsp; IMPACT</div>
        </div>
    </div>
    <div class="navbar-links">
        <a href="#home">Home</a>
        <a href="#solution">Our Solution</a>
        <a href="#impact">Impact</a>
        <a href="#contact">Contact</a>
    </div>
    <div class="navbar-tags">Clean Water &nbsp;|&nbsp; Healthy People &nbsp;|&nbsp; Sustainable Future</div>
</div>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
col1, col2, col3 = st.columns([1.1, 0.8, 1.1], gap="large")

with col1:
    st.markdown('<div class="hero-eyebrow-line"></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Smart Water Purification and<br>Quality Monitoring System</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title-sub">for Rural and Mining-Affected Areas</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-desc">
        Using IoT + AI/ML to monitor water quality, detect risks, ensure safe
        purification, and build healthier communities in rural and mining-affected regions.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-row">
        <div class="feature-item"><div class="feature-icon">💧</div><div class="feature-label">Real-time<br>Monitoring</div></div>
        <div class="feature-item"><div class="feature-icon">🧠</div><div class="feature-label">AI/ML<br>Analysis</div></div>
        <div class="feature-item"><div class="feature-icon">🛡</div><div class="feature-label">Safe Water<br>Purification</div></div>
        <div class="feature-item"><div class="feature-icon">👨👩👧</div><div class="feature-label">Healthier<br>Communities</div></div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="drop-wrap">
        <div class="drop-shape"><div class="drop-inner">AI</div></div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Replace with your custom drop/plant illustration in assets/logo.png for the final version.")

with col3:
    st.markdown('<div class="role-panel">', unsafe_allow_html=True)
    st.markdown('<div class="role-panel-title">👤 Select Your Role</div>', unsafe_allow_html=True)
    st.markdown('<div class="role-panel-sub">Live demo — select a role below to explore</div>', unsafe_allow_html=True)

    if st.button("🟢  Community Member\nCheck water quality, view status and report issues.", key="community"):
        st.switch_page("pages/1_Community.py")

    if st.button("🔵  Health Worker / Caretaker\nMonitor parameters, respond to alerts, manage treatment.", key="caretaker"):
        st.switch_page("pages/2_Caretaker.py")

    if st.button("🟣  Government Authority\nView area-wise data, track alerts, generate reports.", key="government"):
        st.switch_page("pages/3_Government.py")

    st.markdown("---")
    st.markdown("🛡 **Secure & Trusted Monitoring Platform**")
    st.caption("Prototype access — click any role above, no login required for this demo.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- BOTTOM FEATURE STRIP ----------
st.markdown("""
<div class="footer-strip">
    <div class="footer-item"><b>📡 IoT Sensors</b>Track water quality in real time</div>
    <div class="footer-item"><b>🧠 AI/ML Intelligence</b>Detect risks & anomalies</div>
    <div class="footer-item"><b>☁ Cloud Platform</b>Store, analyze & visualize data</div>
    <div class="footer-item"><b>☀ Solar + GSM / LoRa</b>Works even in low-connectivity areas</div>
    <div class="footer-item"><b>🛡 Cleaner Water</b>Healthier Communities</div>
</div>
""", unsafe_allow_html=True)
