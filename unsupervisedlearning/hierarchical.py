import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
iris = load_iris()
X = iris.data  
y = iris.target  # Target (not used for clustering, only for visualization)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
agg_cluster = AgglomerativeClustering(n_clusters=3, linkage='ward', affinity='euclidean')
clusters = agg_cluster.fit_predict(X_scaled)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', marker='o', edgecolor='black')
plt.xlabel('Feature 1 (Standardized)')
plt.ylabel('Feature 2 (Standardized)')
plt.title('Hierarchical Clustering (Iris Dataset)')
plt.show()
