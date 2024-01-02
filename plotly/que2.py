import plotly.express as px
import pandas as pd
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': [350, 420, 280, 390]
}
df = pd.DataFrame(data)
fig = px.bar(df, x='Product', y='Sales', title='Product Sales Comparison')
fig.update_layout(xaxis_title='Product', yaxis_title='Sales', template='plotly_dark')
fig.show()
