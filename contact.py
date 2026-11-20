
import streamlit as st

def app():

    st.markdown("""
        <style>
        .contact-title {
            font-size: 34px;
            font-weight: 700;
            color: #45566f;
            margin-bottom: 18px;
        }

        .contact-text {
            font-size: 16px;
            line-height: 1.8;
            color: #45566f;
        }

        .contact-info {
            font-size: 16px;
            color: #45566f;
            margin-top: 15px;
        }

        .contact-divider {
            border-top: 1px solid #d5dbe3;
            margin-top: 45px;
            margin-bottom: 35px;
        }

        .contact-message {
            background-color: #dceafa;
            color: #164b83;
            padding: 18px;
            border-radius: 8px;
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="contact-title">🤝 Let\'s Connect!</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
        <div class="contact-text">
            I'm always open to collaboration, questions, or just a friendly chat.<br>
            Feel free to reach out through any of the platforms below:
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maulana-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/maulana-maulana-00b6308a/)',
        unsafe_allow_html=True
    )

    st.markdown(
        '[![GitHub](https://img.shields.io/badge/GitHub-Maulana-blue?style=flat&logo=github)](https://github.com/mdacademy36)',
        unsafe_allow_html=True
    )

    st.markdown("""
        <div class="contact-info">
            📧 <b>Email:</b>
            <a href="mailto:molana.secret12@gmail.com">
            molana.secret12@gmail.com</a>
        </div>

        <div class="contact-info">
            📱 <b>WhatsApp:</b>
            <a href="https://wa.me/628116893312" target="_blank">
            Click to chat</a>
        </div>

        <div class="contact-divider"></div>

        <div class="contact-message">
            Let's build something with data. Looking forward to hearing from you.. 😊
        </div>
    """, unsafe_allow_html=True)
