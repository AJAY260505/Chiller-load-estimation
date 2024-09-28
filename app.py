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
    "user@example.com": "password123",
}

def fetch_data():
    # Generate dummy data for the past 30 days (720 hours)
    actual_load = np.random.uniform(50, 150, 720)
    predicted_load = np.random.uniform(50, 150, 720)
    timestamp = [datetime.now() - timedelta(hours=i) for i in range(720)]

    return {
        "timestamp": timestamp,
        "actual_load": actual_load,
        "predicted_load": predicted_load,
        "energy_savings": np.random.uniform(0, 20, 720),
        "efficiency_scores": np.random.uniform(75, 100, 720)
    }

def load_data():
    data = fetch_data()
    df = pd.DataFrame(data)
    return df

def calculate_energy_savings(df):
    total_energy_saved = df['energy_savings'].sum()
    cost_saved = total_energy_saved * 0.1
    co2_emissions_reduced = total_energy_saved * 0.5

    return total_energy_saved, cost_saved, co2_emissions_reduced

def filter_data(df, timeframe):
    if timeframe == "Last 10 Seconds":
        return df.iloc[-10:]
    elif timeframe == "Last 1 Minute":
        return df.iloc[-60:]
    elif timeframe == "Last 5 Minutes":
        return df.iloc[-300:]
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

