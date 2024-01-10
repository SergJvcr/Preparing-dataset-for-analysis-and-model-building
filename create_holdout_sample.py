import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('google_data_analitics\\marketing_sales_data_2.csv')
print(data.head(5))

# Subset X and y variables
penguins_X = data[['Radio', 'TV']]
penguins_y = data[['Sales']]

# Create training data sets and holdout (testing) data sets
X_train, X_test, y_train, y_test = train_test_split(penguins_X, penguins_y, test_size = 0.3, random_state = 42)

# That's all!
# We have set the test_size variable to 0.3, which tells the function what proportion of the data 
# should be in the holdout sample. Additionally, we have set the random_state variable equal to 42 for reproducibility. 
# If you change the random_state, your holdout sample and training data sets will be different, so your model may perform differently

# When you will create a model, the OLS dataframe must be building like this:
# ols_data = pd.concat([X_train, y_train], axis = 1)

# TEST DATASETS WE CAN YOU FOR TESTING OUR MODEL IF IT HAS OVERFITTING OR UNDERFITTING (HOW PRECISELY IS OUR MODEL?)
