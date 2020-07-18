# imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import datetime

# CSS file
css = ['main.css']

app = dash.Dash(__name__)

# Excel file to read
df = pd.read_excel('test.xlsx')

# preprocessing data
# locations = df['Wifi Id'].unique()#dates = [x for x in range(len(df['Date'].unique()))]

df['Date'] = df['Date'].astype('datetime64[ns]')
df = df.sort_values(by='Date')
locations = ['"Canteen"', '"Hostel"', '"CEP"', '"LAB"', '"RC"', '"LT"']
students = df['Student ID'].unique()
students.sort()
dates = df['Date'].dt.date.unique()
dates.astype('datetime64[ns]')
date_mark = {i: dates[i] for i in range(0, len(dates))}
for i in date_mark:
    date_mark[i] = date_mark[i].strftime('%m/%d/%Y')
    date_mark[i] = date_mark[i][0:5]
# Setting Graph Layout
layout = go.Layout(title='Overall Student Data',
                   hovermode='closest'
                   )
fig = go.Figure()


# HTML Component
app.layout = html.Div([

    html.H1("Student Movement Analysis"),
    html.Div([
        html.Label("Select Student:"),
        dcc.Dropdown(
            id='s-id',
            options=[{'label': i, 'value': i}
                     for i in students],
            value=''
        )
    ],
        style={'width': '20%', 'display': 'inline-block', 'padding': '5px'}),
    html.P([
        html.Label("Time Period"),
        dcc.Slider(
            id='slider',
            step=None,
            marks=date_mark,
            min=0,
            max=len(date_mark),
            value=0
        )
    ]),
    dcc.Graph(id='s-graph', figure=fig),

])

# Callbacks


@app.callback(
    Output('s-graph', 'figure'),
    [Input('s-id', 'value')]
)
def update_graph(sid):
    xdata = []
    cep = []
    lt = []
    lab = []
    hostel = []
    rc = []
    canteen = []

    # Fetch location data
    for i in students:
        xdata.append(i)

    # Fetch frequency data
    for i in students:
        cep.append(findFrequency('"CEP"', i))
        canteen.append(findFrequency('"Canteen"', i))
        rc.append(findFrequency('"RC"', i))
        hostel.append(findFrequency('"Hostel"', i))
        lt.append(findFrequency('"LT"', i))
        lab.append(findFrequency('"LAB"', i))

    # Make Plot

    #trace_1 = go.Bar(x=xdata, y=ydata,name='AAPL HIGH')

    lab = go.Scatter(x=xdata, y=lab, name='LAB',
                     line=dict(width=2, color='rgb(0, 0, 0)'))

    lt = go.Scatter(x=xdata, y=lt, name='LT', line=dict(
        width=2, color='rgb(0, 0, 200)'))

    rc = go.Scatter(x=xdata, y=rc, name='RC', line=dict(
        width=2, color='rgb(0, 200, 0)'))

    cep = go.Scatter(x=xdata, y=cep, name='CEP',
                     line=dict(width=2, color='rgb(200, 0, 0)'))

    hostel = go.Scatter(x=xdata, y=hostel, name='Hostel',
                        line=dict(width=2, color='rgb(200, 0, 200)'))

    canteen = go.Scatter(x=xdata, y=canteen, name='Canteen',
                         line=dict(width=2, color='rgb(200, 200, 0)'))

    fig = go.Figure(data=[lab, lt, rc, cep, hostel, canteen], layout=layout)
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
