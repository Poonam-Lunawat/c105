# calculate mean

import csv
import pandas as pd
import plotly_express as px 

with open("data1.csv") as f:
    reader=csv.reader(f)
    filedata=list(reader) 

filedata.pop(0)
total_marks=0
n= len(filedata)
for marks in filedata:
    total_marks += float(marks[1])

mean= total_marks/n
print(mean)

df=pd.read_csv("data1.csv")
fig=px.scatter(df, x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(type="line",y0=mean, y1=mean,x0=0,x1=n)])
fig.update_yaxes(rangemode="tozero")
fig.show()