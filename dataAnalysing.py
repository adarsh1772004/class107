import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv("107.csv")
s=df.groupby("level")["attempt"].mean()
graph=go.Figure(go.Bar(x=s,y=['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
graph.show()