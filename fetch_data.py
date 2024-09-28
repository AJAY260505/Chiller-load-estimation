import random
import pandas as pd
import os

def fetch_data():
    csv_file_path = 'dummy_load_data.csv'
    
    # Check if the file exists
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        actual_load = df['Actual Load'].tolist()
        predicted_load = df['Predicted Load'].tolist()
        historical_load = df['Historical Load'].tolist()
    else:
        # Simulate data if file doesn't exist
        actual_load = [random.uniform(50, 150) for _ in range(10)]
        predicted_load = [random.uniform(50, 150) for _ in range(10)]
        historical_load = [random.uniform(30, 130) for _ in range(30)]
        
        # Create a DataFrame to store the data
        data = {
            'Actual Load': actual_load,
            'Predicted Load': predicted_load,
            'Historical Load': historical_load
        }
        
        df = pd.DataFrame(data)
        df.to_csv(csv_file_path, index=False)  # Save to CSV file
    
    return {
        'actual_load': actual_load,
        'predicted_load': predicted_load,
        'historical_load': historical_load
    }
