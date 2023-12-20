import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data = pd.read_csv('StudentsPerformance.csv')
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data = pd.read_csv('StudentsPerformance.csv')
numeric_columns = ['math score', 'reading score', 'writing score']
X = data[numeric_columns]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
agglomerative_cluster = AgglomerativeClustering(n_clusters=3, linkage='ward')
clusters = agglomerative_cluster.fit_predict(X_scaled)
print(clusters)

