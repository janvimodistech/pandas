import plotly.express as px
import pandas as pd
import numpy as np
np.random.seed(0)
exam_scores = np.random.normal(70, 10, 100)
df = pd.DataFrame({'Scores': exam_scores})
fig = px.histogram(df, x='Scores', title='Distribution of Exam Scores')
fig.update_layout(xaxis_title='Scores', yaxis_title='Frequency')
fig.show()
