import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

file_path = ''  
df = pd.read_csv(file_path)

num_components_list = [10, 50, 100]


fig, axes = plt.subplots(1, len(num_components_list), figsize=(15, 5))

for i, n_components in enumerate(num_components_list):
   
    pca = PCA(n_components=n_components, random_state=42)
    pca.fit(df)
    X_pca = pca.transform(df)
    axes[i].scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.5)
    axes[i].set_title(f'PCA with {n_components} components')
    axes[i].set_xlabel('Principal Component 1')
    axes[i].set_ylabel('Principal Component 2')

plt.tight_layout()
plt.show()
