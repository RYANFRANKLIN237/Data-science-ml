import pandas as pd
import numpy as np

def analyze_customer_data(filename="Customers.csv"):
    try:
      df = pd.read_csv(filename)
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found. please ensure the file exists or run the data_generator.py script to create the file.")
      return
    df = df.drop(columns=["id", "name", "email"])
    correlation_matrix = df.corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

    print("\nInterpretation of Correlation Matrix:")
    print("The correlation matrix shows the relationships between age, balance, and income.")
    print("Values close to 1 indicate a strong positive correlation, values close to -1 indicate a strong negative correlation, and values close to 0 indicate a weak or no correlation.")
    print("Look for values that stand out to understand the relationships. For example:")
    print("- A positive correlation between age and income might suggest that older customers tend to have higher incomes.")
    print("- A negative correlation between balance and income might suggest that customers with higher incomes tend to have lower balances (perhaps because they spend more).")
    print("In this randomly generated dataset, it is unlikely to find strong correlations.")

if __name__ == "__main__":
  analyze_customer_data()