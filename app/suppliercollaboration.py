import gradio as gr
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Load synthetic supplier data
supplier_data = pd.read_csv('supplier_data.csv')

# Feature engineering: Extracting features and target variables
X = supplier_data[['SupplierID']]
y_reliability = supplier_data['ReliabilityScore']
y_cost_effectiveness = supplier_data['CostEffectivenessScore']

# Initialize and train a linear regression model for reliability score
reliability_model = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

reliability_model.fit(X, y_reliability)

# Initialize and train a linear regression model for cost-effectiveness score
cost_effectiveness_model = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

cost_effectiveness_model.fit(X, y_cost_effectiveness)

# Function to simulate supplier collaboration and negotiation
def supplier_collaboration(supplier_id):
    reliability_score = reliability_model.predict([[supplier_id]])[0]
    cost_effectiveness_score = cost_effectiveness_model.predict([[supplier_id]])[0]

    # Simulating negotiation logic
    negotiated_reliability = min(1, reliability_score + 0.1)  # Cap reliability increase at 10%
    negotiated_cost_effectiveness = max(0, cost_effectiveness_score - 0.1)  # Reduce cost-effectiveness by 10%

    return f"Supplier ID: {supplier_id}\nNegotiated Reliability Score: {negotiated_reliability:.2f}\nNegotiated Cost-Effectiveness Score: {negotiated_cost_effectiveness:.2f}"

# Gradio Interface
iface_supplier_collaboration = gr.Interface(
    fn=supplier_collaboration,
    inputs="text",
    outputs="text",
    live=True,
    title="Supplier Collaboration Showcase"
)

# Launch the Gradio app
iface_supplier_collaboration.launch()
