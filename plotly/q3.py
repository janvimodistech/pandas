import plotly.express as px
import pandas as pd
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14],
    'group': ['A', 'A', 'B', 'B', 'C']
}
df = pd.DataFrame(data)
fig = px.scatter(df, x='x', y='y', color='group', title='Scatter Plot with Multiple Groups')
fig.show()
