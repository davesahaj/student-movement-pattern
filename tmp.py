import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_excel("test.xlsx")
#df = df.loc[df['Student ID'] == 6]
df = df.loc[df['Wifi Id'] == '"Hostel"']
df['Date'] = df['Date'].astype('datetime64[ns]')
df = df.loc[(df['Date'].dt.day == 9)]
df = df.groupby('Student ID', as_index=False).count()


app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input', value='Enter something here!', type='text'),
    html.Div(id='output'),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df['Student ID'],
                    y=df['Date'],
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    }
                )
            ]
        }
    )
])


@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    return 'Input: "{}"'.format(input_data)

if __name__ == '__main__':
    app.run_server(debug=True)
