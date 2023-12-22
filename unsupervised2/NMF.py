import numpy as np
from sklearn.decomposition import NMF
# Create a sample dataset (replace this with your own dataset)
# Here, we create a random 5x10 matrix with non-negative values
np.random.seed(0)
X = np.random.rand(5, 10)
# Specify the number of components for NMF
n_components = 3
# Create an instance of NMF with the specified number of components
nmf = NMF(n_components=n_components, init='random', random_state=0)
W = nmf.fit_transform(X)  # This represents the transformed data (basis components)
H = nmf.components_  # This represents the matrix of coefficients (encoding of original features)
print("Original data (X):")
print(X)
print("\nTransformed data (W):")
print(W)
print("\nMatrix of coefficients (H):")
print(H)
