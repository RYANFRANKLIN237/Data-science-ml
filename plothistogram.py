import pandas as pd
import matplotlib.pyplot as plt

# 1. Construct Table1 and Table2
data1 = {'city': ['Muea', 'Molyko', 'Malingo'], 'humidity': [65, 68, 71]}
table1 = pd.DataFrame(data1)

data2 = {'city': ['Molyko', 'Muea'], 'temperature': [21, 14], 'humidity': [68, 65]}
table2 = pd.DataFrame(data2)

print("Table 1:\n", table1)
print("\nTable 2:\n", table2)

# 2. Outer Join
df = pd.merge(table1, table2, on='city', how='outer', suffixes=('_table1', '_table2'))
print("\nOuter Join (df):\n", df)

# 3. Set index, drop empty rows
df2 = df.set_index('city')
df2 = df2.dropna()  # Drop rows with NaN values
print("\nDataFrame with Index and Dropped NaNs (df2):\n", df2)

# 4. Interpolation and Plotting
df = df.set_index('city') #set the index for interpolation
df_interpolated = df.interpolate()
print("\nDataFrame with Interpolated Values (df_interpolated):\n", df_interpolated)

plt.figure(figsize=(10, 6))  # Adjust figure size for better visualization
plt.plot(df_interpolated.index, df_interpolated['humidity_table1'], marker='o', label='Humidity Table 1')
plt.plot(df_interpolated.index, df_interpolated['humidity_table2'], marker='x', label='Humidity Table 2')
plt.plot(df_interpolated.index, df_interpolated['temperature'], marker='s', label='Temperature')


plt.xlabel("City")
plt.ylabel("Value")
plt.title("Temperature and Humidity Across Cities (Interpolated)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45, ha='right') #rotate x axis labels for readability if needed
plt.tight_layout() #adjust layout to prevent labels from overlapping
plt.show()

# 5. Histograms
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.hist(df_interpolated['temperature'], bins=5, edgecolor='black') #Added bins and edgecolor for better visualization
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Histogram of Temperature")

plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
plt.hist(df_interpolated['humidity_table1'], bins=5, edgecolor='black') #Added bins and edgecolor for better visualization
plt.xlabel("Humidity")
plt.ylabel("Frequency")
plt.title("Histogram of Humidity")

plt.tight_layout()
plt.show()