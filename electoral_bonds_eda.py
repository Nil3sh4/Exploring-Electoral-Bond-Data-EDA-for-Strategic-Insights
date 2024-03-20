import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("output1.csv")

# Display the first few rows of the DataFrame
print(data.head())

# Summary statistics
print(data.describe())

# Visualize the distribution of the amount spent using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x="Denomination", bins=20, kde=True)
plt.title("Distribution of Amount Spent")
plt.xlabel("Denomination")
plt.ylabel("Frequency")
plt.show()

# Box plot to identify outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="Denomination")
plt.title("Box Plot of Denomination")
plt.xlabel("Denomination")
plt.show()

# Explore relationships between Purchaser Name and Denomination
plt.figure(figsize=(12, 8))
sns.boxplot(data=data, x="Denomination", y="Purchaser Name")
plt.title("Denomination vs Purchaser Name")
plt.xlabel("Denomination")
plt.ylabel("Purchaser Name")
plt.show()

# Explore relationships between Date and Denomination
plt.figure(figsize=(12, 8))
sns.lineplot(data=data, x="Date", y="Denomination")
plt.title("Denomination over Time")
plt.xlabel("Date")
plt.ylabel("Denomination")
plt.xticks(rotation=45)
plt.show()
