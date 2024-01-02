import plotly.express as px
import pandas as pd

def generate_interactive_pie_chart(data, category_column, value_column, title):
    fig = px.pie(data, names=category_column, values=value_column, title=title, hole=0.3)
    return fig
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [30, 20, 25, 25]
}
df = pd.DataFrame(data)
pie_chart = generate_interactive_pie_chart(df, 'Category', 'Value', 'Distribution of Categories')
pie_chart.show()
