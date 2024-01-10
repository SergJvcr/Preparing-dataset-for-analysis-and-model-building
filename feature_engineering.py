import pandas as pd

data = pd.read_csv('google_data_analitics\\nba-players.csv', index_col=0)

# Data exploration
print(data.head(10))
print(f'Our data contains {data.shape[0]} rows and {data.shape[1]} columns.')
print(data.info())
print(data.describe(include='all'))
print(data.columns) # display all column names

# Check for missing values
print(data.isna().sum())

# Statistical tests
# Display percentage (%) of values for each class (1, 0) represented in the target column of this dataset
print(data['target_5yrs'].value_counts(normalize=True) * 100) # if 89% - 11% - this is OK

# Feature selection
# Select the columns to proceed with include the target column, `target_5yrs`.
selected_data = data.drop(['name', 'fgm', 'fga', '3p_made', '3pa', 'ftm', 'fta', 'oreb', 'dreb'], axis=1)
# Display the first few rows
print(selected_data.head(10))

# Feature transformation 
# Dummy encode categorical variables - if we want to convert categorical data to numerical data
# data = pd.get_dummies(data, drop_first=True)

# Feature extraction
# Extract two features that would help predict target_5yrs
# Create a new variable named `extracted_data`
extracted_data = selected_data.copy()
# Add a new column named `total_points` and
# calculate total points earned by multiplying the number of games played by the average number of points earned per game
extracted_data['total_points'] = extracted_data['gp'] * extracted_data['pts']
# Add a new column named `efficiency`. Calculate efficiency by dividing the total points earned by the total number 
# of minutes played, which yields points per minute. (Note that `min` represents avg. minutes per game.)
extracted_data['efficiency'] = extracted_data['total_points'] / (extracted_data['min'] * extracted_data['gp'])

print(extracted_data.head(10))

# Remove any columns from `extracted_data` that are no longer needed
extracted_data = extracted_data.drop(['gp', 'pts', 'min'], axis=1)
# Display the first few rows of `extracted_data` to ensure that column drops took place
print(extracted_data.head(5))

# Export the extracted data
extracted_data.to_csv('extracted_nba_players_data.csv', index=0)