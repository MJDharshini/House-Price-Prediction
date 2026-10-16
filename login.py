import streamlit as st


def login():

    # ==============================
    # LOGIN PAGE CSS
    # ==============================
    st.markdown("""
    <style>

    /* Page background */
    .stApp {
        background: linear-gradient(135deg, #eef4f8, #f8fbfd);
    }

    /* Hide Streamlit menu */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Login wrapper */
    .login-wrapper {
        min-height: 75vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Login card */
    .login-card {
        background: white;
        width: 390px;
        padding: 38px 42px;
        border-radius: 22px;
        box-shadow: 0px 12px 35px rgba(0,0,0,0.12);
        border: 1px solid #e8eef2;
        text-align: center;
        margin: auto;
    }

    /* Logo */
    .logo {
        font-size: 55px;
        margin-bottom: 5px;
    }

    /* App name */
    .app-name {
        font-size: 30px;
        font-weight: 800;
        color: #087f73;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .app-subtitle {
        font-size: 14px;
        color: #7a858c;
        margin-bottom: 25px;
    }

    /* Login title */
    .login-title {
        font-size: 24px;
        font-weight: 700;
        color: #263238;
        margin-bottom: 5px;
    }

    .login-text {
        font-size: 14px;
        color: #7a858c;
        margin-bottom: 20px;
    }

    /* Footer text */
    .footer-text {
        text-align: center;
        color: #8a949a;
        font-size: 13px;
        margin-top: 20px;
    }

    </style>
    """, unsafe_allow_html=True)


    # ==============================
    # TOP LOGO / TITLE
    # ==============================

    st.markdown("""
    <div class="login-card">

        <div class="logo">🏠</div>

        <div class="app-name">
            SmartHome AI
        </div>

        <div class="app-subtitle">
            Intelligent House Price Prediction
        </div>

        <div class="login-title">
            🔐 Welcome Back
        </div>

        <div class="login-text">
            Login to continue to your SmartHome AI account
        </div>

    </div>
    """, unsafe_allow_html=True)


    # ==============================
    # USER INPUT
    # ==============================

    username = st.text_input(
        "👤 Username",
        placeholder="Enter your username"
    )

    password = st.text_input(
        "🔑 Password",
        type="password",
        placeholder="Enter your password"
    )


    # ==============================
    # LOGIN BUTTON
    # ==============================

    if st.button(
        "🔐 Login",
        use_container_width=True
    ):

        # ANY USER CAN LOGIN
        if username.strip() != "" and password.strip() != "":

            st.session_state["logged_in"] = True
            st.session_state["username"] = username

            st.success(
                f"✅ Login Successful! Welcome, {username}!"
            )

            # Move to prediction page
            st.session_state["page"] = "prediction"

            st.rerun()

        else:

            st.error(
                "⚠️ Please enter both Username and Password."
            )


    st.markdown("""
    <div class="footer-text">
        🏠 SmartHome AI • House Price Prediction System
    </div>
    """, unsafe_allow_html=True)  