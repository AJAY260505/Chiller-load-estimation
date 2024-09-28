def calculate_energy_savings(actual_load, predicted_load):
    savings = sum(actual_load) - sum(predicted_load)
    return savings
