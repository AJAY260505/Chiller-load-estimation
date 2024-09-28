from datetime import datetime, timedelta  # Importing datetime and timedelta
import pandas as pd

def fetch_data():
    # Simulated data for testing; replace with actual API call in production
    data = {
        "timestamp": [datetime.now() - timedelta(hours=i) for i in range(24)],
        "actual_load": [78.4 + (i % 5) for i in range(24)],  # Simulated load data
        "predicted_load": [80 + (i % 4) for i in range(24)]  # Simulated predicted load
    }
    return pd.DataFrame(data)  # Return a DataFrame directly
