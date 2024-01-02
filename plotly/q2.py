import plotly.express as px
import pandas as pd
data = {
    'category': ['A', 'B', 'C', 'D'],
    'values': [10, 20, 15, 25]
}
df = pd.DataFrame(data)
fig = px.bar(df, x='category', y='values', title='Bar Plot')
fig.show()
