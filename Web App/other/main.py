import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=css)

df = pd.read_excel('test.xlsx')
df['Date'] = df['Date'].astype('datetime64[ns]')
df = df.sort_values(by='Date')

#locations = df['Wifi Id'].unique()
locations = ['"Canteen"', '"Hostel"', '"CEP"', '"LAB"', '"RC"', '"LT"']
students = df['Student ID'].unique()
dates = df['Date'].dt.date.unique()
dates.astype('datetime64[ns]')


#dates = [x for x in range(len(df['Date'].unique()))]

print(type(dates))

app.layout = html.Div([

    html.Div([
        html.Label("Select Location:"),
        dcc.Dropdown(
            id='l-id',
            options=[{'label': i, 'value': i}
                     for i in locations],
            value=''
        )
    ],
        style={'width': '30%', 'display': 'inline-block', 'padding': '5px'}),


    html.Div([
        html.Label("Select Student:"),
        dcc.Dropdown(
            id='s-id',
            options=[{'label': i, 'value': i}
                     for i in students],
            value=''
        )
    ],
        style={'width': '30%', 'display': 'inline-block', 'padding': '5px'}),

    html.Div([
        html.Label("Select Date:"),
        dcc.Dropdown(
            id='d-id',
            options=[{'label': i, 'value': i}
                     for i in dates],
            value=''
        )
    ],
        style={'width': '30%', 'display': 'inline-block', 'padding': '5px'}),
    html.Div(id='output'),
    html.Br(),
    dcc.Graph(id='s-graph')
])


@app.callback(
    Output('s-graph', 'figure'),
    [Input('l-id', 'value'),
     Input('s-id', 'value'),
     Input('d-id', 'value')]
)
def update_graph(lid, sid, did):

    return {
        'data': [dict(x=[lid],
                      y=[findFrequency(lid,sid,did)])],
        'layout': dict()
    }


def findFrequency(lid, sid, did):
    dff = df
    fl = dff.loc[dff['Wifi Id'] == lid]
    fl = fl.loc[fl['Student ID'] == sid]
    fl = fl.loc[fl['Date'].dt.date == pd.to_datetime(did)]
    print(fl.info)
    freq = fl.index
    freq = len(freq)
    return (freq)


if __name__ == '__main__':
    app.run_server(debug=True)

    # dcc.Slider(
    #   id='date-slider',
    #  min=df['Date'].dt.date.min(),
    # max = df['Date'].dt.date.max(),
    # value=df['Date'].dt.date.max(),
    #  marks ={str(date):str(date) for date in df['Date'].dt.date.unique()},
    # step=None
    # )
