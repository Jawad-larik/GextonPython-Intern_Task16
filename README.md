# GextonPython-Intern_Task16
A modern organization requires an intelligent virtual assistant that can handle natural language queries while providing data analysis capabilities. The solution needs to combine chatbot functionality with data visualization tools and predictive modeling in a user-friendly web interface.

````markdown
# 🤖 Helpi Assistant – AI Chatbot with Data Analysis & Prediction

Helpi Assistant is an intelligent virtual assistant built using **Python** and **Streamlit**. It combines natural language processing, data analysis, and predictive modeling in a clean, user-friendly interface. This project was developed as part of an internship assignment under the guidance of **Sir Muhammad Arham MH**.

---

## 🔍 Features

### 💬 Chatbot (NLP)
- Responds to greetings, time/date, and basic math queries
- Handles knowledge-based queries using **Wikipedia API**
- Maintains a simple reminder list

### 📊 Data Analysis
- Upload and process CSV files
- View statistical summaries
- Generate interactive visualizations using **Plotly**

### 📈 Predictive Modeling
- **House Price Prediction** using area, bedrooms, bathrooms
- **Student Performance Prediction** using study hours, grades, attendance

### 🔐 User Authentication
- Email/password login and registration via **Firebase**
- Guest mode for temporary access
- Session-based login persistence

---

## 🧰 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas, Matplotlib, Seaborn, Plotly
- Pyrebase (Firebase Auth)
- Wikipedia API

---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/helpi-assistant.git
   cd helpi-assistant
````

2. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Firebase**

   * Replace Firebase credentials inside `firebase_auth.py` with your actual Firebase Web App config.

4. **Start the App**

   ```bash
   streamlit run app.py
   ```

---

## 📁 Folder Structure

```
helpi-assistant/
│
├── app.py
├── chatbot.py
├── data_analysis.py
├── prediction.py
├── firebase_auth.py
├── requirements.txt
├── README.md
└── sample_data/
```

---

## 👨‍💻 Developer

**Muhammad Jawad Larik**
Intern – Python Automation
Sindh University | Gexton Education Institute

---

```
