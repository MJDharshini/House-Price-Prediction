import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SmartHome AI",
    page_icon="🏠",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(91, 74, 255, 0.25),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(0, 200, 255, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(120, 60, 255, 0.15),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #080b14 0%,
            #10152a 45%,
            #0b1020 100%
        );

    background-attachment: fixed;
}

.block-container {
    max-width: 900px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #a9acb8;
    font-size: 17px;
    margin-bottom: 25px;
}

/* Login card */
.login-card {
    background: rgba(24, 29, 48, 0.78);
    padding: 35px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow:
        0 20px 50px rgba(0,0,0,0.45),
        0 0 40px rgba(91,74,255,0.08);
    text-align: center;
    margin-top: 30px;
    backdrop-filter: blur(12px);
}

/* Success */
.success-card {
    background: rgba(16, 52, 40, 0.82);
    padding: 45px;
    border-radius: 25px;
    border: 1px solid rgba(70, 220, 160, 0.35);
    text-align: center;
    box-shadow:
        0 20px 50px rgba(0,0,0,0.45),
        0 0 35px rgba(40,200,130,0.08);
    backdrop-filter: blur(12px);
}

/* Result */
.result-card {
    background: rgba(25, 31, 53, 0.82);
    padding: 45px;
    border-radius: 25px;
    border: 1px solid rgba(120, 140, 255, 0.25);
    text-align: center;
    box-shadow:
        0 20px 55px rgba(0,0,0,0.5),
        0 0 40px rgba(91,74,255,0.10);
    backdrop-filter: blur(12px);
}

/* Logo */
.logo {
    font-size: 65px;
    text-align: center;
}

/* Price */
.price {
    font-size: 45px;
    font-weight: 900;
    color: white;
    text-align: center;
    margin: 15px 0;
}

