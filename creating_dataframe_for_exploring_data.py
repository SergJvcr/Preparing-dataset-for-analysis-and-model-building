import pandas as pd

df = pd.read_csv('google_data_analitics\\2017_Yellow_Taxi_Trip_Data.csv')

# View and inspect summary information about the dataframe:
print(df.head(10))
print(df.info())
print(df.describe())

# Investigate the variables:
# Sort the data by trip distance from maximum to minimum value
trip_distance_max_to_min = df.sort_values(by=['trip_distance'], ascending=False)
print(trip_distance_max_to_min)

# Sort the data by total amount and print the top 20 values
sort_max_total_amount = df['total_amount'].sort_values(ascending=False)
print(sort_max_total_amount.head(20))

# Sort the data by total amount and print the bottom 20 values
sort_min_total_amount = df['total_amount'].sort_values(ascending=True)
sort_min_total_amount.head(20)
# or we can write it like this:
print(sort_max_total_amount.tail(20))

# How many of each payment type are represented in the data?
print(df['payment_type'].value_counts())
# According to the data dictionary, the payment method was encoded as follows:
# 1 = Credit card
# 2 = Cash
# 3 = No charge
# 4 = Dispute

# What is the average tip for trips paid for with credit card?
mask_1 = df['payment_type'] == 1
credit_card_payment = df[mask_1]['tip_amount'].mean()
print('tip amount for credit cards:', credit_card_payment)

# What is the average tip for trips paid for with cash?
mask_2 = df['payment_type'] == 2
cash_payment = df[mask_2]['tip_amount'].mean()
print('tip amount for cash:', cash_payment)

# How many times is each vendor ID represented in the data?
print(df['VendorID'].value_counts())

# What is the mean total amount for each vendor?
mask_3 = df['VendorID'] == 1
vendor_1_mean_total_amount = df[mask_3]['total_amount'].mean()
print('the mean for total amount for vendor 1:', vendor_1_mean_total_amount)

mask_4 = df['VendorID'] == 2
vendor_2_mean_total_amount = df[mask_4]['total_amount'].mean()
print('the mean for total amount for vendor 2:', vendor_2_mean_total_amount)
# or we can do it like this:
print(df.groupby(['VendorID']).mean()[['total_amount']])

# Filter the data for credit card payments only
mask_5 = df['payment_type'] == 1
credit_card_payment = df[mask_5]
# Filter the data for passenger count only
print(credit_card_payment['passenger_count'].value_counts())

# Calculate the average tip amount for each passenger count (credit card payments only)
print(df.groupby(['passenger_count']).mean()[['tip_amount']])


# ----------------------------------------------------------------------------
# To show the key features and sorting them by total_amount
sort_max_total_amount_ = df.sort_values(by=['total_amount'], ascending=False)
sort_max_total_amount_[['Unnamed: 0', 'trip_distance', 'total_amount']].head(20)