import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Using all four features for clustering

# Compute Sum of Squared Errors (SSE) for different values of K
sse = []
k_values = range(1, 21)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)  # Inertia is the SSE

# Compute the second derivative (rate of change of SSE)
sse_diff = np.diff(sse)  # First derivative
sse_diff2 = np.diff(sse_diff)  # Second derivative

# The optimal K is typically where the second derivative is minimal (largest drop in SSE)
optimal_k = np.argmin(sse_diff2) + 2  # +2 because second derivative reduces dimension by 2

# Print the optimal K
print(f"Optimal number of clusters (K) based on the elbow method: {optimal_k}")    

# Plot SSE against K
plt.figure(figsize=(8, 6))
plt.plot(k_values, sse, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Sum of Squared Errors (SSE)')
plt.title('Elbow Method for Optimal K')
plt.xticks(range(1, 21))
plt.grid(True)
plt.show()

# The optimal K is typically at the 'elbow' of the curve
