import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# ---- Load data ----
df = pd.read_csv("formatted_sales.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# ---- Create line chart ----
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",   # optional — remove if not desired
    title="Pink Morsel Sales"
)

# Axis labels
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales ($)"
)

# ---- Dash App ----
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Soul Foods Sales Visualiser",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# ---- Run server ----
if __name__ == "__main__":
    app.run(debug=True)
