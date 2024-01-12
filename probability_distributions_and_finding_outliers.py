import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
#import statsmodels.api as sm

data = pd.read_csv("google_data_analitics\\modified_c4_epa_air_quality.csv")

# Display first 10 rows of the data
print(data.head(10))
print('The shape of the data:', data.shape)
print(data.describe())
print(data.info())

# Create a histogram to visualize distribution of aqi_log
plt.hist(data['aqi_log'])
plt.xlabel('aqi_log')
plt.title('The distribution of aqi_log')
plt.show()

# Statistical tests
# The empirical rule states that, for every normal distribution:
# - 68% of the data fall within 1 standard deviation of the mean
# - 95% of the data fall within 2 standard deviations of the mean
# - 99.7% of the data fall within 3 standard deviations of the mean

# Define variable for aqi_log mean.
mean_aqi_log = data['aqi_log'].mean()

print(f'The mean is {round(mean_aqi_log, 4)}')

# Define variable for aqi_log standard deviation.
std_aqi_log = data['aqi_log'].std()

print(f'The standard deviation is {round(std_aqi_log, 4)}')

# Define variable for lower limit, 1 standard deviation below the mean.
low_lim_aqi_log = mean_aqi_log - 1 * std_aqi_log
# Define variable for upper limit, 1 standard deviation above the mean.
upp_lim_aqi_log = mean_aqi_log + 1 * std_aqi_log

print(f'The lower limit for 1 std is {round(low_lim_aqi_log, 4)}')
print(f'The upper limit for 1 std is {round(upp_lim_aqi_log, 4)}')

# Display the actual percentage of data that falls within 1 standard deviation of the mean.
data_within_1_std = ((data['aqi_log'] >= low_lim_aqi_log) & (data['aqi_log'] <= upp_lim_aqi_log)).mean()

print(f'The actual % of data that falls within 1 std of the mean is {data_within_1_std} or {round(data_within_1_std * 100, 2)}%')

# Define variable for lower limit, 2 standard deviations below the mean.
low_lim_2_aqi_log = mean_aqi_log - 2 * std_aqi_log
# Define variable for upper limit, 2 standard deviations below the mean.
upp_lim_2_aqi_log = mean_aqi_log + 2 * std_aqi_log

print(f'The lower limit for 2 std is {round(low_lim_2_aqi_log, 4)}')
print(f'The upper limit for 2 std is {round(upp_lim_2_aqi_log, 4)}')

# Display the actual percentage of data that falls within 2 standard deviations of the mean.
data_within_2_std = ((data['aqi_log'] >= low_lim_2_aqi_log) & (data['aqi_log'] <= upp_lim_2_aqi_log)).mean()

print(f'The actual % of data that falls within 2 std of the mean is {data_within_2_std} or {round(data_within_2_std * 100, 2)}%')

# Define variable for lower limit, 3 standard deviations below the mean.
low_lim_3_aqi_log = mean_aqi_log - 3 * std_aqi_log
# Define variable for upper limit, 3 standard deviations above the mean.
upp_lim_3_aqi_log = mean_aqi_log + 3 * std_aqi_log

print(f'The lower limit for 3 std is {round(low_lim_3_aqi_log, 4)}')
print(f'The upper limit for 3 std is {round(upp_lim_3_aqi_log, 4)}')

# Display the actual percentage of data that falls within 3 standard deviations of the mean.
data_within_3_std = ((data['aqi_log'] >= low_lim_3_aqi_log) & (data['aqi_log'] <= upp_lim_3_aqi_log)).mean()

print(f'The actual % of data that falls within 3 std of the mean is {data_within_3_std} or {round(data_within_3_std * 100, 2)}%')

# Results. Evaluation. Z-score. Outliers
# Compute the z-score for every aqi_log value, and add a column named z_score in the data to store those results.
data['z_score'] = stats.zscore(data['aqi_log'])

print(data.head(5))

# Identify the parts of the data where aqi_log is above or below 3 standard deviations of the mean
mask = ((data['z_score'] < -3) | (data['z_score'] > 3)) # | - it's like 'or'
print(data[mask])

# To show the outliers
plt.scatter(x=data['z_score'], y=data['z_score'], alpha=0.3)
plt.scatter(x=data['z_score'][mask], y=data['z_score'][mask], c='orange', alpha=1, marker='D', s=75) # to show the outliers
plt.title('The scatter plot for z_scores')
plt.show()


