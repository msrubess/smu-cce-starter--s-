import streamlit as st

from analysis import get_financials, get_news, get_stock_price_ratings
from notebook_reader import list_reusable_functions


st.set_page_config(page_title="Finance Analysis App", page_icon="📈")
st.title("Finance Analysis Explorer")
st.write("Enter a stock ticker and choose an analysis type to explore basic financial data.")

with st.sidebar:
    st.caption("Notebook functions detected")
    try:
        functions = list_reusable_functions("notebooks")
        if functions:
            for func in functions:
                st.code(func)
        else:
            st.info("No reusable notebook functions were found.")
    except Exception as exc:
        st.warning(f"Unable to read notebooks: {exc}")

with st.form("analysis_form"):
    ticker = st.text_input("Ticker symbol", value="AAPL")
    analysis_type = st.selectbox(
        "Analysis type",
        ["filings", "news", "stock price ratings"],
    )
    run_button = st.form_submit_button("Run")

if run_button:
    symbol = ticker.strip()
    if not symbol:
        st.warning("Please enter a ticker symbol.")
        st.stop()

    symbol = symbol.upper()

    try:
        if analysis_type == "filings":
            st.subheader(f"Financial statements for {symbol}")
            results = get_financials(symbol)

            if not results:
                st.info("No financial data available for this ticker.")
            else:
                for section_name, frame in results.items():
                    st.write(f"### {section_name}")
                    st.dataframe(frame.head(10))

        elif analysis_type == "news":
            st.subheader(f"Recent news for {symbol}")
            news_df = get_news(symbol)

            if news_df.empty:
                st.info("No recent news was found for this ticker.")
            else:
                st.dataframe(news_df[["title", "publisher", "published_at", "description"]])

        else:
            st.subheader(f"Stock price and analyst ratings for {symbol}")
            result = get_stock_price_ratings(symbol)
            price = result["price"]
            recommendations = result["recommendations"]

            if price is not None:
                st.metric("Current Price", f"${price:,.2f}")
            else:
                st.warning("Current price data is not available for this ticker.")

            if recommendations.empty:
                st.info("No analyst rating history was found for this ticker.")
            else:
                st.dataframe(recommendations)

    except Exception as exc:
        st.error(f"Something went wrong while loading the data: {exc}")
        st.write("Try another ticker or check that the stock symbol is valid.")
