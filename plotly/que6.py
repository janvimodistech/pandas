import plotly.express as px
import pandas as pd
import numpy as np
np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 10), columns=[f'Feature {i+1}' for i in range(10)])
corr_matrix = df.corr()
fig = px.imshow(corr_matrix,
                x=corr_matrix.columns,
                y=corr_matrix.index,
                color_continuous_scale='Viridis',
                title='Correlation Heatmap')
fig.update_layout(width=800, height=800)
fig.show()
