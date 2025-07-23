import streamlit as st
import datetime
import wikipedia
import re

# Initialize reminder list
if "reminders" not in st.session_state:
    st.session_state.reminders = []

def get_response(user_input):
    user_input = user_input.lower()

    # Greeting
    if any(greet in user_input for greet in ["hello", "hi", "hey"]):
        return "Hello! How can I help you today?"

    # Time
    if "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"

    # Date
    if "date" in user_input:
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today}"

    # Math Calculation
    if "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "")
            result = eval(expression)
            return f"The result is {result}"
        except:
            return "Sorry, I couldn't evaluate that expression."

    # Wikipedia Query
    if "who is" in user_input or "what is" in user_input:
        try:
            topic = user_input.replace("who is", "").replace("what is", "").strip()
            summary = wikipedia.summary(topic, sentences=2)
            return summary
        except:
            return "Sorry, I couldn't find that on Wikipedia."

    # Add Reminder
    if "remind me to" in user_input:
        task = re.findall(r"remind me to (.+)", user_input)
        if task:
            st.session_state.reminders.append(task[0])
            return f"Reminder added: {task[0]}"

    # Show Reminders
    if "show reminders" in user_input:
        if st.session_state.reminders:
            return "\n".join([f"🔔 {rem}" for rem in st.session_state.reminders])
        else:
            return "You have no reminders."

    return "I'm not sure how to answer that. Try asking something else!"

def run_chatbot():
    st.subheader("💬 AI Chatbot")

    user_input = st.text_input("You:", key="user_input_chat")

    if user_input:
        response = get_response(user_input)
        st.markdown(f"**Helpi Assistant:** {response}")
