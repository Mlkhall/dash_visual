import plotly.graph_objects as go
from numpy import array
from pandas import read_excel, to_numeric
from scipy.interpolate import interp1d
from plotly.subplots import make_subplots
from datetime import timedelta


def get_trend_fig(n=40):
    lab = read_excel('./lab.xlsx')[:-1]
    model = read_excel('./model.xlsx')

    lab = lab[:n]

    model = model[model.d >= lab.d.iloc[-1] - timedelta(hours=10)]

    liner_interp = interp1d(to_numeric(model.d), model.v, kind='linear')

    lab_time, model_vale_by_lab_time = lab.d,  liner_interp(to_numeric(lab.d))

    data = model_vale_by_lab_time - lab.v

    colors = array(['#1F5869', ] * len(lab_time))
    colors_model = array(["#33ffe6", ] * len(lab_time))
    colors_lab = array(["#ffd348", ] * len(lab_time))

    colors_lab[abs(data) > 3] = '#ff6e2e'
    colors_model[abs(data) > 3] = '#33ffe6'
    colors[abs(data) > 3] = '#ff2c6d'

    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.11,
        row_heights=[0.7, 0.3]
    )

    fig.add_trace(go.Scatter(x=lab.d.iloc[:n],
                             y=lab.v.iloc[:n],
                             mode='lines+markers',
                             name='ЛИМС',
                             marker=dict(symbol='circle',
                                         line_color=colors_lab,
                                         color=colors_lab,
                                         line_width=1,
                                         size=20),

                             line=dict(color='#ffd348', width=5)), row=1, col=1)

    fig.add_trace(go.Scatter(x=model.d,
                             y=model.v,
                             mode='lines',
                             name='Модель',
                             line=dict(color='#33ffe6', width=3)), row=1, col=1)

    fig.add_trace(go.Scatter(x=lab_time,
                             y=model_vale_by_lab_time,
                             showlegend=False,
                             name='Модель, ЛИМС',
                             mode='markers',
                             marker=dict(symbol='circle',
                                         line_color=colors_model,
                                         color=colors_model,
                                         line_width=5,
                                         opacity=0.5,
                                         size=15),
                             ), row=1, col=1)

    fig.add_trace(go.Bar(x=lab_time[:n], y=data,
                         name='Ошибка',
                         marker_color=colors,
                         ), row=2, col=1)

    fig.update_layout(
        legend_orientation="h",
        legend_yanchor="top",
        legend_y=1.12,
        legend=dict(traceorder='normal', bgcolor='#153F4C'),
        font_family="Courier New",
        font_color="#63A8A6",
        font_size=22,
        autosize=False,
        width=1190,
        height=875,
        margin=dict(r=0, l=0, t=10, b=0)
    )
    # #153F4C
    fig.update_xaxes(visible=True, gridcolor='#63A8A6', rangeslider_visible=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#63A8A6')
    fig.update_layout({'plot_bgcolor': '#153F4C', 'paper_bgcolor': '#153F4C'},
                      modebar_add=['togglespikelines', 'togglehover', 'v1hovermode'])

    return fig
