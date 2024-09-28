# Chiller Load Monitoring & Forecasting

## Overview

The **Chiller Load Monitoring & Forecasting** application provides an intuitive and interactive platform for monitoring and analyzing chiller performance. Utilizing advanced AI algorithms, the application forecasts chiller loads, tracks energy savings, and provides actionable insights to improve operational efficiency.

## Problem Statement

Chillers are critical components in HVAC systems, and their performance directly impacts energy consumption and operational costs. Traditional monitoring systems lack real-time analytics and predictive capabilities, making it challenging for operators to optimize chiller performance. 

### Key Challenges:

- **Inefficient Monitoring**: Limited visibility into chiller performance metrics.
- **High Energy Costs**: Rising electricity prices necessitate efficient energy management.
- **Predictive Analytics**: Lack of tools to forecast future loads and make data-driven decisions.

## Unique Selling Proposition (USP)

1. **AI-Driven Insights**: Integrates machine learning to provide predictive analytics for load forecasting, helping businesses optimize energy consumption.
  
2. **User-Centric Interface**: The application features an interactive and visually appealing UI, making it easy for users to monitor performance and gain insights at a glance.

3. **Comprehensive Metrics**: Tracks energy savings, efficiency scores, and CO2 emissions reduction, enabling users to make informed operational decisions.

4. **Customizable Dashboard**: Users can tailor their monitoring experience with options to filter data by timeframe and select specific operational parameters.

5. **Guided Onboarding**: The application includes a guided onboarding process, ensuring new users can quickly understand and navigate the platform.

## Features

- **Real-Time Monitoring**: Visualize actual vs. predicted chiller loads in real-time.
- **Energy Overview**: Track total energy saved, cost savings, and CO2 emissions reductions.
- **Interactive Graphs**: Utilize Plotly for dynamic data visualization, providing in-depth analytics.
- **Timeframe Filtering**: Choose from multiple timeframes to analyze chiller performance.
- **User Authentication**: Secure access with user login and registration functionalities.
- **Maintenance Reminders**: Automated notifications based on performance data and historical usage.

## Technical Stack

- **Frontend**: Streamlit for building interactive web applications.
- **Backend**: Python for data processing and analysis.
- **Data Visualization**: Plotly for creating interactive plots and charts.
- **Machine Learning**: Scikit-learn for implementing AI algorithms (future plans).
- **APIs**: Utilizes requests for fetching external resources (e.g., Lottie animations).

## Getting Started

### Prerequisites

To run this project locally, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone <https://github.com/AJAY260505/Chiller-load-estimation>
   cd chiller-load-estimation
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

   # Dummy user database for demonstration purposes
USER_DB = {
    "user@example.com": "password123",
}

### Usage

- **Login**: Enter your credentials to access the application.
- **Select Chiller**: Choose the chiller you want to monitor from the sidebar.
- **View Metrics**: Explore various performance metrics and visualizations to gain insights.

## Contributing

Contributions are welcome! If you'd like to improve the application or add new features, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to reach out at [ajay260505@.com].
