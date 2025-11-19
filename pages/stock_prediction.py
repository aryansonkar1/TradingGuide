import streamlit as st
from pages.utils.model_train import get_data,stationary_check,get_rolling_mean,get_differencing_order,fit_model,evaluate_model,get_forecast,inverse_scaling,scaling
import pandas as pd
import numpy as np
from pages.utils.plotly_fig import pplotly_table, moving_average_forecast
import plotly.graph_objects as go # <-- Import graph_objects


st.set_page_config(
    page_title = 'Stock Prediction',
    page_icon = ':chart_with_downwards_trend:',
    layout = 'wide'
)
st.title('Stock Prediction')

ticker = st.text_input('Stock ticker','AAPL')

rmse = 0



stock = get_data(ticker)
rolling_price = get_rolling_mean(stock['Close'])

# Ensure rolling_price is a 1D Series (handle case where it might be 2D array)
if isinstance(rolling_price, pd.Series):
    rolling_price_series = rolling_price
elif isinstance(rolling_price, pd.DataFrame):
    # If it's a DataFrame, extract the first column as Series
    rolling_price_series = rolling_price.iloc[:, 0] if len(rolling_price.columns) > 0 else rolling_price.squeeze()
elif isinstance(rolling_price, np.ndarray):
    # If it's a numpy array, flatten if 2D and create Series with proper index
    if rolling_price.ndim > 1:
        rolling_price = rolling_price.flatten()
    # Get the index from original data, accounting for dropped NaN values from rolling mean
    original_index = stock['Close'].index
    # rolling mean with window=7 drops first 6 values, so start from index 6
    rolling_index = original_index[6:6+len(rolling_price)]
    rolling_price_series = pd.Series(rolling_price, index=rolling_index)
elif hasattr(rolling_price, 'shape') and len(rolling_price.shape) > 1 and rolling_price.shape[1] > 1:
    # Handle array-like objects with 2D shape (like some numpy array wrappers)
    rolling_price_flat = np.array(rolling_price).flatten()
    original_index = stock['Close'].index
    rolling_index = original_index[6:6+len(rolling_price_flat)]
    rolling_price_series = pd.Series(rolling_price_flat, index=rolling_index)
elif hasattr(rolling_price, 'values'):
    # If it has .values attribute, try to extract and flatten
    values = np.array(rolling_price.values)
    if values.ndim > 1:
        values = values.flatten()
    original_index = stock['Close'].index
    rolling_index = original_index[6:6+len(values)]
    rolling_price_series = pd.Series(values, index=rolling_index)
else:
    # Fallback: convert to numpy array first, then to Series
    try:
        arr = np.array(rolling_price)
        if arr.ndim > 1:
            arr = arr.flatten()
        original_index = stock['Close'].index
        rolling_index = original_index[6:6+len(arr)]
        rolling_price_series = pd.Series(arr, index=rolling_index)
    except Exception:
        # Last resort: try to create Series directly
        rolling_price_series = pd.Series(rolling_price).squeeze()

# Convert Series to DataFrame
rolling_price_df = rolling_price_series.to_frame(name='Close')
rolling_price_df.index.name = 'Date'

# Keep rolling_price as Series for other functions that expect Series
rolling_price = rolling_price_series


differencing_order = get_differencing_order(rolling_price)
scaled_data, scaler = scaling(rolling_price)
rmse = evaluate_model(scaled_data,differencing_order)

st.write('**Model RMSE Score:**',rmse)

st.subheader('Forecasting Next 30 days close price for ' + ticker)
# Get the last date from historical data to ensure continuous line
last_historical_date = rolling_price_df.index[-1]
forecast = get_forecast(scaled_data, differencing_order, last_historical_date=last_historical_date)

forecast['Close'] = inverse_scaling(scaler, forecast['Close'])
st.write('#### Forecast Data (Next 30 Days)')
forecast = forecast.sort_index(ascending=True).round(3)
forecast['Date'] = forecast.index
forecast.reset_index(drop=True, inplace=True)
forecast = forecast[['Date', 'Close']]
fig_tail = pplotly_table(forecast)
fig_tail.update_layout(height= 220)
st.plotly_chart(fig_tail , use_container_width=True)

# Add forecast visualization chart
st.write('#### Forecast Visualization (Next 30 Days)')
# Combine historical and forecast data for visualization
historical_data = rolling_price_df.copy()

# Combine historical and forecast
forecast_with_index = forecast.set_index('Date')
combined = pd.concat([historical_data, forecast_with_index])
fig_forecast = moving_average_forecast(combined)
st.plotly_chart(fig_forecast, use_container_width=True)





