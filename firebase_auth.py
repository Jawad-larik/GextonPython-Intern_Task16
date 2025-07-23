import streamlit as st
import pyrebase

# Firebase configuration — replace with your actual keys
firebase_config = {
    "apiKey": "AIzaSyCJGOJ7ktI1un2B6ZWq-nLk8MY1g1qcyFs",
    "authDomain": "help-assistant-ai-chatbot.firebaseapp.com",
    "projectId": "help-assistant-ai-chatbot",
    "storageBucket": "help-assistant-ai-chatbot.firebasestorage.app",
    "messagingSenderId": "156951616597",
    "appId": "1:156951616597:web:3acacb18c550e6676448dc",
    "measurementId": "G-4HSE4XMZ2G",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login():
    st.subheader("🔐 Login or Register")

    choice = st.radio("Select option:", ["Login", "Register", "Continue as Guest"])

    if choice == "Login":
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.auth_status = True
                st.session_state.user = user
                st.success("✅ Logged in successfully")
            except:
                st.error("Login failed. Check credentials.")

    elif choice == "Register":
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_pass")
        if st.button("Register"):
            try:
                auth.create_user_with_email_and_password(email, password)
                st.success("✅ Registration successful. You can now log in.")
            except:
                st.error("Registration failed. Try different credentials.")

    elif choice == "Continue as Guest":
        st.session_state.auth_status = True
        st.session_state.user = {"email": "guest@helpi.ai"}
        st.success("✅ Continuing as Guest")


def logout():
    st.subheader("🔓 Logout")
    if st.button("Logout Now"):
        st.session_state.auth_status = False
        st.session_state.user = None
        st.success("You’ve been logged out.")

def check_auth_status():
    return st.session_state.get("auth_status", False)
