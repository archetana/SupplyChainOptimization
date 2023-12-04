import gradio as gr
import pandas as pd
import numpy as np

# Load synthetic data for demonstration
sales_data = pd.read_csv('historical_sales_data.csv')
external_factors_data = pd.read_csv('external_factors_data.csv')
supplier_data = pd.read_csv('supplier_data.csv')

# Function to simulate real-time monitoring and generate alerts
def real_time_monitoring(product_id, region):
    # Simulate data retrieval based on product_id and region
    product_sales = sales_data[(sales_data['ProductID'] == int(product_id)) & (sales_data['Region'] == region)]
    external_factors = external_factors_data[external_factors_data['Date'] == pd.to_datetime('today').strftime('%Y-%m-%d')]
    supplier_info = supplier_data.sample()

    # Calculate key metrics
    total_sales = product_sales['QuantitySold'].sum()
    economic_indicator = external_factors['EconomicIndicator'].values[0]
    supplier_reliability = supplier_info['ReliabilityScore'].values[0]
    supplier_cost_effectiveness = supplier_info['CostEffectivenessScore'].values[0]

    # Define alert conditions
    alert_conditions = {
        'LowSales': total_sales < 50,
        'HighEconomicIndicator': economic_indicator > 1.2,
        'LowSupplierReliability': supplier_reliability < 0.8,
        'HighSupplierCost': supplier_cost_effectiveness < 0.5
    }

    # Generate alerts based on conditions
    alerts = {key: "Alert!" for key, condition in alert_conditions.items() if condition}

    # Build dashboard display
    dashboard_display = f"""
    <h2>Real-Time Monitoring Dashboard</h2>
    <p>Product ID: {product_id}</p>
    <p>Region: {region}</p>
    <p>Total Sales: {total_sales}</p>
    <p>Economic Indicator: {economic_indicator}</p>
    <p>Supplier Reliability: {supplier_reliability}</p>
    <p>Supplier Cost Effectiveness: {supplier_cost_effectiveness}</p>
    <h3>Alerts</h3>
    <ul>
    """

    # Add alerts to display
    for alert, message in alerts.items():
        dashboard_display += f"<li>{alert}: {message}</li>"

    dashboard_display += "</ul>"

    return dashboard_display

# Gradio Interface
iface_real_time_monitoring = gr.Interface(
    fn=real_time_monitoring,
    inputs=["text", gr.Radio(['North', 'South', 'East', 'West'], label="Region")],
    outputs=gr.Textbox(),
    live=True,
    title="Real-Time Monitoring Dashboard"
)

# Launch the Gradio app
iface_real_time_monitoring.launch()
