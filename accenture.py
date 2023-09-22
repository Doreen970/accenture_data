import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
df = pd.read_csv("topcategory1.csv")

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['total_score'])
plt.xlabel('Category')
plt.ylabel('Total Score')
plt.title('Total Scores by Category')
plt.xticks(rotation=45)

# Show the chart
plt.tight_layout()
plt.show()
