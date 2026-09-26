import pandas as pd
import yfinance as yf


def _get_ticker_object(ticker):
    """Return a Yahoo Finance ticker object or raise a clear error."""
    symbol = (ticker or "").strip()
    if not symbol:
        raise ValueError("Ticker symbol is required.")

    return yf.Ticker(symbol.upper())


def get_financials(ticker):
    """Return a dictionary of key financial tables for a ticker."""
    stock = _get_ticker_object(ticker)

    tables = {
        "Income Statement": stock.financials.head(10),
        "Balance Sheet": stock.balance_sheet.head(10),
        "Cash Flow": stock.cashflow.head(10),
    }

    cleaned_tables = {}
    for name, frame in tables.items():
        if frame is None or frame.empty:
            cleaned_tables[name] = pd.DataFrame(columns=["No Data"])
        else:
            cleaned_tables[name] = frame.reset_index()

    return cleaned_tables


def get_news(ticker):
    """Return the latest news articles for a ticker as a DataFrame."""
    stock = _get_ticker_object(ticker)
    articles = stock.news or []

    if not articles:
        return pd.DataFrame(columns=["title", "publisher", "published_at", "description"])

    rows = []
    for article in articles[:10]:
        content = article.get("content", {}) if isinstance(article, dict) else {}
        if not isinstance(content, dict):
            content = {}

        title = content.get("title") or article.get("title") or "No title"
        description = content.get("description") or article.get("summary") or "No description"
        publisher = content.get("publisher") or article.get("publisher") or "Unknown"
        published_at = article.get("providerPublishTime") or article.get("published_at")

        rows.append(
            {
                "title": title,
                "publisher": publisher,
                "published_at": published_at,
                "description": description,
            }
        )

    return pd.DataFrame(rows)


def get_stock_price_ratings(ticker):
    """Return the current stock price and analyst recommendation history."""
    stock = _get_ticker_object(ticker)

    info = stock.info or {}
    price = info.get("currentPrice")

    recommendations = stock.recommendations
    if recommendations is None or recommendations.empty:
        recommendations = pd.DataFrame(columns=["To Grade", "From Grade", "Action", "Date"])
    else:
        recommendations = recommendations.tail(10).reset_index()

    return {
        "price": price,
        "recommendations": recommendations,
    }
