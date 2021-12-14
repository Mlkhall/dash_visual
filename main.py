import plotly.express as px
from dash import Dash
import copy
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

from plot_of_dash import get_trend_fig

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
app.title = 'МКС: Аналитика'

app.layout = html.Div([

    html.H1("АНАЛИТКА РАБОТЫ МОДЕЛЕЙ МКС", className='app-head-title'),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.H1("Инструмент для визуализации работы моделей", className='text-properties'),
                html.Label('Выберите модель', className='label-dropdown'),
                html.Div(
                    dcc.Dropdown(
                        options=[
                            {'label': 'Модель 1', 'value': '1'},
                            {'label': 'Модель 2', 'value': '2'},
                            {'label': 'Модель 3', 'value': '3'},
                            {'label': 'Модель 4', 'value': '4'},
                            {'label': 'Модель 5', 'value': '5'},
                            {'label': 'Модель 6', 'value': '6'}
                        ],
                        value='1',
                    ), className='dropdown-model'),
                html.Div([
                    html.Label('Число точек лаборатории для анализа', className='slider-label'),

                    dbc.Pagination(id="pagination",
                                   min_value=5,
                                   max_value=50,
                                   step=5,
                                   active_page=5,
                                   className='pagination-style'),
                ])
            ]),
            width=3,
            className='model-analyst',
        ),
        dbc.Col([
            html.Div([
                dcc.Graph(

                    id='models-lines',
                    figure=get_trend_fig(n=5)
                    # style={'display': 'none'}
                ),
            ], style={'margin-left': 0, 'margin-top': 10, 'overflowY': 'scroll'}),
        ],
            width=8,
            style={"height": "85.8vh", "background-color": "#153F4C", 'margin-left': 45},

        ),

    ], style={"height": "32.2vh"}),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.H1(className='metric-value-style', id='R'),
                html.H6("Корреляция", className='metric-correlation-style'),
            ]),
            width={"size": 2, 'order': 2},
            className='metric-value-col-style'
        ),
        dbc.Col(
            html.P("R", className='metric-style'),
            width={"size": 1, 'order': 1},
            className="metric-col-style"
        ),
    ], style={"height": "15vh"}),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.H1("123,23", className='metric-value-style'),
                html.H6("Среднеквадратическое отклонение", className='metric-correlation-style'),
            ]),
            width={"size": 2, 'order': 2},
            className='metric-value-col-style'
        ),
        dbc.Col(
            html.P("S", className='metric-style'),
            width={"size": 1, 'order': 1},
            className="metric-col-style",
        ),
    ], style={"height": "15vh", 'margin-top': 30}),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.H1("23,23", className='metric-value-style'),
                html.H6("Детерминация", className='metric-correlation-style'),
            ]),
            width={"size": 2, 'order': 2},
            className='metric-value-col-style'
        ),
        dbc.Col(
            html.P("D", className='metric-style'),
            width={"size": 1, 'order': 1},
            className="metric-col-style",
        ),
    ], style={"height": "15vh", 'margin-top': 30})

])


@app.callback(
    Output("models-lines", "figure"), [Input("pagination", "active_page")]
)
def change_active_page(value):
    if value is None:
        pass
    else:
        return get_trend_fig(n=value)


@app.callback(
    Output("R", "children"), [Input("pagination", "active_page")]
)
def change_corr_value(value):
    return value


# Run app and display result inline in the notebook
if __name__ == '__main__':
    app.run_server(debug=True)
