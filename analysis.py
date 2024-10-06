import pandas as pd

# Updated file path with .csv extension
file_path = 'C:/Users/DELL/Desktop/Company Data Financial Analysis/Financials.csv'

# Load the dataset
try:
    df = pd.read_csv(file_path)
    print("File loaded successfully.")
except FileNotFoundError:
    print(f"File not found at {file_path}. Please check the file path and try again.")

# Clean column names and process data
df.columns = df.columns.str.strip()  # Remove leading and trailing spaces

# Display column names and the first few rows
print("Cleaned column names:", df.columns)
print(df.head())



import matplotlib.pyplot as plt

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plot Sales over Time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()


import pandas as pd

# Assuming df is your DataFrame and it is already cleaned

# Define the path to save the cleaned file on your desktop
output_path = 'C:/Users/DELL/Desktop/Company_Data_Financial_Analysis_Cleaned.csv'

# Save the DataFrame to a CSV file
df.to_csv(output_path, index=False)

print(f'Cleaned data has been saved to {output_path}')
