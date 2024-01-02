import plotly.graph_objects as go
import pandas as pd
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [25, 24, 23, 22, 26, 27, 28]
fig = go.Figure()
fig.add_trace(go.Scatter(x=days, y=temperatures, mode='lines+markers', name='Temperature'))
fig.update_layout(title='Weekly Temperature Trend',
                  xaxis_title='Day of the Week',
                  yaxis_title='Temperature (°C)',
                  template='plotly_dark')
fig.show()
