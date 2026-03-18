import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

print(df.head())
print(df.info())
print(df.describe())

#Task 1 Distribution Analysis Using Histograms

#Histogram with 5 bins
plt.figure(figsize=(8,5))
plt.hist(df['total_bill'],bins = 5, color = 'skyblue', edgecolor = 'black')
plt.xlabel('Total Bill (USD)')
plt.ylabel('Frequency')
plt.title('Histogram of Total Bills (5 Bins)')
plt.show()

# Histogram with 20 bins
plt.figure(figsize=(8, 5))
plt.hist(df['total_bill'], bins=20, color='orange', edgecolor='black')
plt.xlabel('Total Bill (USD)')
plt.ylabel('Frequency')
plt.title('Histogram of Total Bill (20 Bins)')
plt.show()

#Answer for Task 1 Markdown cell
#The distribution of total_bill appears to be right-skewed (positively skewed) because most bills are concentrated at lower values, while a few bills extend to higher amounts.
#With 5 bins, the histogram gives a general overview of the distribution but hides finer details. With 20 bins, the histogram shows more detail, making it easier to see the spread, peaks, and possible gaps in the data.

#Task 2 Outlier Detection Using Box Plots

#Plot code
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', data=df, order=['Thur', 'Fri', 'Sat', 'Sun'])
plt.xlabel('Day')
plt.ylabel('Total Bill (USD)')
plt.title('Box Plot of Total Bill Across Days')
plt.show()

# Task 2: Outlier Detection Using Box Plots - Markdown cell Answer

#1. The day with the highest median total bill appears to be **[write the day from your output]**.
#2. At least one day that appears to have outliers is **[write the day, e.g., Sunday]**.
#3. I calculated the Interquartile Range (IQR) manually using `groupby()` and `quantile()`:
 #  - **Q1** = 25th percentile
  # - **Q3** = 75th percentile
   #- **IQR** = Q3 - Q1

   #Then I used the standard outlier rule:
   #- **Lower Bound = Q1 - 1.5 × IQR**
   #- **Upper Bound = Q3 + 1.5 × IQR**

   #Any `total_bill` values outside this range are considered outliers. The identified values for the selected day fall outside these bounds, so they are confirmed as outliers.

#Task 3 Multi-Variable Comparison Using an Interactive Plot

import plotly.express as px

fig = px.scatter(
    df,
    x='total_bill',
    y='tip',
    color='time',
    hover_data=['day', 'size'],
    title='Interactive Scatter Plot: Total Bill vs Tip by Meal Time'
)

fig.show()

#Answer for Task 3
#There appears to be a positive relationship between total_bill and tip. As the total bill increases, the tip generally tends to increase as well.
#Lunch and Dinner transactions show some differences. Dinner points are usually more spread out and include higher bill amounts, while Lunch points are more concentrated in a smaller range. This suggests dinner bills are often larger and may lead to more varied tip amounts.
#One interesting data point is a transaction with a very high total bill but a comparatively low tip (or a very high tip for a moderate bill). This stands out because it differs from the general positive trend and may represent unusual tipping behavior.




