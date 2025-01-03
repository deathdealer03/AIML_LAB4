import pandas as pd  
data = {
    'Name': ['Tom', 'Nick', 'Krish', 'Jack', 'John'],  # Capitalized names for consistency
    'Age': [15, 21, 30, 18, 25],  # Removed the extra value '29' to match other columns
    'Salary': [500000, 55000, 50600, 58000, 52000],  # Salaries corresponding to the names
    'Department': ['HR', 'ENGINEERING', 'HR', 'MARKETING', 'HR']  # Correct department names
}

# Create a DataFrame
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv('exp4.csv', index=False)

# Read the data back from the CSV file
data = pd.read_csv('exp4.csv')

# Print the data to verify
print(data)
