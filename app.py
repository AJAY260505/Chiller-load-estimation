import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime, timedelta
import time
from streamlit_lottie import st_lottie
import requests

# Dummy user database for demonstration purposes
USER_DB = {
    "user@example.com": "password123",  # username: password
}

# Register new user
def register_user(email, password):
    if email in USER_DB:
        st.error("User already exists! Please try logging in.")
    else:
        USER_DB[email] = password
        st.success("Account created successfully! You can now log in.")

# Fetch Lottie animation from URL
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Dummy data generation for the chiller load and energy savings
def fetch_data():
    actual_load = np.random.uniform(50, 150, 720)  # Simulated actual loads
    predicted_load = np.random.uniform(50, 150, 720)  # Simulated predicted loads
    timestamp = [datetime.now() - timedelta(hours=i) for i in range(720)]
    return {
        "timestamp": timestamp,
        "actual_load": actual_load,
        "predicted_load": predicted_load,
        "energy_savings": np.random.uniform(0, 20, 720),  # Simulated energy savings
        "efficiency_scores": np.random.uniform(75, 100, 720)  # Simulated efficiency scores
    }

# Load data into a DataFrame
def load_data():
    data = fetch_data()
    df = pd.DataFrame(data)
    return df

# Calculate energy savings, cost savings, and CO2 reduction
def calculate_energy_savings(df):
    total_energy_saved = df['energy_savings'].sum()
    cost_saved = total_energy_saved * 0.1  # Assuming cost is $0.1 per kWh
    co2_emissions_reduced = total_energy_saved * 0.5  # Assuming 0.5 kg of CO2 per kWh saved
    return total_energy_saved, cost_saved, co2_emissions_reduced

# Filter data based on the selected timeframe
def filter_data(df, timeframe):
    if timeframe == "Last 10 Seconds":
        return df.iloc[-10:]
    elif timeframe == "Last 1 Minute":
        return df.iloc[-60:]
    elif timeframe == "Last 5 Minutes":
        return df.iloc[-5:]
    elif timeframe == "Last 1 Hour":
        return df.iloc[-60:]
    elif timeframe == "Last 12 Hours":
        return df.iloc[-720:]
    elif timeframe == "Last 24 Hours":
        return df.iloc[-1440:]
    elif timeframe == "Last 7 Days":
        return df.iloc[-168:]
    elif timeframe == "Last 30 Days":
        return df.iloc[-720:]
    else:
        return df

# Welcome page with login and registration forms
def welcome_page():
    st.markdown("""
        <style>
            body {
                background: linear-gradient(135deg, #e0eafc, #cfdef3);
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            }
            .login-form {
                margin: auto;
                margin-top: 100px;
                transition: transform 0.3s;
                position: relative;
                z-index: 1;
            }
            .login-form:hover {
                transform: scale(1.02);
            }
            .login-input {
                margin-bottom: 20px;
                border: 2px solid #007bff;
                border-radius: 5px;
                padding: 12px;
                width: 100%;
                font-size: 16px;
            }
            .login-input:focus {
                border-color: #0056b3;
                outline: none;
            }
            .login-button {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 12px;
                font-size: 16px;
                cursor: pointer;
                width: 100%;
                transition: background-color 0.3s, transform 0.3s;
            }
            .login-button:hover {
                background-color: #0056b3;
                transform: translateY(-2px);
            }
            .title {
                text-align: center;
                color: #007bff;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Load Lottie animation
    lottie_url = "https://lottie.host/137363ea-56b9-4ce5-b005-a36513f5cc8b/sKGlHJ9lCV.json"
    lottie_animation = load_lottie_url(lottie_url)
    st_lottie(lottie_animation, speed=1, width=400, height=400, key="login_animation")

    # Login form container
    st.markdown('<div class="login-form">', unsafe_allow_html=True)
    st.markdown('<h2 class="title">Welcome to Chiller Load Monitoring</h2>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Please login to access the application.</p>', unsafe_allow_html=True)

    with st.form(key='login_form'):
        email = st.text_input("Email", placeholder="Enter your email", key="email")
        password = st.text_input("Password", type="password", placeholder="Enter your password", key="password")
        login_button = st.form_submit_button("Login")

        if login_button:
            if email in USER_DB and USER_DB[email] == password:
                st.session_state.authenticated = True
                st.session_state.welcome_page = True
                st.success("Login successful! Please click the proceed button.")
                time.sleep(1)
            else:
                st.error("Invalid credentials. Please try again.")
    
    if st.button("Register"):
        st.session_state.registering = True

    if st.session_state.get('registering', False):
        st.subheader("Register a New Account")
        reg_email = st.text_input("Email for Registration", placeholder="Enter your email")
        reg_password = st.text_input("Password for Registration", type="password", placeholder="Enter your password")
        if st.button("Create Account"):
            register_user(reg_email, reg_password)

# Welcome page after login with Lottie animation
def show_welcome_page():
    st.title("Welcome!")
    st.write("Thank you for logging in. Click the button below to proceed to the main application.")
    lottie_url = "https://lottie.host/137363ea-56b9-4ce5-b005-a36513f5cc8b/sKGlHJ9lCV.json"
    st_lottie(load_lottie_url(lottie_url), speed=1, width=400, height=400, key="welcome_animation")
    
    if st.button("Proceed to Main Page"):
        st.session_state.page = "Main Page"

# Guided onboarding content
def guided_onboarding():
    st.title("Guided Onboarding")
    st.write("This is where the guided onboarding content will go.")

# Main application
def main():
    st.set_page_config(page_title="Chiller Load Monitoring", layout="wide")

    # Initialize session state for authentication
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.page = "Welcome Page"

    if not st.session_state.authen
