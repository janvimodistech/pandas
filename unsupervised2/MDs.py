import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.manifold import MDS
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset from Scikit-Learn
iris = datasets.load_iris()
X = iris.data  # Features
y = iris.target  # Target (class labels)

# Preprocess the data if necessary (e.g., standardize the features)
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Create an MDS model with the desired number of dimensions (e.g., 2 for 2D visualization)
mds = MDS(n_components=2, random_state=42)

# Fit the MDS model to your data and transform it to the lower-dimensional space
X_mds = mds.fit_transform(X_std)

# Visualize the MDS result
plt.figure(figsize=(8, 6))
for i, target_name in enumerate(iris.target_names):
    plt.scatter(X_mds[y == i, 0], X_mds[y == i, 1], label=target_name)
plt.title('MDS Visualization of Iris Dataset')
plt.xlabel('MDS Component 1')
plt.ylabel('MDS Component 2')
plt.legend()
plt.show()
