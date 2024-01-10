import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Read in the data
df = pd.read_csv('google_data_analitics\\eda_outliers_dataset1.csv')
print(df.head(10))

# Create a function that convert the number of strikes value 
# to a more readable format on the graph 
# (e.g., converting 100,000 to 100K, 3,000,000 to 3M, and so on):
def readable_numbers(x):
    """
    takes a large number and formats it into K,M to make it more readable.
    """
    if x >= 1e6:
        s = '{:1.1f}M'.format(x*1e-6)
    else:
        s = '{:1.0f}K'.format(x*1e-3)
    return s

# Use the readable_numbers() function to create a new column 
df['number_of_strikes_readable']=df['number_of_strikes'].apply(readable_numbers)

# Create a box plot for showing outliers
box = sns.boxplot(x=df['number_of_strikes'])
g = plt.gca()
box.set_xticklabels(np.array([readable_numbers(x) for x in g.get_xticks()]))
plt.xlabel('Number of strikes')
plt.title('Yearly number of lightning strikes')
plt.show()
# here are two dots on the left side outer our figure - outliers

# Calculating the lower threshold for outliers:
# Calculate 25th percentile of annual strikes
percentile25 = df['number_of_strikes'].quantile(0.25)
# Calculate 75th percentile of annual strikes
percentile75 = df['number_of_strikes'].quantile(0.75)
# Calculate interquartile range
iqr = percentile75 - percentile25
# Calculate upper and lower thresholds for outliers
upper_limit = percentile75 + 1.5 * iqr
lower_limit = percentile25 - 1.5 * iqr
# The points that have values less than lower_limit 
# or more than upper_limit are outliers:
print('Lower limit is: ', lower_limit)
print('Upper limit is: ', upper_limit)

# A Boolean mask was used to filter the dataframe 
# so it only contained rows where the number of strikes 
# was less than the lower limit:
mask_for_lower_limit = df['number_of_strikes'] < lower_limit
print(df[mask_for_lower_limit])

# OR we can show in on a scatter plot:
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(x[i]-0.5, y[i]+500000, s=readable_numbers(y[i]))

colors = np.where(df['number_of_strikes'] < lower_limit, 'r', 'b')

fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(df['year'], df['number_of_strikes'],c=colors)
ax.set_xlabel('Year')
ax.set_ylabel('Number of strikes')
ax.set_title('Number of lightning strikes by year')
addlabels(df['year'], df['number_of_strikes'])
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
plt.show()


#  DELEATE OUTLIERS
# Once you know the cutoff points for outliers, 
# if you want to delete them, you can use a Boolean mask 
# to select all rows such that: lower limit ≤ values ≤ upper limit.  
mask_for_delete_lower_outliers = (df['number_of_strikes'] >= lower_limit) & (df['number_of_strikes'] <= upper_limit)
df = df[mask_for_delete_lower_outliers].copy()
print(df)

# REASSIGNING OUTLIERS.
# Instead of deleting outliers, we can always reassign them, 
# that is, change the values to ones that fit within 
# the general distribution of the dataset.

# Create a floor and ceiling at a quantile: for example, 
# you could place walls at the 90th and 10th percentile of the distribution of data values. 
# Any value above the 90% mark or below the 10% mark are changed to fit within the walls you set.
# Calculate 10th percentile
tenth_percentile = np.percentile(df['number_of_strikes'], 10)

# Calculate 90th percentile
ninetieth_percentile = np.percentile(df['number_of_strikes'], 90)

# Apply lambda function to replace outliers with thresholds defined above
df['number_of_strikes'] = df['number_of_strikes'].apply(lambda x: (
    tenth_percentile if x < tenth_percentile 
    else ninetieth_percentile if x > ninetieth_percentile 
    else x))

print (df)

# OR we can impute the average (the mean) or the median.
# In some cases, it might be best to reassign all outlier values to match the median or mean value. 
# This will ensure that your median and distribution are based solely on the non-outlier values, 
# leaving the original outliers excluded. The actual imputation or reassigning of values can be 
# pretty simple if you’ve already found the outliers. The following code block calculates 
# the median of the values greater than the lower limit. 
# Then it imputes the median where values are lower than the lower limit.

# Calculate median of all NON-OUTLIER values
median = np.median(df['number_of_strikes'][df['number_of_strikes'] >= lower_limit])
# Impute the median for all values < lower_limit
df['number_of_strikes'] = np.where(df['number_of_strikes'] < lower_limit, median, df['number_of_strikes'] )

print(df)