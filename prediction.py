import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def run_prediction():
    st.subheader("📈 Predictive Modeling")

    option = st.selectbox("Choose a model to run", ["House Price Prediction", "Student Performance Prediction"])

    if option == "House Price Prediction":
        house_price_prediction()
    elif option == "Student Performance Prediction":
        student_performance_prediction()


def house_price_prediction():
    st.markdown("### 🏠 House Price Prediction")

    # Sample training data
    data = pd.DataFrame({
        "area": [1500, 1800, 2400, 3000, 3500],
        "bedrooms": [3, 4, 3, 5, 4],
        "bathrooms": [2, 3, 2, 4, 3],
        "price": [300000, 400000, 500000, 600000, 650000]
    })

    X = data[["area", "bedrooms", "bathrooms"]]
    y = data["price"]

    model = LinearRegression()
    model.fit(X, y)

    st.write("Enter details for prediction:")

    area = st.number_input("Area (sqft)", min_value=500, max_value=10000, value=1500)
    bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)

    if st.button("Predict Price"):
        input_data = pd.DataFrame([[area, bedrooms, bathrooms]], columns=["area", "bedrooms", "bathrooms"])
        prediction = model.predict(input_data)
        st.success(f"Estimated House Price: ${int(prediction[0]):,}")


def student_performance_prediction():
    st.markdown("### 🎓 Student Performance Prediction")

    # Sample training data
    data = pd.DataFrame({
        "study_hours": [1, 2, 3, 4, 5, 6],
        "attendance": [60, 70, 75, 80, 85, 90],
        "past_grade": [50, 60, 65, 70, 80, 90],
        "final_score": [55, 62, 68, 75, 85, 95]
    })

    X = data[["study_hours", "attendance", "past_grade"]]
    y = data["final_score"]

    model = LinearRegression()
    model.fit(X, y)

    st.write("Enter details for prediction:")

    study_hours = st.slider("Study Hours Per Day", 0, 10, 3)
    attendance = st.slider("Attendance (%)", 0, 100, 75)
    past_grade = st.slider("Past Grade (%)", 0, 100, 65)

    if st.button("Predict Score"):
        input_data = pd.DataFrame([[study_hours, attendance, past_grade]], columns=["study_hours", "attendance", "past_grade"])
        prediction = model.predict(input_data)
        st.success(f"Predicted Final Score: {int(prediction[0])}%")
