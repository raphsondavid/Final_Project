import plotly.plotly as py
from plotly.offline import download_plotlyjs,iplot
import plotly.graph_objs as go
import numpy as np

groups = ['Rent','Food','Bills','Miscellaneous']
amount = [1500,1000,1500,2000]
colors = ['#07fcf8','#FF0000','#33ff46','#f906fd']
trace = go.Pie(labels=groups, values = amount,
              hoverinfo='label+percent', textinfo = 'value',
              textfont=dict(size=25),
              marker = dict(colors=colors, line=dict(color='#000000', width=0.3)))
iplot([trace])
