import plotly.graph_objects as go
import pandas as pd
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 11, 12, 13, 14]
}
df = pd.DataFrame(data)
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['X'],
    y=df['Y'],
    mode='markers',  
    marker=dict(color='blue', size=10),  
    name='Data' 
))
fig.update_layout(title='Interactive Scatter Plot', xaxis_title='X-axis', yaxis_title='Y-axis', template='plotly_dark')
fig.show()
