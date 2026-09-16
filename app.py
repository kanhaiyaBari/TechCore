import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AquaGuard | TechCore",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background: #f5f9fc;
        color: #12365a;
    }

    .block-container {
        padding-top: 0.5rem;
        padding-left: 4rem;
        padding-right: 4rem;
        max-width: 1500px;
    }

    /* Hide Streamlit default UI */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* ---------- NAVBAR ---------- */

    .navbar {
        height: 82px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid #dce8f1;
        margin-bottom: 25px;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-icon {
        width: 48px;
        height: 48px;
        border-radius: 13px;
        background: linear-gradient(145deg, #063b68, #087fa6);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 25px;
        box-shadow: 0 6px 18px rgba(0, 80, 130, 0.18);
    }

    .brand-name {
        font-size: 27px;
        font-weight: 800;
        color: #07365d;
        line-height: 1;
    }

    .brand-tag {
        font-size: 12px;
        color: #52718c;
        margin-top: 5px;
        letter-spacing: 1px;
    }

    .nav-links {
        display: flex;
        gap: 34px;
        color: #204c70;
        font-size: 15px;
        font-weight: 600;
    }

    .nav-right {
        color: #52718c;
        font-size: 14px;
    }


    /* ---------- HERO ---------- */

    .hero {
        min-height: 590px;
        border-radius: 28px;
        padding: 55px 55px;
        background:
            linear-gradient(
                90deg,
                rgba(248,252,255,0.98) 0%,
                rgba(248,252,255,0.94) 45%,
                rgba(248,252,255,0.35) 100%
            );
        position: relative;
        overflow: hidden;
        border: 1px solid #dbe9f3;
    }

    .hero::after {
        content: "";
        position: absolute;
        right: -120px;
        bottom: -170px;
        width: 570px;
        height: 570px;
        background: #d9f4f5;
        border-radius: 50%;
        opacity: 0.55;
        z-index: 0;
    }

    .hero-content {
        position: relative;
        z-index: 2;
    }

    .water-logo {
        font-size: 45px;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 43px;
        line-height: 1.12;
        font-weight: 800;
        color: #07365d;
        max-width: 650px;
        margin: 0;
    }

    .hero-title span {
        color: #087fa6;
    }

    .hero-subtitle {
        font-size: 22px;
        color: #17618c;
        margin-top: 15px;
        max-width: 650px;
    }

    .hero-description {
        font-size: 16px;
        line-height: 1.7;
        color: #47677f;
        max-width: 620px;
        margin-top: 20px;
    }

    .line {
        width: 58px;
        height: 4px;
        background: #11a6a0;
        border-radius: 4px;
        margin: 20px 0;
    }


    /* ---------- FEATURE ICONS ---------- */

    .features {
        display: flex;
        gap: 42px;
        margin-top: 32px;
    }

    .feature {
        text-align: center;
        width: 100px;
    }

    .feature-icon {
        width: 55px;
        height: 55px;
        margin: auto;
        border: 2px solid #2997d2;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 25px;
        background: white;
    }

    .feature-text {
        font-size: 13px;
        font-weight: 700;
        color: #173f61;
        margin-top: 8px;
    }


    /* ---------- ROLE PANEL ---------- */

    .role-panel {
        background: rgba(255,255,255,0.96);
        border: 1px solid #d6e5ef;
        border-radius: 24px;
        padding: 32px;
        box-shadow: 0 15px 40px rgba(17, 65, 95, 0.12);
        height: 100%;
    }

    .role-title {
        font-size: 28px;
        font-weight: 800;
        color: #07365d;
    }

    .role-subtitle {
        font-size: 15px;
        color: #58748a;
        margin-bottom: 24px;
    }


    /* ---------- ROLE CARDS ---------- */

    .role-card {
        border-radius: 15px;
        padding: 17px 18px;
        margin-bottom: 14px;
        border: 1px solid #cfe0eb;
        background: #fafdff;
        transition: 0.2s;
    }

    .role-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(20,80,120,0.10);
    }

    .role-card-title {
        font-size: 17px;
        font-weight: 800;
        color: #07365d;
    }

    .role-card-text {
        font-size: 13px;
        color: #55738a;
        margin-top: 5px;
    }

    /* Streamlit buttons */

    div.stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 12px;
        border: 1px solid #c9dce8;
        background: white;
        color: #07365d;
        font-weight: 700;
        font-size: 15px;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        border-color: #1594bd;
        color: #087fa6;
        background: #f1fbfd;
    }


    /* ---------- TRUST ---------- */

    .trust {
        text-align: center;
        border-top: 1px solid #dce8f1;
        margin-top: 22px;
        padding-top: 18px;
        color: #496b82;
        font-size: 13px;
    }


    /* ---------- BOTTOM STRIP ---------- */

    .bottom-strip {
        margin-top: 25px;
        background: #06365d;
        border-radius: 24px 24px 0 0;
        padding: 24px 30px;
        color: white;
    }

    .tech-item {
        text-align: center;
    }

    .tech-icon {
        font-size: 25px;
    }

    .tech-title {
        font-weight: 700;
        font-size: 14px;
        margin-top: 6px;
    }

    .tech-text {
        font-size: 11px;
        color: #bcd8e8;
        margin-top: 3px;
    }


    /* ---------- MOBILE ---------- */

    @media (max-width: 900px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .navbar {
            height: auto;
            padding: 15px 0;
        }

        .nav-links,
        .nav-right {
            display: none;
        }

        .hero {
            padding: 30px 20px;
        }

        .hero-title {
            font-size: 30px;
        }

        .hero-subtitle {
            font-size: 18px;
        }

        .features {
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .role-panel {
            margin-top: 25px;
        }
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVBAR
# =========================================================

st.markdown("""
<div class="navbar">

    <div class="brand">
        <div class="brand-icon">⚙️</div>

        <div>
            <div class="brand-name">TechCore</div>
            <div class="brand-tag">INNOVATE • BUILD • IMPACT</div>
        </div>
    </div>

    <div class="nav-links">
        <span>Home</span>
        <span>About</span>
        <span>Our Solution</span>
        <span>Impact</span>
        <span>Contact</span>
    </div>

    <div class="nav-right">
        Clean Water &nbsp; | &nbsp; Healthy Communities
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO + ROLE SELECTION
# =========================================================

left, right = st.columns([1.15, 0.85], gap="large")


# =========================================================
# LEFT SIDE
# =========================================================

with left:

    st.markdown("""
    <div class="hero">

        <div class="hero-content">

            <div class="water-logo">💧</div>

            <h1 class="hero-title">
                Smart Water Purification and
                <span>Quality Monitoring System</span>
            </h1>

            <div class="hero-subtitle">
                for Rural and Mining-Affected Areas
            </div>

            <div class="line"></div>

            <div class="hero-description">
                Using IoT + AI/ML to monitor water quality,
                identify abnormal conditions, support safe
                purification and provide actionable alerts
                for rural and mining-affected communities.
            </div>

            <div class="features">

                <div class="feature">
                    <div class="feature-icon">💧</div>
                    <div class="feature-text">
                        Real-time<br>Monitoring
                    </div>
                </div>

                <div class="feature">
                    <div class="feature-icon">🧠</div>
                    <div class="feature-text">
                        AI/ML<br>Analysis
                    </div>
                </div>

                <div class="feature">
                    <div class="feature-icon">🛡️</div>
                    <div class="feature-text">
                        Safe Water<br>Purification
                    </div>
                </div>

                <div class="feature">
                    <div class="feature-icon">👥</div>
                    <div class="feature-text">
                        Community<br>Safety
                    </div>
                </div>

            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# RIGHT SIDE
# =========================================================

with right:

    st.markdown("""
    <div class="role-panel">

        <div class="role-title">
            👥 Select Your Role
        </div>

        <div class="role-subtitle">
            Choose how you want to access the AquaGuard system
        </div>

    </div>
    """, unsafe_allow_html=True)

    # Community
    if st.button("👥  Community Member\nCheck water quality and report issues",
                 key="community"):

        st.session_state.page = "community"
        st.rerun()

    # Health Worker
    if st.button("🩺  Health Worker / Caretaker\nMonitor water quality and respond to alerts",
                 key="health"):

        st.session_state.page = "health"
        st.rerun()

    # Government
    if st.button("🏛️  Government Authority\nMonitor locations, alerts and analytics",
                 key="government"):

        st.session_state.page = "government"
        st.rerun()


    st.markdown("""
    <div class="trust">
        🛡️ <b>AquaGuard Monitoring Platform</b><br>
        Prototype Access — No login required
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# BOTTOM TECHNOLOGY STRIP
# =========================================================

st.markdown("""
<div class="bottom-strip">

<div class="tech-item">

    <div class="tech-icon">📡</div>
    <div class="tech-title">IoT Sensors</div>
    <div class="tech-text">
        Continuous water-quality monitoring
    </div>

</div>

<div class="tech-item">

    <div class="tech-icon">🧠</div>
    <div class="tech-title">AI / ML</div>
    <div class="tech-text">
        Risk and water-quality analysis
    </div>

</div>

<div class="tech-item">

    <div class="tech-icon">☁️</div>
    <div class="tech-title">Cloud Platform</div>
    <div class="tech-text">
        Store and visualize monitoring data
    </div>

</div>

<div class="tech-item">

    <div class="tech-icon">☀️</div>
    <div class="tech-title">Solar + GSM / LoRa</div>
    <div class="tech-text">
        Designed for remote areas
    </div>

</div>

<div class="tech-item">

    <div class="tech-icon">🛡️</div>
    <div class="tech-title">Water Safety</div>
    <div class="tech-text">
        Detect • Decide • Act
    </div>

</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# DEMO PAGE ROUTING
# =========================================================

if st.session_state.page != "home":

    st.markdown("---")

    role = st.session_state.page

    if role == "community":
        st.success("Community Member Dashboard")
        st.write("This will open the Community Dashboard.")

    elif role == "health":
        st.info("Health Worker / Caretaker Dashboard")
        st.write("This will open the Caretaker Dashboard.")

    elif role == "government":
        st.warning("Government Authority Dashboard")
        st.write("This will open the Government Dashboard.")

    if st.button("← Back to Role Selection"):
        st.session_state.page = "home"
        st.rerun()
