import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv('datahw.csv')
fig = ff.create_distplot([data['Avg Rating'].tolist()],['rating'], show_hist = False)
fig.show()