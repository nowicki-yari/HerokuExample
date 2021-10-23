import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
pd.options.plotting.backend = "plotly"

df = pd.read_csv('weather.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H2('Weather App prototype'),
    dcc.Dropdown(
        id='dropdown-time',
        options=[{'label': i, 'value': i} for i in ['9am', '3pm']],
        value='9am'
    ),
    dcc.Graph(id='display-value')
])


@app.callback(dash.dependencies.Output('display-value', 'figure'),
                [dash.dependencies.Input('dropdown-time', 'value')])
def display_value(value):
    df_filtered = df.filter(regex='{}$'.format(value), axis=1)
    df_filtered = df_filtered.drop(['WindDir{}'.format(value)], axis=1)
    print(df_filtered)
    fig = px.line(df_filtered)
    fig.update_layout()
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