/* Input labels */
label {
    font-weight: 600 !important;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    height: 48px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "page" not in st.session_state:
    st.session_state["page"] = "login"

if "username" not in st.session_state:
    st.session_state["username"] = ""

if "prediction" not in st.session_state:
    st.session_state["prediction"] = None


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("house_price_model.pkl")


try:
    model = load_model()

except Exception:
    st.error("❌ Model could not be loaded.")

    st.info(
        "Make sure house_price_model.pkl is inside "
        "your HousePricePrediction folder."
    )

    st.stop()


# =========================================================
# PAGE 1 - LOGIN
# =========================================================

if not st.session_state["logged_in"]:

    st.markdown(
        '<div class="logo">🏠</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="main-title">SmartHome AI</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">'
        'Intelligent House Price Prediction System'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        '<div class="login-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<h2 style="color:white;">🔐 Welcome Back</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#a9acb8;">'
        'Login to continue to SmartHome AI'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    username = st.text_input(
        "👤 Username",
        placeholder="Enter your username"
    )

    password = st.text_input(
        "🔑 Password",
        type="password",
        placeholder="Enter your password"
    )

    st.write("")

    if st.button(
        "🔐 Login",
        use_container_width=True
    ):

        if username.strip() and password.strip():

            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["page"] = "success"

            st.rerun()

        else:

            st.error(
                "⚠️ Please enter both username and password."
            )


# =========================================================
# PAGE 2 - LOGIN SUCCESS
# =========================================================

elif st.session_state["page"] == "success":

    st.markdown(
        '<div class="logo">🎉</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="main-title">Login Successful!</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">'
        'Welcome to SmartHome AI'
        '</p>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        '<div class="success-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<h2 style="color:#ffffff;">✅ Authentication Successful</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<p style="color:#b8d8ca;font-size:17px;">'
        f'Welcome, <b>{st.session_state["username"]}</b>!'
        f'</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#b8d8ca;">'
        'Your SmartHome AI dashboard is ready.'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    if st.button(
        "🏠 Continue to House Prediction",
        use_container_width=True
    ):

        st.session_state["page"] = "prediction"

        st.rerun()


# =========================================================
# PAGE 3 - HOUSE PRICE PREDICTION
# =========================================================

elif st.session_state["page"] == "prediction":

    st.markdown(
        '<p class="main-title">🏠 SmartHome AI</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">'
        'Intelligent House Price Prediction'
        '</p>',
        unsafe_allow_html=True
    )

    st.info(
        "🤖 Enter the property details below to estimate the house price."
    )

    st.divider()

    st.subheader("🏡 Property Details")

    col1, col2 = st.columns(2)

    # =====================================================
    # FIRST COLUMN
    # =====================================================

    with col1:

        bedrooms = st.number_input(
            "🛏️ Number of Bedrooms",
            min_value=1,
            max_value=10,
            value=3
        )

        bathrooms = st.number_input(
            "🛁 Number of Bathrooms",
            min_value=1.0,
            max_value=10.0,
            value=2.0,
            step=0.5
        )

        sqft_living = st.number_input(
            "📐 Living Area (sqft)",
            min_value=300,
            max_value=15000,
            value=1800
        )

        sqft_lot = st.number_input(
            "🌳 Lot Area (sqft)",
            min_value=500,
            max_value=1000000,
            value=5000
        )

        floors = st.number_input(
            "🏢 Number of Floors",
            min_value=1.0,
            max_value=4.0,
            value=1.0,
            step=0.5
        )

        waterfront = st.selectbox(
            "🌊 Waterfront Property",
            ["No", "Yes"]
        )

        view = st.slider(
            "👀 View Rating",
            0,
            4,
            0
        )

        condition = st.slider(
            "⭐ House Condition",
            1,
            5,
            3
        )

    # =====================================================
    # SECOND COLUMN
    # =====================================================

    with col2:

        grade = st.slider(
            "🏆 House Grade",
            1,
            13,
            7
        )

        sqft_above = st.number_input(
            "⬆️ Above Ground Area (sqft)",
            min_value=300,
            max_value=15000,
            value=1800
        )

        sqft_basement = st.number_input(
            "⬇️ Basement Area (sqft)",
            min_value=0,
            max_value=5000,
            value=0
        )

        yr_built = st.number_input(
            "📅 Year Built",
            min_value=1900,
            max_value=2026,
            value=2000
        )

        yr_renovated = st.number_input(
            "🔨 Year Renovated",
            min_value=0,
            max_value=2026,
            value=0
        )

        zipcode = st.number_input(
            "📍 ZIP Code",
            min_value=10000,
            max_value=99999,
            value=98001
        )

        lat = st.number_input(
            "🌐 Latitude",
            value=47.5,
            format="%.6f"
        )

        long = st.number_input(
            "🌐 Longitude",
            value=-122.2,
            format="%.6f"
        )

        sqft_living15 = st.number_input(
            "🏘️ Nearby Living Area (sqft)",
            min_value=300,
            max_value=15000,
            value=1800
        )

        sqft_lot15 = st.number_input(
            "🏘️ Nearby Lot Area (sqft)",
            min_value=500,
            max_value=1000000,
            value=5000
        )

    st.divider()

    # =====================================================
    # PREDICT BUTTON
    # =====================================================

    if st.button(
        "🔮 Predict House Price",
        use_container_width=True
    ):

        waterfront_value = (
            1 if waterfront == "Yes" else 0
        )

        house = pd.DataFrame([{

            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "sqft_living": sqft_living,
            "sqft_lot": sqft_lot,
            "floors": floors,
            "waterfront": waterfront_value,
            "view": view,
            "condition": condition,
            "grade": grade,
            "sqft_above": sqft_above,
            "sqft_basement": sqft_basement,
            "yr_built": yr_built,
            "yr_renovated": yr_renovated,
            "zipcode": zipcode,
            "lat": lat,
            "long": long,
            "sqft_living15": sqft_living15,
            "sqft_lot15": sqft_lot15

        }])

        try:

            prediction = model.predict(house)

            st.session_state["prediction"] = float(
                prediction[0]
            )

            st.session_state["page"] = "result"

            st.rerun()

        except Exception as e:

            st.error("❌ Prediction failed.")
            st.code(str(e))


# =========================================================
# PAGE 4 - RESULT
# =========================================================

elif st.session_state["page"] == "result":

    price = st.session_state["prediction"]

    st.markdown(
        '<div class="logo">🏠</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="main-title">Prediction Complete</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">'
        'SmartHome AI Analysis'
        '</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        '<div class="result-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<h2 style="color:#b7bdcf;">'
        '💰 Estimated House Market Value'
        '</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="price">${price:,.2f}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#aeb3c2;">'
        '🤖 Machine Learning Based Prediction'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔄 Predict Another House",
            use_container_width=True
        ):

            st.session_state["page"] = "prediction"

            st.rerun()

    with col2:

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.session_state["prediction"] = None
            st.session_state["page"] = "login"

            st.rerun()     