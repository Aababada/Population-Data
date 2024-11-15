import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('population_data.csv')

# Select the relevant columns
data = data[['Country Name', '2021']]

# Rename the columns
data.columns = ['Country', 'Population']

# Sort the data by population
data = data.sort_values(by='Population', ascending=False)

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(data['Country'], data['Population'])
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Population Distribution by Country (2021)')
plt.show()
