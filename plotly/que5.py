import plotly.graph_objects as go
from plotly.subplots import make_subplots
time = [1, 2, 3, 4, 5]
team1_scores = [10, 15, 13, 17, 20]
team2_scores = [8, 12, 11, 14, 18]
fig = make_subplots(rows=1, cols=2, subplot_titles=('Team 1', 'Team 2'))
fig.add_trace(go.Scatter(x=time, y=team1_scores, mode='lines+markers', name='Team 1'), row=1, col=1)
fig.add_trace(go.Scatter(x=time, y=team2_scores, mode='lines+markers', name='Team 2'), row=1, col=2)
fig.update_layout(title='Performance Comparison of Two Teams Over Time',
                  xaxis_title='Time',
                  yaxis_title='Scores')
fig.show()
