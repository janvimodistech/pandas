import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.manifold import Isomap
digits = load_digits()
X = digits.data
y = digits.target
n_neighbors = 30
n_components = 2  
isomap = Isomap(n_neighbors=n_neighbors, n_components=n_components)
X_iso = isomap.fit_transform(X)
plt.figure(figsize=(10, 8))
plt.scatter(X_iso[:, 0], X_iso[:, 1], c=y, cmap=plt.cm.get_cmap('nipy_spectral', 10))
plt.colorbar(label='digit label', ticks=range(10))
plt.clim(-0.5, 9.5)
plt.title('Isomap projection of the digits dataset')
plt.show()
