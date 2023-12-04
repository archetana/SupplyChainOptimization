import pandas as pd
import numpy as np

def generate_clean_data():
    # Generating synthetic sales data
    np.random.seed(42)
    start_date = pd.to_datetime('2019-01-01')
    end_date = pd.to_datetime('2022-12-31')
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')

    sales_data = pd.DataFrame({
        'Date': date_range,
        'ProductID': np.random.randint(1, 101, size=len(date_range)),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], size=len(date_range)),
        'QuantitySold': np.random.randint(10, 100, size=len(date_range))
    })

    # Generating synthetic external factors data
    external_factors_data = pd.DataFrame({
        'Date': date_range,
        'EconomicIndicator': np.random.uniform(0.8, 1.2, size=len(date_range)),
        'WeatherImpact': np.random.uniform(0.5, 1.5, size=len(date_range))
    })

    # Generating synthetic supplier data
    supplier_data = pd.DataFrame({
        'SupplierID': np.arange(1, 51),
        'SupplierName': [f'Supplier_{i}' for i in range(1, 51)],
        'ReliabilityScore': np.random.uniform(0.7, 1.0, size=50),
        'CostEffectivenessScore': np.random.uniform(0.5, 1.0, size=50)
    })

    # Save to CSV
    sales_data.to_csv('historical_sales_data.csv', index=False)
    external_factors_data.to_csv('external_factors_data.csv', index=False)
    supplier_data.to_csv('supplier_data.csv', index=False)

    return sales_data, external_factors_data, supplier_data

def main():
    sales_data, external_factors_data, supplier_data = generate_clean_data()

    # Displaying the first few rows of each generated dataset
    print("Historical Sales Data:")
    print(sales_data.head())

    print("\nExternal Factors Data:")
    print(external_factors_data.head())

    print("\nSupplier Data:")
    print(supplier_data.head())

if __name__ == "__main__":
    main()
