import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
file_path = r'D:\pandas\pandas\unsupervised2\CC GENERAL.csv'
df = pd.read_csv(file_path)
X = df.iloc[:, 1:] 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
imputer = SimpleImputer(strategy='mean')  # Replace NaN with mean value
X_imputed = imputer.fit_transform(X_scaled)
pca = PCA()
X_pca = pca.fit_transform(X_imputed)
explained_variance_ratio = pca.explained_variance_ratio_
plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, marker='o')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio by Principal Component')
plt.show()
