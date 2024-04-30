import matplotlib.pyplot as plt
import pandas as pd  # For data manipulation (optional)

# Choose a data source (replace with your actual data)
# Option 1: Sample data (modify as needed)
data = {
    "Date": ["2024-04-25", "2024-04-26", "2024-04-27", "2024-04-28", "2024-04-29"],
    "Temperature (Celsius)": [15, 18, 20, 17, 14],
    "Precipitation (mm)": [0, 1.2, 0.5, 2.1, 0]  # Add another weather element
}

# Option 2: Load data from a CSV file (example)
# data = pd.read_csv("weather_data.csv")  # Replace with your filename

# Convert dates to datetime format (optional, if needed for plotting)
if "Date" in data:
    data["Date"] = pd.to_datetime(data["Date"])

# Select desired weather elements (modify as needed)
weather_elements = ["Temperature (Celsius)", "Precipitation (mm)"]  # Choose elements to visualize

# Create the visualization (replace 'Line' with your preferred chart type, e.g., 'Bar')
plt.figure(figsize=(10, 6))  # Adjust figure size for better readability
for element in weather_elements:
    plt.plot(data["Date"], data[element], label=element)

# Customize the plot
plt.xlabel("Date")
plt.ylabel("Value")  # Adjust label based on weather elements
plt.title("Weather Data Visualization (Punjab, India)")  # Modify title
plt.grid(True)
plt.legend()  # Include a legend if displaying multiple weather elements
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability with many dates

# Display the plot
plt.tight_layout()  # Adjust spacing between elements
plt.show()
