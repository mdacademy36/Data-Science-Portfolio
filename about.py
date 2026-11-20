
import streamlit as st
from pathlib import Path
import base64


def app():

    # ====================================
    # LOAD PROFILE IMAGE
    # ====================================

    image_path = Path(__file__).parent / "assets" / "maulana.png"

    if image_path.exists():
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(
                image_file.read()
            ).decode()

        profile_image = f"data:image/png;base64,{encoded_image}"
    else:
        profile_image = ""


    # ====================================
    # CUSTOM CSS
    # ====================================

    st.markdown("""
    <style>

    .about-label {
        color: #F59E0B;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 3px;
        margin-bottom: 20px;
    }

    .about-title {
        color: #475569;
        font-size: 38px;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 15px;
    }

    .about-subtitle {
        color: #94A3B8;
        font-size: 17px;
        margin-bottom: 28px;
    }

    .about-text {
        color: #475569;
        font-size: 16px;
        line-height: 1.8;
        margin-bottom: 16px;
    }

    .section-title {
        color: #16474B;
        font-size: 27px;
        font-weight: 700;
        margin-top: 28px;
        margin-bottom: 18px;
    }

    .skills-text {
        color: #475569;
        font-size: 16px;
        font-weight: 600;
        line-height: 2;
    }

    .profile-image {
        width: 250px;
        height: 250px;
        object-fit: cover;
        border-radius: 50%;
        border: 4px solid #F59E0B;
    }

    .profile-name {
        color: #16474B;
        font-size: 28px;
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
    }

    .profile-role {
        color: #94A3B8;
        font-size: 15px;
        text-align: center;
        margin-top: 8px;
    }

    .profile-location {
        color: #475569;
        font-size: 14px;
        text-align: center;
        margin-top: 12px;
    }

    .project-title {
        color: #16474B;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .project-text {
        color: #475569;
        font-size: 15px;
        line-height: 1.8;
    }

    </style>
    """, unsafe_allow_html=True)


    # ====================================
    # TWO COLUMN LAYOUT
    # ====================================

    col1, col2 = st.columns([2.2, 1], gap="large")


    # ====================================
    # LEFT COLUMN
    # ====================================

    with col1:

        # ABOUT ME

        st.markdown(
            '<div class="about-label">ABOUT ME</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="about-title">Data Analytics & Business Insights</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="about-subtitle">Business Thinking. Data-Driven Solutions.</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="about-text">
            I am a business professional with <b>8 years of experience
            in sales and marketing</b>, with a growing focus on data
            analytics and business intelligence. My business background
            enables me to understand business challenges and transform
            raw data into meaningful insights that support informed
            decision-making and business growth.
        </div>

        <div class="about-text">
            I use tools such as <b>Excel, SQL, Python, and Power BI</b>
            to analyze data, identify trends, and uncover business
            opportunities. I also leverage <b>n8n workflow automation</b>
            to streamline repetitive tasks and improve operational efficiency.
        </div>

        <div class="about-text">
            My goal is to combine business knowledge, data analytics,
            and automation to deliver practical, data-driven solutions
            that create value for businesses.
        </div>
        """, unsafe_allow_html=True)


        # TECHNICAL SKILLS

        st.markdown(
            '<div class="section-title">Technical Skills</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="skills-text">
            Excel · SQL · Python · Power BI · Looker Studio · n8n Automation
        </div>
        """, unsafe_allow_html=True)


        # DIVIDER AFTER TECHNICAL SKILLS

        st.markdown("""
        <div style="
            width: 100%;
            border-top: 1px solid #d5dbe3;
            margin-top: 35px;
            margin-bottom: 25px;
        "></div>
        """, unsafe_allow_html=True)


        # FEATURED PROJECT

        st.markdown(
            '<div class="section-title" style="margin-top:0;">Featured Project</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="project-title">
            Used Car Price Prediction
        </div>

        <div class="project-text">
            This project develops a machine learning model to predict
            used car prices based on vehicle characteristics and
            specifications. Using 19,237 records and 18 features,
            the project covers data preprocessing, exploratory data
            analysis, feature engineering, regression modeling,
            hyperparameter tuning, and model evaluation.
        </div>

        <div style="margin-top:20px; line-height:2.5;">
            <a href="https://drive.google.com/file/d/1j5HiJAImFhySDgTKpnrQW6ZrN7--qdOS/view?usp=drive_link" target="_blank">
                View Project Presentation
            </a>
        </div>
        """, unsafe_allow_html=True)


    # ====================================
    # RIGHT COLUMN
    # ====================================

    with col2:

        # PROFILE

        st.markdown(
            '<div style="text-align:center; padding-top:65px;">',
            unsafe_allow_html=True
        )

        if profile_image:
            st.markdown(
                f'<img src="{profile_image}" class="profile-image">',
                unsafe_allow_html=True
            )
        else:
            st.warning("Profile image not found. Check assets folder.")

        st.markdown("""
        <div class="profile-name">Maulana</div>
        <div class="profile-role">Data Analyst and Science</div>
        <div class="profile-location">
            📍 Banda Aceh, Indonesia
        </div>
        </div>
        """, unsafe_allow_html=True)


        # DIVIDER AFTER PROFILE

        st.markdown("""
        <div style="
            width: 100%;
            border-top: 1px solid #d5dbe3;
            margin-top: 35px;
            margin-bottom: 25px;
        "></div>
        """, unsafe_allow_html=True)


        # CONNECT WITH ME

        st.markdown(
            '<div class="section-title" style="margin-top:0;">Connect With Me</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="project-text">
            Interested in data analytics, business insights,
            and automation?
        </div>

        <div style="margin-top:20px; line-height:2.5;">
            <a href="https://www.linkedin.com/in/maulana-maulana-00b6308a/" target="_blank">
                LinkedIn
            </a>
            <br>
            <a href="https://github.com/mdacademy36" target="_blank">
                GitHub
            </a>
        </div>
        """, unsafe_allow_html=True)


    # ====================================
    # BOTTOM SEPARATOR
    # ====================================

    st.divider()
