# plot_utils.py
import matplotlib.pyplot as plt
import numpy as np

def plot_load_data(actual_load, predicted_load):
    plt.figure(figsize=(12, 6))
    plt.plot(actual_load, label='Actual Load', marker='o')
    plt.plot(predicted_load, label='Predicted Load', marker='x')
    plt.title('Actual vs Predicted Load')
    plt.xlabel('Time Interval')
    plt.ylabel('Load (KW)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_historical_data(historical_load):
    plt.figure(figsize=(12, 6))
    plt.plot(historical_load, label='Historical Load', color='orange')
    plt.title('Historical Load Over Time')
    plt.xlabel('Time Interval')
    plt.ylabel('Load (KW)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
