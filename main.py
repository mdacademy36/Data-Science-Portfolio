
import streamlit as st
import textwrap
st.set_page_config(
    page_title="Used Car Price Prediction | MDacademy36",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

import used_car_price
import about
import contact

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F3F6F8;
}

/* Main content text */
.stApp,
.stMarkdown p,
.stMarkdown li {
    color: #37474F !important;
}

/* Main content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #123C43;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Sidebar radio */
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 10px;
}

[data-testid="stSidebar"] [role="radio"] {
    background-color: rgba(255,255,255,0.07);
    padding: 12px;
    border-radius: 8px;
}

[data-testid="stSidebar"] [role="radio"]:hover {
    background-color: rgba(255,255,255,0.18);
}

/* Titles */
h1, h2, h3 {
    color: #123C43;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E5EAF0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

[data-testid="stMetricLabel"] {
    color: #64748B !important;
}

[data-testid="stMetricValue"] {
    color: #123C43 !important;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background-color: #1677A5;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 22px;
    font-weight: 600;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #125D82;
    color: white;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 10px;
}

/* Dividers */
hr {
    border-color: #DCE4E8;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748B;
    font-size: 13px;
    padding: 25px 0 10px 0;
}

/* Sidebar text color correction */
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown span {
    color: #D0E4E6 !important;
}

/* Sidebar branding */
[data-testid="stSidebar"] h2 {
    color: #FFFFFF !important;
}

/* Sidebar navigation heading */
[data-testid="stSidebar"] h3 {
    color: #FFFFFF !important;
}

/* Sidebar captions */
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
    color: #B8CDD0 !important;
}

/* Info box text visibility */
[data-testid="stAlert"] p {
    color: #123C43 !important;
    font-weight: 500 !important;
}

[data-testid="stAlert"] {
    color: #123C43 !important;
}
/* Hide Streamlit Header */
header[data-testid="stHeader"] {
    display: none !important;
}

/* Hide Streamlit Toolbar */
div[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0 !important;
}

/* Remove top decoration */
div[data-testid="stDecoration"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR BRANDING
# ==========================================

with st.sidebar:

    st.markdown("""
    <div style="
        padding: 18px 10px;
        text-align: center;
        background-color: #1B5058;
        border-radius: 12px;
        margin-bottom: 25px;
    ">
        <h2 style="color:white; margin:0;">
            MD<span style="color:#64B5F6;">ACADEMY36</span>
        </h2>
        <p style="
            color:#D0E4E6;
            font-size:11px;
            letter-spacing:2px;
            margin:5px 0 0 0;
        ">
            DATA SCIENCE PORTFOLIO
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Navigation")

    menu = st.radio(
        "Choose Page",
        [
            "Home",
            "Used Car Price Prediction",
            "About",
            "Contact"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.caption("MACHINE LEARNING PROJECT")
    st.caption("Used Car Price Prediction")
    st.caption("Developed by MDacademy36")


# ==========================================
# HOME PAGE
# ==========================================

if menu == "Home":

    st.html("""
    <div style="
        background-color: #123C43;
        padding: 35px;
        border-radius: 15px;
        margin-bottom: 25px;
    ">
        <p style="
            color: #80CBC4;
            font-size: 13px;
            letter-spacing: 2px;
        ">
            MACHINE LEARNING · REGRESSION
        </p>

        <h1 style="
            color: #FFFFFF !important;
            font-size: 35px;
            margin: 0;
        ">
            Used Car Price Prediction
        </h1>

        <p style="
            color: #E0EEEE;
            font-size: 16px;
            line-height: 1.7;
        ">
            Predicting used car prices based on vehicle specifications
            using supervised machine learning regression models.
        </p>
    </div>
    """)


    st.subheader("Project Overview")

    st.write("""
    This project aims to develop a machine learning model
    that estimates the selling price of used vehicles based
    on their characteristics and specifications.

    The analysis covers data preprocessing, exploratory data
    analysis, feature engineering, regression modeling,
    and model evaluation.
    """)

    st.divider()

    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", "19,237")
    col2.metric("Total Features", "18")
    col3.metric("Target Variable", "Price")

    st.divider()

    st.subheader("Project Workflow")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **01. Data Preparation**

        - Data Cleaning
        - Missing Value Handling
        - Feature Engineering
        - Data Transformation
        """)

    with col2:
        st.markdown("""
        **02. Machine Learning**

        - Regression Modeling
        - Model Comparison
        - Hyperparameter Tuning
        - Model Evaluation
        """)

    st.info(
        "Navigate to Used Car Price Prediction "
        "to explore the dataset and prediction interface."
    )


# ==========================================
# PAGE ROUTING
# ==========================================

elif menu == "Used Car Price Prediction":
    used_car_price.app()

elif menu == "About":
    about.app()

elif menu == "Contact":
    contact.app()


# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div class="footer">
    © 2024 MDacademy36 |
    <strong>Excel</strong> ·
    <strong>SQL</strong> ·
    <strong>Python</strong> ·
    <strong>Power BI</strong> ·
    <strong>Looker Studio</strong> ·
    <strong>n8n Automation</strong>
</div>
""", unsafe_allow_html=True)

