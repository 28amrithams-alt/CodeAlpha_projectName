import streamlit as st
from chatbot import find_best_match

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Public Help FAQ Chatbot",
    layout="centered"
)

# -------------------------------------------------
# BACKGROUND + UI STYLES (FIXED TEXT VISIBILITY)
# -------------------------------------------------
st.markdown(
    """
    <style>
    /* Page background: calm teal-blue gradient suitable for public help */
    .stApp {
        background: linear-gradient(135deg, #05668D 0%, #028090 50%, #00A896 100%);
        background-attachment: fixed;
        color-scheme: light;
    }

    /* Central chat card with high contrast text */
    .chat-card {
        background-color: rgba(255, 255, 255, 0.98);
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.16);
        max-width: 700px;
        margin: auto;
        color: #023047; /* deep teal for body text */
    }

    /* Heading color (prominent, trustworthy) */
    h1 {
        color: #01303F;
        text-align: center;
    }

    /* Body / label / helper text */
    p, label, span {
        color: #0b3a3a;
        font-size: 16px;
        text-align: center;
    }

    /* Input styling for readability */
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        color: #023047;
        background-color: #f6f9f9;
        border: 1px solid rgba(2,48,71,0.08);
    }

    /* Buttons and success/warning alert tweaks */
    .stButton>button {
        background-color: #028090 !important;
        color: #ffffff !important;
        border-radius: 10px;
    }

    /* Make alerts high-contrast and readable on the card */
    .stAlert-success, .stAlert-success * {
        background-color: #dff3ec !important;
        color: #023047 !important;
        border-radius: 10px;
    }

    .stAlert-warning, .stAlert-warning * {
        background-color: #fff4e5 !important;
        color: #663c00 !important;
        border-radius: 10px;
    }

    /* Remove Streamlit's top white header/menu and footer to avoid an empty white bar */
    #MainMenu { visibility: hidden; }
    header { display: none !important; height: 0 !important; margin: 0 !important; padding: 0 !important; }
    footer { visibility: hidden; }

    /* Welcome banner (inserted by the app) - fixed and full width to avoid white box */
    .welcome-banner {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        width: 100%;
        padding: 12px 0;
        text-align: center;
        background: rgba(1,48,64,0.98); /* deep teal overlay */
        color: #ffffff;
        font-weight: 600;
        border-bottom: 1px solid rgba(255,255,255,0.06);
        box-shadow: 0 2px 6px rgba(0,0,0,0.12);
    }

    /* Make main block transparent so the banner doesn't sit inside a white box */
    .block-container {
        padding-top: 3.8rem; /* leave space for fixed banner */
        background: transparent !important;
        margin-top: 0;
    }

    /* Also ensure the parent main and app containers are transparent */
    .main, .css-1lcbmhc.e1ewe7hr2, .stApp > .main {
        background: transparent !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# CHATBOT UI
# -------------------------------------------------
# top welcome banner replaces the default header
st.markdown("<div class='welcome-banner'>🚨 <strong>Welcome</strong> — Public Help FAQ Chatbot: Ask about medical emergencies, safety, and facilities.</div>", unsafe_allow_html=True)

st.markdown("<div class='chat-card'>", unsafe_allow_html=True)

st.title("🚨 Public Help FAQ Chatbot")

st.write(
    "Ask questions related to **medical emergencies, ambulance assistance, public safety, "
    "women’s safety, travel help, and essential facilities**."
)

user_input = st.text_input("Enter your question:")

if user_input.strip():
    response = find_best_match(user_input)
    st.success(response)

st.markdown("</div>", unsafe_allow_html=True)
