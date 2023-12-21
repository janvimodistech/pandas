import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.manifold import LocallyLinearEmbedding
data = load_iris()
X = data.data  
y = data.target  
n_neighbors = 10  # Number of neighbors to consider for each point
n_components = 2  # Number of components for dimensionality reduction
lle = LocallyLinearEmbedding(n_neighbors=n_neighbors, n_components=n_components, random_state=42)
X_lle = lle.fit_transform(X)
plt.scatter(X_lle[:, 0], X_lle[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.colorbar()
plt.title('Locally Linear Embedding (LLE) Visualization of Iris Dataset')
plt.xlabel('LLE Component 1')
plt.ylabel('LLE Component 2')
plt.show()
