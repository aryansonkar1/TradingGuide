import streamlit as st

st.set_page_config(
    page_title="Trading Guide - Stock Analysis & Prediction Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# st.title("Trading Guide App :bar_chart:")
# st.header("We provide the greatest platform to collect all information prior to investing in stock")
# st.image("image.webp")




st.markdown("""
    <div style='text-align: center; padding: 5rem 2rem; background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%); 
                border-radius: 24px; margin-bottom: 4rem; color: white; box-shadow: 0 25px 70px rgba(15, 23, 42, 0.4);'>
        <h1 style='color: white; font-size: 3.8rem; font-weight: 800; margin-bottom: 1.5rem; letter-spacing: -0.03em; line-height: 1.1;'>
             Trading Guide Platform
        </h1>
        <p style='color: rgba(255,255,255,0.9); font-size: 1.5rem; max-width: 900px; margin: 0 auto 3rem; line-height: 1.7; font-weight: 400;'>
            Empower your investment decisions with AI-powered stock analysis, real-time predictions, and comprehensive market insights
        </p>
        <div style='display: flex; justify-content: center; gap: 1.5rem; margin-top: 2.5rem; flex-wrap: wrap;'>
            <div style='background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%); padding: 1.5rem 2.5rem; border-radius: 16px; box-shadow: 0 10px 25px rgba(6, 182, 212, 0.3);'>
                <div style='font-size: 2.5rem; font-weight: 700;'>1000+</div>
                <div style='font-size: 1rem; opacity: 0.95; margin-top: 0.3rem;'>Stocks Analyzed</div>
            </div>
            <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.5rem 2.5rem; border-radius: 16px; box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3);'>
                <div style='font-size: 2.5rem; font-weight: 700;'>30 Days</div>
                <div style='font-size: 1rem; opacity: 0.95; margin-top: 0.3rem;'>Price Forecasts</div>
            </div>
            <div style='background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); padding: 1.5rem 2.5rem; border-radius: 16px; box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);'>
                <div style='font-size: 2.5rem; font-weight: 700;'>Real-time</div>
                <div style='font-size: 1rem; opacity: 0.95; margin-top: 0.3rem;'>Market Data</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


st.markdown("## we provide the following services")

st.markdown("#### :one: stock Information")
st.write("Through this page, you can see all the information about stock")

st.markdown("#### :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models.Use this tool to gainn valuable insights into market trends and make informed investment decision")

st.markdown("#### :three: CAPM Return")
st.write("Discover how the Capital Asset Pricing Model(CAPM) calculates the expected return of different stock asset based on its risk and market performanece")

st.markdown("#### :four: CAPM Beta")
st.write("Calculates Beta and Expected return for individual stock")