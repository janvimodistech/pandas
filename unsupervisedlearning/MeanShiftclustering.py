import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data  
y = iris.target  
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#  Mean Shift clustering
bandwidth = 1.0  # Bandwidth parameter
ms = MeanShift(bandwidth=bandwidth)
ms.fit(X_scaled)
#  cluster centers and labels
cluster_centers = ms.cluster_centers_
cluster_labels = ms.labels_

# Visualize the clusters (assuming 2D data)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=cluster_labels, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', color='red', s=100, label='Centers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Mean Shift Clustering')
plt.legend()
plt.show()
