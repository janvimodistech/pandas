import plotly.graph_objects as go
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
fig.update_layout(title='Simple Line Plot', xaxis_title='X Axis', yaxis_title='Y Axis')
fig.show()
