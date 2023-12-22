import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("data_set_ALL_AML_train.csv")
numeric_columns = df.select_dtypes(include=['int64']).columns
df_numeric = df[numeric_columns]
scaler = StandardScaler()
X_std = scaler.fit_transform(df_numeric)
perplexity_values = [5, 30, 50]
for perplexity in perplexity_values:
    tsne = TSNE(n_components=2, perplexity=perplexity, random_state=42)
    X_tsne = tsne.fit_transform(X_std)
    plt.figure(figsize=(8, 8))
    plt.scatter(X_tsne[:, 0], X_tsne[:, 1], cmap='viridis', s=10)
    plt.title(f"t-SNE Visualization with Perplexity={perplexity}")
    plt.xlabel("t-SNE Component 1")
    plt.ylabel("t-SNE Component 2")
    plt.colorbar()
    plt.show()
