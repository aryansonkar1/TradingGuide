import plotly.graph_objects as go
import datetime
import dateutil
import pandas_ta as pta

def pplotly_table(DataFrame):
    headerColor = "Grey"
    RowEvenColor = "#FAF8F8"
    RowOddColor = "#E6EAEE"
    fig = go.Figure(data=[go.Table(
    header = dict(
        values = ["<b>"+str(i)[:10]+"</b>" for i in DataFrame.columns],
        line_color = "#F9F1F0",fill_color = "#222D39",
        align="center",font=dict(color='White',size=15),height=35
        ),
        cells = dict(
            values=[DataFrame[col].astype(str) for col in DataFrame.columns],
            line_color="#F9F1F0",
            fill_color=[[RowEvenColor, RowOddColor] * (len(DataFrame)//2 + 1)],
            align="center",
            font=dict(color="black", size=12),
            height=28
        ))
    ])
    fig.update_layout(height = 290,margin = dict(l=0,r=0,t=0,b=0))  
    return fig

def filter_data(dataFrame,num_period):
    if num_period=='1mo':
        date = dataFrame.index[-1] + dateutil.relativedelta.relativedelta(months=-1)
    elif num_period =='5d':
        date = dataFrame.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
    elif num_period =='6mo':
        date = dataFrame.index[-1] + dateutil.relativedelta.relativedelta(months=-6)
    elif num_period =='1y':
        date = dataFrame.index[-1] + dateutil.relativedelta.relativedelta(years=-1)
    elif num_period =='5y':
        date = dataFrame.index[-1] + dateutil.relativedelta.relativedelta(years=-5)
    elif num_period =='ytd':
        date = datetime.datetime(dataFrame.index[-1].year,1,1)
    else:
        date = dataFrame.index[0]

    return dataFrame.reset_index()[dataFrame.reset_index()['Date']>date]


def close_chart(dataframe,num_period=False):
    if num_period:
        dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    # fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['Open'],mode='lines',name='Open',line=dict(width=2,color='#5ab7ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['Close'],mode='lines',name='Close',line=dict(width=2,color='black')))
    # fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['High'],mode='lines',name='High',line=dict(width=2,color="#0078ff")))
    # fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['Low'],mode='lines',name='Low',line=dict(width=2,color='red')))
    
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(showlegend=True)
    fig.update_layout(height=500,margin=dict(l=0,r=0,t=0,b=0),plot_bgcolor='white',paper_bgcolor='#e1efff',legend=dict(yanchor="top",xanchor="right"))
    return fig


def candlestick(dataframe,num_period):
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=dataframe['Date'],open=dataframe['Open'],high=dataframe['High'],low=dataframe['Low'],close=dataframe['Close']))
    fig.update_layout(showlegend=False,height=500,margin=dict(l=0,r=0,t=0,b=0),plot_bgcolor='white',paper_bgcolor='#e1efff')
    return fig

def RSI(dataframe,num_period):
    dataframe['RSI'] = pta.rsi(dataframe['Close'])
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe.RSI,name='RSI',marker=dict(color='orange'),line=dict(width=2,color='orange')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=[70]*len(dataframe),name='OverBought',marker=dict(color='red'),line=dict(width=2,color='red',dash='dash')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=[30]*len(dataframe),name='Oversold',marker=dict(color='#79da84'),line=dict(width=2,color='#79da84',dash='dash')))
    fig.update_layout(yaxis_range=[0,100],height=200,plot_bgcolor='white',paper_bgcolor='#e1efff',margin=dict(l=0,r=0,t=0,b=0)
                      ,legend=dict(orientation="h",yanchor="top",xanchor="right",x=1))
    
    return fig


def moving_average(dataframe,num_period):
    dataframe['SMA_20'] = pta.sma(dataframe['Close'],7)
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()

    # fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['Open'],mode='lines',name='Open',line=dict(width=2,color='#5ab7ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['Close'],mode='lines',name='Close',line=dict(width=2,color='black')))
    # fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['High'],mode='lines',name='High',line=dict(width=2,color="#0078ff")))
    # fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['Low'],mode='lines',name='Low',line=dict(width=2,color='red')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['SMA_20'],mode='lines',name='SMA_20',line=dict(width=2,color='purple')))
    
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height=500,margin=dict(l=0,r=20,t=20,b=0),plot_bgcolor='white',paper_bgcolor='#e1efff',legend=dict(yanchor="top",xanchor="right"))
    return fig

def MACD(dataframe,num_period):
    macd=pta.macd(dataframe['Close']).iloc[:,0]
    macd_signal = pta.macd(dataframe['Close']).iloc[:,1]
    macd_hist = pta.macd(dataframe['Close']).iloc[:,2]
    dataframe['MACD'] = macd 
    dataframe['MACD Signal'] = macd_signal 
    dataframe['MACD Hist'] = macd_hist
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['MACD Signal'],name='OverBought',marker=dict(color='red'),line=dict(width=2,color='red',dash='dash')))
    fig.add_trace(go.Scatter(x=dataframe['Date'],y=dataframe['MACD'],name='RSI',marker=dict(color='orange'),line=dict(width=2,color='orange',dash='dash')))
    fig.update_layout(yaxis_range=[0,100],height=200,plot_bgcolor='white',paper_bgcolor='#e1efff',margin=dict(l=0,r=0,t=0,b=0)
                      ,legend=dict(orientation="h",yanchor="top",xanchor="right",x=1))
    
    return fig

def moving_average_forecast(forecast):
    fig = go.Figure()

    # Show only last month (30 days) of historical data before forecast
    # Historical data is everything except the last 30 days (which is the forecast)
    historical_data = forecast.iloc[:-30]
    forecast_data = forecast.iloc[-30:]
    
    # Get only the last 30 days of historical data
    if len(historical_data) > 30:
        historical_data = historical_data.iloc[-30:]
    
    # Ensure lines connect by including the first forecast point in both traces
    if len(historical_data) > 0 and len(forecast_data) > 0:
        # Historical trace: include all historical data plus first forecast point for continuity
        hist_x = list(historical_data.index) + [forecast_data.index[0]]
        hist_y = list(historical_data['Close']) + [forecast_data['Close'].iloc[0]]
        
        # Forecast trace: start from first forecast point (shared with historical)
        forecast_x = list(forecast_data.index)
        forecast_y = list(forecast_data['Close'])
        
        fig.add_trace(go.Scatter(
            x = hist_x, 
            y = hist_y, 
            mode = 'lines', 
            name ='Close Price',
            line = dict(width = 2, color = 'black')
        ))
        fig.add_trace(go.Scatter(
            x = forecast_x, 
            y = forecast_y, 
            mode = 'lines', 
            name ='Future Close Price',
            line = dict(width = 2, color = 'red')
        ))
    else:
        fig.add_trace(go.Scatter(x = historical_data.index, y = historical_data['Close'], mode = 'lines', name ='Close Price',line = dict(width = 2, color = 'black')))
        fig.add_trace(go.Scatter(x = forecast_data.index, y = forecast_data['Close'], mode = 'lines', name ='Future Close Price',line = dict(width = 2, color = 'red')))

    fig.update_xaxes(rangeslider_visible = True)
    fig.update_layout(height = 500, margin = dict(l=0, r=20, t=20, b=0) , plot_bgcolor = 'white',paper_bgcolor = '#e1efff',legend=dict(yanchor='bottom',xanchor='right'))

    return fig
