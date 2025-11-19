# Trading Guide Platform 📈

A comprehensive Streamlit application for stock analysis, prediction, and market insights. This platform provides AI-powered stock analysis, real-time predictions, and comprehensive market data visualization.

## Features

- **Stock Information**: View detailed information about stocks including financial metrics, company profiles, and historical data
- **Stock Prediction**: Get 30-day price forecasts based on advanced forecasting models
- **Technical Analysis**: Interactive charts with RSI, MACD, and Moving Average indicators
- **Real-time Data**: Live market data using yfinance

## Project Structure

```
Trading_app/
├── Home.py                 # Main entry point
├── pages/
│   ├── stock_analysis.py   # Stock information and analysis page
│   ├── stock_prediction.py # Stock prediction page
│   └── utils/
│       ├── model_train.py  # ML model training utilities
│       └── plotly_fig.py  # Plotting utilities
├── requirements.txt        # Python dependencies
└── .streamlit/
    └── config.toml        # Streamlit configuration
```

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Trading_app
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

Run the Streamlit app:
```bash
streamlit run Home.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment

### Option 1: Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy your app for free.

1. **Push your code to GitHub**:
   - Create a new repository on GitHub
   - Push your code to the repository

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and branch
   - Set the main file path to `Home.py`
   - Click "Deploy"

3. **Your app will be live** at `https://your-app-name.streamlit.app`

### Option 2: Docker Deployment

1. Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. Build and run:
```bash
docker build -t trading-app .
docker run -p 8501:8501 trading-app
```

### Option 3: Heroku

1. Create a `Procfile`:
```
web: streamlit run Home.py --server.port=$PORT --server.address=0.0.0.0
```

2. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

3. Deploy to Heroku:
```bash
heroku create your-app-name
git push heroku main
```

### Option 4: AWS/Azure/GCP

For cloud platform deployment, you can use:
- **AWS**: EC2 instance or Elastic Beanstalk
- **Azure**: App Service or Container Instances
- **GCP**: Cloud Run or App Engine

## Requirements

- Python 3.8+
- See `requirements.txt` for all dependencies

## Usage

1. **Stock Analysis Page**: Enter a stock ticker symbol to view:
   - Company profile and financial metrics
   - Historical price data
   - Interactive charts with technical indicators (RSI, MACD, Moving Average)

2. **Stock Prediction Page**: Enter a stock ticker to get:
   - 30-day price forecast
   - Model performance metrics (RMSE)
   - Visual forecast charts

## Notes

- The app uses `yfinance` to fetch real-time stock data
- Predictions are based on historical data and statistical models
- Always verify predictions with additional research before making investment decisions

## License

This project is open source and available for personal and educational use.

