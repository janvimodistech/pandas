import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# learn to Create a synthetic dataset for demonstration
np.random.seed(42)  
num_samples = 100
spending_scores = np.random.rand(num_samples) * 100  
annual_incomes = np.random.rand(num_samples) * 100000  
data = pd.DataFrame({'SpendingScore': spending_scores, 'AnnualIncome': annual_incomes})
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)
inertia = []
for n_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
data['Cluster'] = clusters
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', marker='o', edgecolor='black')
plt.xlabel('Spending Score (Standardized)')
plt.ylabel('Annual Income (Standardized)')
plt.title('K-Means Clustering')
plt.show()
print("Cluster Centers:")
print(scaler.inverse_transform(kmeans.cluster_centers_))
