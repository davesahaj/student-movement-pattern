# imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# CSS file
css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=css)

# Excel file to read
df = pd.read_excel('test.xlsx')

# preprocessing data
# locations = df['Wifi Id'].unique()#dates = [x for x in range(len(df['Date'].unique()))]

df['Date'] = df['Date'].astype('datetime64[ns]')
df = df.sort_values(by='Date')
locations = ['"Canteen"', '"Hostel"', '"CEP"', '"LAB"', '"RC"', '"LT"']
students = df['Student ID'].unique()
students.sort()
students_mark = {i+1: str(students[i]) for i in range(0, len(students))}
dates = df['Date'].dt.date.unique()
dates.astype('datetime64[ns]')


fig = go.Figure()


# HTML Component
app.layout = html.Div([

    html.H1("Student Movement Analysis"),

    dcc.Graph(id='s-graph', figure=fig, animate=False),

    html.P([
        html.Label("Student ID"),
        dcc.Slider(
            id='s-id',
            step=1,
            marks=students_mark,
            min=1,
            max=len(students_mark),
            value=1,

        )
    ])
])

# Callbacks


@app.callback(
    Output('s-graph', 'figure'),
    [Input('s-id', 'value')]
)
def update_graph(sid):
    xdata = []
    ydata = []

    # Fetch location data
    for i in locations:
        xdata.append(i)

    # Fetch frequency data
    for i in locations:
        ydata.append(findFrequency(i, sid))

    # Make Plot
    # https://plotly.com/python/reference/#scatter-marker

   # trace_1 = go.Bar(x=xdata, y=ydata,name='Frequency', opacity=0.7)
    
    trace_2 = go.Scatter(showlegend=False,
                         mode="markers+lines",
                         x=xdata,
                         y=ydata,
                         name='',
                         line=dict(shape='spline', smoothing=0.8, width=2,
                                   color='rgb(0, 200, 200)'))

    # Setting Graph Layout
    layout = dict(
        xaxis={'title': 'Wifi Locations'},
        yaxis={'title': 'Frequency','range':[0,480]},
        title='Student Wise Frequency',
        hovermode='closest',
        plot_bgcolor='#ddd',
        paper_bgcolor='#eee',
        autosize=True,
        transition={'duration': 300,'easing': 'cubic-in-out'}
    )

    fig = go.Figure(data=[trace_2], layout=layout)


    return fig


def findFrequency(lid, sid):
    dff = df
    fl = dff.loc[dff['Wifi Id'] == lid]
    fl = fl.loc[fl['Student ID'] == sid]
   # print(fl.info)
    freq = fl.index
    freq = len(freq)
    return (freq)


if __name__ == '__main__':
    app.run_server(debug=True)