def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

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
            .login-button {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 12px;
                font-size: 16px;
                cursor: pointer;
                width: 100%;
            }
            .title {
                text-align: center;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
            }
        </style>
    """, unsafe_allow_html=True)

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
                st.session_state.login_success = True
                st.success("Login successful! Please click the proceed button.")
                time.sleep(1)
            else:
                st.error("Invalid credentials. Please try again.")

    st.markdown('</div>', unsafe_allow_html=True)

def show_welcome_page():
    st.title("Welcome!")
    st.write("Thank you for logging in. Click the button below to proceed to the main application.")

    lottie_url = "https://lottie.host/137363ea-56b9-4ce5-b005-a36513f5cc8b/sKGlHJ9lCV.json"
    lottie_animation = load_lottie_url(lottie_url)
    st_lottie(lottie_animation, speed=1, width=400, height=400, key="welcome_animation")

    if st.button("Proceed to Main Page"):
        st.session_state.page = "Main Page"

def guided_onboarding():
    st.title("Guided Onboarding")

    st.subheader("Welcome to Chiller Load Monitoring")
    st.write(
        """
        We’re excited to guide you through our AI-powered chiller monitoring platform. This onboarding will help you 
        understand how to use the platform to monitor, forecast, and optimize your chiller's performance.
        """
    )

    st.subheader("1. System Overview")
    st.write(
        """
        Our platform provides real-time and predictive insights into the performance of your chillers, allowing you to:
        - **Monitor chiller load** in real-time.
        - **Forecast future loads** using AI-based predictive analytics.
        - **Track energy savings** and efficiency metrics.
        - **Receive alerts and notifications** for potential maintenance needs.
        """
    )

    st.subheader("2. Key Features")
    st.write(
        """
        Here’s a breakdown of what you can do within the platform:
        - **Real-Time Data Monitoring**: View live data for actual and predicted chiller loads, updated continuously.
        - **AI-Based Forecasting**: Utilize machine learning models to predict future load demands, helping you to optimize energy use.
        - **Energy Savings Overview**: See detailed calculations of energy savings, cost savings, and reduced CO2 emissions over different time periods.
        - **Efficiency Score Tracking**: Track the efficiency of your chillers, identifying performance trends and areas for improvement.
        """
    )

    st.subheader("3. How to Navigate")
    st.write(
        """
        - **Dashboard**: This is where you’ll monitor your chillers’ real-time load, energy usage, and efficiency scores.
            - **Select a Chiller**: Use the dropdown on the sidebar to choose the chiller you want to analyze.
            - **Set Temperature Range**: Adjust the temperature range filter to analyze the chiller's performance under different conditions.
            - **Timeframe Selection**: Choose a timeframe from the dropdown to view data from the last 10 seconds to the past 30 days.
        """
    )

    st.subheader("4. Step-by-Step Guide")
    st.write(
        """
        1. **Login**: Start by logging into the platform using your email and password.
        2. **Select a Chiller**: Once logged in, head over to the main page and select a chiller from the dropdown menu.
        3. **Monitor Load Data**: You’ll immediately see the real-time load data and efficiency scores for the selected chiller.
        4. **Change Timeframe**: To analyze data for different periods, use the "Timeframe" dropdown to filter the data.
        5. **Check Energy Savings**: Scroll down to the "Energy Overview" section to view your energy and cost savings, as well as CO2 emission reductions.
        6. **Analyze Efficiency**: Review the efficiency scores displayed in the bar chart to assess the chiller's performance over the selected period.
        7. **Receive Alerts**: If any chiller requires attention, you’ll see notifications or alerts regarding potential maintenance needs.
        """
    )

    st.subheader("5. Optimizing Performance with AI")
    st.write(
        """
        Our AI-based predictive analytics provide you with insights to:
        - **Optimize scheduling**: Ensure that your chiller is operating during peak efficiency times.
        - **Scenario Simulation**: Test different operational scenarios to see how changing parameters will impact performance and energy use.
        - **Sustainability Focus**: Our platform helps you reduce energy consumption and achieve sustainability goals by monitoring CO2 emissions and energy savings.
        """
    )

    st.subheader("6. Getting Help")
    st.write(
        """
        If you need assistance at any point, our **Ongoing Customer Support** feature is here to provide guidance. 
        Feel free to use the help button in the sidebar to connect with our support team.
        """
    )

def main():
    st.set_page_config(page_title="Chiller Load Monitoring", layout="wide")

    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.page = "Welcome Page"

    if not st.session_state.authenticated:
        welcome_page()
    else:
        if 'welcome_page' in st.session_state and st.session_state.welcome_page:
            show_welcome_page()
            st.session_state.welcome_page = False
        else:
            st.title("AI-Based Chiller Load Monitoring & Forecasting")

            page = st.sidebar.selectbox("Select a Page", ["Main Page", "Guided Onboarding"])

            if page == "Main Page":
                st.sidebar.header("🌟 Chiller Selection")
                chillers = ["Chiller 1", "Chiller 2", "Chiller 3", "Chiller 4"]
                selected_chiller = st.sidebar.selectbox("Select a Chiller", chillers)

                st.sidebar.subheader("⚙️ Settings")
                temp_range = st.sidebar.slider("Select Temperature Range (°C)", 0, 100, (20, 80))
                st.sidebar.markdown(f"Temperature range selected: **{temp_range[0]}°C** to **{temp_range[1]}°C**")

                operational_params = st.sidebar.multiselect("Operational Parameters", options=["Parameter 1", "Parameter 2", "Parameter 3"])

                df = load_data()
                total_energy_saved, cost_saved, co2_emissions_reduced = calculate_energy_savings(df)

                st.subheader("Energy Overview")
                st.write(f"Total Energy Saved: **{total_energy_saved:.2f} kWh**")
                st.write(f"Total Cost Saved: **${cost_saved:.2f}**")
                st.write(f"CO2 Emissions Reduced: **{co2_emissions_reduced:.2f} kg**")

                timeframe = st.selectbox("Select Timeframe", ["Last 10 Seconds", "Last 1 Minute", "Last 5 Minutes", "Last 1 Hour", "Last 12 Hours", "Last 24 Hours", "Last 7 Days", "Last 30 Days"])
                filtered_df = filter_data(df, timeframe)

                st.subheader("Chiller Load Monitoring")
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=filtered_df['timestamp'], y=filtered_df['actual_load'], mode='lines', name='Actual Load', line=dict(color='blue')))
                fig.add_trace(go.Scatter(x=filtered_df['timestamp'], y=filtered_df['predicted_load'], mode='lines', name='Predicted Load', line=dict(color='orange')))
                fig.update_layout(title='Chiller Load Monitoring', xaxis_title='Time', yaxis_title='Load (kW)', xaxis_rangeslider_visible=True)
                st.plotly_chart(fig)

                st.subheader("Efficiency Scores")
                st.bar_chart(filtered_df['efficiency_scores'])

            elif page == "Guided Onboarding":
                guided_onboarding()

if __name__ == "__main__":
    main()
