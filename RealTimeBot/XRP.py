from gettext import npgettext
from turtle import width
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import Data as dt
import Indicators as i
import TradingLogic as tl

app = Dash(__name__)

app.layout = html.Div([
    
    dcc.Graph(id="fig"),
    
    
    dcc.Interval(id="interval", interval =20000)

    ])

@app.callback(
    Output("fig", "figure"),    
    Input("interval", "n_intervals")
    
        )

def update_figure(n_intervals):
    
    inst_data1= dt.get_instrument_data("XRP-USDT", "30m", 100)
    inst_data2= dt.get_instrument_data("XRP-USDT", "5m", 300)
    
    
    macd_values = i.get_macd_values(inst_data1)
    stoch_values = i.get_stoch_values(inst_data2)
    ema_values=i.get_ema_values(inst_data1, 26)
    
    fig = make_subplots(rows=2,cols=2, shared_xaxes=True,  vertical_spacing=0.01, row_heights=[0.8, 0.2])
    
    macd_trace = go.Scatter(y = macd_values[0][0], x = inst_data1['time'], line=dict(color='dodgerblue', width=1))
    macdsignal_trace = go.Scatter(y = macd_values[0][1], x = inst_data1['time'], line=dict(color='orange', width=1))
    hist_trace = go.Bar(x = inst_data1['time'], y = macd_values[0][2])

 
    stochfast_trace = go.Scatter(y= stoch_values[0], x=inst_data2['time'],line=dict(color='dodgerblue', width=1))
    stochslow_trace = go.Scatter(y= stoch_values[1], x=inst_data2['time'], line=dict(color='orange', width=1))

    ema_trace = go.Scatter(x=inst_data1['time'], y=ema_values[0])


    fig.add_trace(ema_trace, row =1, col =1)


    fig.add_trace(hist_trace, row=2, col=1)
    fig.add_trace(macd_trace, row=2, col=1)
    fig.add_trace(macdsignal_trace, row=2, col=1)


    fig.add_trace(stochslow_trace, row=2, col=2)
    fig.add_trace(stochfast_trace, row=2, col=2)
    fig.add_hline(y=70, row=2, col=2, line_width=0.8, line_dash="dash", line_color="red")
    fig.add_hline(y=30, row=2, col=2, line_width=0.8, line_dash="dash", line_color="red")
    
    inst1= fig.add_trace(go.Ohlc(x=inst_data1['time'],
            open=inst_data1['open'],
            high=inst_data1['high'],
                    low=inst_data1['low'],
                    close=inst_data1['close']
                    ), row=1, col=1).update_traces(line_width=0.8, 
                      selector=dict(
                          type='ohlc'
                          )
                      )
                    

    inst2=fig.add_trace(go.Ohlc(x=inst_data2['time'],
            open=inst_data2['open'],
            high=inst_data2['high'],
                    low=inst_data2['low'],
                    close=inst_data2['close']
                    ), row=1, col=2).update_traces(line_width=0.8, 
                      selector=dict(
                          type='ohlc'
                          )
                      )
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=False
                )
            ),
        xaxis2=dict(
            rangeslider=dict(
                visible=False
                )
            ), height=700
        )
    tl.get_short_entry(macd_values,ema_values,stoch_values,inst_data2, fig, go, "XRP SHORT")
    tl.get_long_entry(macd_values,ema_values,stoch_values,inst_data2, fig, go, "XRP LONG")
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8056)


