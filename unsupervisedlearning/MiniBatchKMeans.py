import pandas as pd
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import StandardScaler

def mini_batch_kmeans_clustering(data, n_clusters=8, batch_size=100, random_state=42):
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    kmeans = MiniBatchKMeans(n_clusters=n_clusters, batch_size=batch_size, random_state=random_state)
    kmeans.fit(data_scaled)
    data['cluster'] = kmeans.labels_
    return data

clustered_df = mini_batch_kmeans_clustering(data=df, n_clusters=5, batch_size=100, random_state=42)

# Print the first few rows of the clustered DataFrame
print(clustered_df.head())

