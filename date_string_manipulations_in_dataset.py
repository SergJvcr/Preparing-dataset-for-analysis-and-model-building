# Date string manipulations with Python

# In this case, we will work with 2016–2018 lightning strike data from 
# the National Oceanic and Atmospheric Association (NOAA) 
# to calculate weekly sums of lightning strikes and plot them on a bar graph. 
# Then, we will calculate quarterly lightning strike totals and plot them on bar graphs.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read in the data
df = pd.read_csv('google_data_analitics\\eda_manipulate_date_strings_with_python.csv')
print(df.head(10))

# Create new time columns
# Convert the `date` column to datetime.
df['date'] = pd.to_datetime(df['date'])
# In this case, we will use:
# %Y for year, %V for week number, %q for quarter
df['week'] = df['date'].dt.strftime('%Y-W%V')
df['month'] = df['date'].dt.strftime('%Y-%m')
df['quarter'] = df['date'].dt.to_period('Q').dt.strftime('%Y-Q%q')
df['year'] = df['date'].dt.strftime('%Y')

print(df.head(10))

# Plot the number of weekly lightning strikes in 2018
# Create a new dataframe view of just 2018 data, summed by week.
mask = df['year'] == '2018'
df_by_week_2018 = df[mask].groupby(['week']).sum().reset_index()

print(df_by_week_2018.head())

# Plot a bar graph of weekly strike totals in 2018.
plt.bar(x = df_by_week_2018['week'],
        height = df_by_week_2018['number_of_strikes'],
        color = 'orange')
plt.plot()
plt.xlabel("Week number")
plt.ylabel("Number of lightning strikes")
plt.title("Number of lightning strikes per week (2018)")
plt.xticks(rotation = 45, fontsize = 8) # Rotate x-axis
plt.show()

# Plot the number of quarterly lightning strikes from 2016–2018
# Group 2016-2018 data by quarter and sum
df_by_quarter = df.groupby(['quarter']).sum().reset_index()
# Format as text, in millions
df_by_quarter['number_of_strikes_formatted'] = df_by_quarter['number_of_strikes'].div(1000000).round(1).astype(str) + 'M'

print(df_by_quarter.head())

# Add labels
# Before we start plotting, writing a function 
# that will help label each bar in the plot with its 
# corresponding number_of_strikes_formatted text

def add_labels(x, y, labels):
    '''
    Iterates over data and plots text labels above each bar of bar graph.
    '''
    for i in range(len(x)):
        plt.text(i, y[i], labels[i], ha = 'center', va = 'bottom')

# Plot the bar graph
plt.figure(figsize = (15, 5))
plt.bar(x = df_by_quarter['quarter'], height = df_by_quarter['number_of_strikes'])
add_labels(df_by_quarter['quarter'], df_by_quarter['number_of_strikes'], df_by_quarter['number_of_strikes_formatted'])
plt.plot()
plt.xlabel('Quarter')
plt.ylabel('Number of lightning strikes')
plt.title('Number of lightning strikes per quarter (2016-2018)')
plt.show()

# Create a grouped bar chart
# Create two new columns
df_by_quarter['quarter_number'] = df_by_quarter['quarter'].str[-2:]
df_by_quarter['year'] = df_by_quarter['quarter'].str[:4]

print(df_by_quarter.head())

# Fill in the chart parameters
plt.figure(figsize = (15, 5))
p = sns.barplot(
    data = df_by_quarter,
    x = 'quarter_number',
    y = 'number_of_strikes',
    hue = 'year')
for b in p.patches:
    p.annotate(str(round(b.get_height()/1000000, 1))+'M', 
                   (b.get_x() + b.get_width() / 2., b.get_height() + 1.2e6), 
                   ha = 'center', va = 'bottom', 
                   xytext = (0, -12), 
                   textcoords = 'offset points')
plt.xlabel("Quarter")
plt.ylabel("Number of lightning strikes")
plt.title("Number of lightning strikes per quarter (2016-2018)")
plt.show()