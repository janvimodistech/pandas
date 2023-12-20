import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
iris = load_iris()
X = iris.data  
y = iris.target  
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Performing  DBSCAN clustering
# The parameters eps and min_samples are important in DBSCAN:
# - eps: The maximum distance between two samples for one to be considered as in the neighborhood of the other.
# - min_samples: The number of samples (or total weight) in a neighborhood for a point to be considered as a core point.
dbscan = DBSCAN(eps=0.5, min_samples=5)  # You can adjust these parameters based on your dataset
clusters = dbscan.fit_predict(X_scaled)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', marker='o', edgecolor='black')
plt.xlabel('Feature 1 (Standardized)')
plt.ylabel('Feature 2 (Standardized)')
plt.title('DBSCAN Clustering (Iris Dataset)')
plt.show()
