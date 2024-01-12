import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
# import statsmodels.api as sm

epa_data = pd.read_csv("google_data_analitics\\c4_epa_air_quality.csv", index_col = 0)

# First 10 rows of the data
print(epa_data.head(10))
print(epa_data.info())
print(epa_data.describe(include='all'))

# reseaching the population mean
population_mean = epa_data['aqi'].mean()

print(f'The population mean for aqi value is {round(population_mean, 4)}')

# SAMPLE WITH REPLACEMENT
# replace=True to specify sampling with replacement
# random_state - number for random seed
sampled_data = epa_data.sample(50, replace=True, random_state=42)

print(sampled_data.head(10))

# Compute the mean value from the aqi column in sample
sample_mean = sampled_data['aqi'].mean()

print(f'The sample mean for aqi value is {round(sample_mean, 4)}')

# APPLY THE CENTRAL LIMIT THEOREM TO THE WHOLE POPULATION
# Create an empty list and assign it to a variable called estimate_list
# Create a function for calculation and storing (collecting) 
# the mean values for all 10000 samples
estimate_list = []
for i in range(10000):
    estimate_list.append(epa_data['aqi'].sample(50, replace='True').mean())

# Create a new DataFrame from the list of 10,000 estimates for reseaching the means values
estimate_df = pd.DataFrame(data = {'estimate': estimate_list})

print(estimate_df.head(10))

# Compute the mean() of the sampling distribution 
# (for estimate_df, where we're storing the means for 10000 samples)
mean_sample_means = estimate_df['estimate'].mean()

print(f'The mean for aqi value of the sampling distribution is {mean_sample_means}')

# Calculate the standard error
standard_error = sampled_data['aqi'].std() / np.sqrt(len(sampled_data))

print(f'The standard error for sampled_data is {standard_error}')

# Output the distribution of these estimates using a histogram
plt.figure(figsize=(8, 5))
plt.hist(estimate_df['estimate'], color='orange', density=True, alpha=0.4, label = 'Histogram of sample means of 10000 random samples')
# ------------
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100) # generate a grid of 100 values from xmin to xmax.
p = stats.norm.pdf(x, population_mean, standard_error)
plt.plot(x, p, color='black', linewidth=2, label = 'Normal curve from central limit theorem')
plt.axvline(x=mean_sample_means, color='blue', linestyle = ':', linewidth=2, label = 'Mean of sample means of 10000 random samples')
# ------------
plt.xticks(np.arange(3, 12.5, step=0.5))
plt.legend(bbox_to_anchor=(1.01, 1))
plt.title('The sampling distribution')
plt.xlabel('The mean for aqi value of the sampling distribution')
plt.ylabel('Density')
plt.show()

# Results and evaluation
# Visualize the relationship between the sampling and normal distributions
plt.figure(figsize=(8,5))
plt.hist(estimate_df['estimate'], bins=25, density=True, alpha=0.4, label = "histogram of sample means of 10000 random samples")
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100) # generate a grid of 100 values from xmin to xmax.
p = stats.norm.pdf(x, population_mean, standard_error)
plt.plot(x, p, color='black', linewidth=2, label = 'normal curve from central limit theorem')
plt.axvline(x=population_mean, color='m', linestyle = 'solid', label = 'population mean')
plt.axvline(x=sample_mean, color='r', linestyle = '--', label = 'sample mean of the first random sample')
plt.axvline(x=mean_sample_means, color='b', linestyle = ':', label = 'mean of sample means of 10000 random samples')
plt.title("Sampling distribution of sample mean")
plt.xlabel('sample mean')
plt.ylabel('density')
plt.legend(bbox_to_anchor=(1.04,1))
plt.show()