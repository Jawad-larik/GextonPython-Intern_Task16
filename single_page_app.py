import streamlit as st
from chatbot import run_chatbot
from data_analysis import run_data_analysis
from prediction import run_prediction
from firebase_auth import login, logout

# Page settings
st.set_page_config(page_title="Helpi Assistant", layout="wide")

# Title
st.title("🤖 Helpi Assistant – AI Chatbot, Data Analysis & Prediction")

# Initialize session state
if "auth_status" not in st.session_state:
    st.session_state.auth_status = False
if "user" not in st.session_state:
    st.session_state.user = None

# Main Tabs
tabs = st.tabs(["🔐 Login", "💬 Chatbot", "📊 Data Analysis", "📈 Predictive Modeling", "🔓 Logout"])

# Tab 1 – Login
with tabs[0]:
    login()

# Tab 2 – Chatbot
with tabs[1]:
    if st.session_state.auth_status:
        run_chatbot()
    else:
        st.warning("Please login to use this feature.")

# Tab 3 – Data Analysis
with tabs[2]:
    if st.session_state.auth_status:
        run_data_analysis()
    else:
        st.warning("Please login to use this feature.")

# Tab 4 – Prediction
with tabs[3]:
    if st.session_state.auth_status:
        run_prediction()
    else:
        st.warning("Please login to use this feature.")

# Tab 5 – Logout
with tabs[4]:
    if st.session_state.auth_status:
        logout()
    else:
        st.info("You're already logged out.")
