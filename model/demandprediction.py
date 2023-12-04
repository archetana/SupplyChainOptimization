import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load historical sales data
sales_data = pd.read_csv('historical_sales_data.csv')

# Feature engineering: Extracting features and target variable
X = sales_data[['ProductID', 'Region']]
y = sales_data['QuantitySold']

# Convert categorical variables to dummy/indicator variables
X = pd.get_dummies(X, columns=['Region'], drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Visualize predictions vs actual values
plt.scatter(y_test, predictions)
plt.xlabel('Actual Quantity Sold')
plt.ylabel('Predicted Quantity Sold')
plt.title('Actual vs Predicted Quantity Sold')
plt.show()
