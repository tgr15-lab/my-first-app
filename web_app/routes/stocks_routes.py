from flask import Blueprint, request, render_template, redirect, url_for, flash

from app.stocks import fetch_stocks_csv

stocks_routes = Blueprint("stocks_routes", __name__)


@stocks_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html")


@stocks_routes.route("/stocks/dashboard")
def stocks_dashboard():
    print("STOCKS DASHBOARD...")
    symbol = (request.args.get("symbol") or "NFLX").upper().strip()
    print("SYMBOL:", symbol)

    try:
        df = fetch_stocks_csv(symbol)
        if "timestamp" not in df.columns:
            raise ValueError("No data found for that symbol.")
    except Exception as err:
        print("OOPS", err)
        flash(f"Oops, couldn't fetch data for '{symbol}'. Please check the symbol and try again.", "danger")
        return redirect(url_for("stocks_routes.stocks_form"))

    price_col = "adjusted_close" if "adjusted_close" in df.columns else "close"
    df = df.sort_values(by="timestamp", ascending=True)

    # most recent 10 days for the table, most recent first
    recent_rows = df.tail(10).iloc[::-1].to_dict("records")

    return render_template("stocks_dashboard.html",
        symbol=symbol,
        price_col=price_col,
        rows=recent_rows,
        dates=df["timestamp"].astype(str).tolist(),
        prices=df[price_col].tolist(),
    )