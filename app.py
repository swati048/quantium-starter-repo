import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# ---------- Load & prepare data ----------
df = pd.read_csv("formatted_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")


# ---------- Helper function to build figure ----------
def make_figure(region):
    if region != "all":
        filtered = df[df["region"] == region]
    else:
        filtered = df

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        title=f"Sales Trend — {region.upper()}",
    )

    fig.update_layout(
        template="plotly_white",

        xaxis_title="Date",
        yaxis_title="Sales ($)",

        plot_bgcolor="#312d5c",
        paper_bgcolor="#141136",
        font_color="white",

        margin=dict(l=40, r=20, t=60, b=40)
    )
    return fig


# ---------- Dash App ----------
app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "background": "linear-gradient(to right, #74ebd5, #ACB6E5)",
        "padding": "30px"
    },
    children=[

        html.H1(
            "Soul Foods Pink Morsel Sales",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "20px"
            }
        ),

        html.P(
            "Interactive regional sales exploration",
            style={"textAlign": "center", "color": "#555"}
        ),
        
        html.Div(
            style={
                "background": "linear-gradient(to right, #ed72b8, #03cafc)",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0px 4px 12px rgba(0,0,0,0.1)",
                "marginBottom": "20px"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontWeight": "bold"}
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginTop": "10px"}
                ),
            ]
        ),

        html.Div(
            style={
                "background": "linear-gradient(to right, #ed72b8, #03cafc)",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0px 4px 12px rgba(0,0,0,0.1)"
            },
            children=[
                dcc.Graph(id="sales-chart")
            ]
        )
    ]
)


# ---------- Callback ----------
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    return make_figure(selected_region)


# ---------- Run ----------
if __name__ == "__main__":
    app.run(debug=True)
