import gradio as gr
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# Load historical sales data
sales_data = pd.read_csv('historical_sales_data.csv')

# Feature engineering: Extracting features and target variable
X = sales_data[['ProductID', 'Region']]
y = sales_data['QuantitySold']

# Convert categorical variables to dummy/indicator variables
encoder = OneHotEncoder(drop='first')
X_encoded = encoder.fit_transform(X[['Region']])
X_encoded_df = pd.DataFrame(X_encoded.toarray(), columns=encoder.get_feature_names(['Region']))
X = pd.concat([X[['ProductID']], X_encoded_df], axis=1)

# Initialize and train a linear regression model
model = Pipeline([
    ('encoder', OneHotEncoder(drop='first')),
    ('regressor', LinearRegression())
])

model.fit(X, y)

# Function to calculate cost savings
def calculate_cost_savings(product_id, region, current_inventory, lead_time):
    # Predict quantity sold using the AI model
    input_data = pd.DataFrame({'ProductID': [product_id], 'Region': [region]})
    input_data_encoded = encoder.transform(input_data[['Region']])
    input_data_encoded_df = pd.DataFrame(input_data_encoded.toarray(), columns=encoder.get_feature_names(['Region']))
    input_data = pd.concat([input_data[['ProductID']], input_data_encoded_df], axis=1)
    predicted_quantity = int(model.predict(input_data)[0])

    # Calculate cost savings
    current_demand = predicted_quantity
    optimized_demand = int(model.predict(input_data)[0])
    holding_cost_current = current_inventory * 1  # Assuming holding cost per unit is 1
    holding_cost_optimized = min(current_inventory, optimized_demand * lead_time) * 1
    cost_savings = holding_cost_current - holding_cost_optimized

    return f"Cost Savings: ${cost_savings}"

# Gradio Interface
iface = gr.Interface(
    fn=calculate_cost_savings,
    inputs=["text", gr.Radio(['North', 'South', 'East', 'West'], label="Region"), "text", "text"],
    outputs="text",
    live=True,
    title="Inventory Management System"
)

# Launch the Gradio app
iface.launch()
