import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv('./formatted_output.csv')
df = df.sort_values(by='date')

app = Dash(__name__)

PAGE_BG = "#1e1e1e"
CARD_BG = "#2d2d2d"
TEXT_COLOR = "#ffffff"
ACCENT_COLOR = "#00adb5"

app.layout = html.Div(
    style={
        "backgroundColor": PAGE_BG,
        "color": TEXT_COLOR,
        "minHeight": "100vh",
        "fontFamily": "Segoe UI, Tahoma, Geneva, Verdana, sans-serif",
        "padding": "2rem"
    },
    children=[
        html.Header(
            children=[
                html.H1("Soul Foods: Regional Sales Analytics", style={"margin": "0", "paddingBottom": "10px"}),
                html.P("Pink Morsel Performance Dashboard", style={"color": ACCENT_COLOR, "fontSize": "1.2rem", "marginTop": "0"})
            ],
            style={"textAlign": "center", "marginBottom": "2rem"}
        ),

        html.Div(
            children=[
                html.Label("Select Region:", style={"fontWeight": "bold", "marginRight": "15px", "fontSize": "1.1rem"}),
                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": " North", "value": "north"},
                        {"label": " East", "value": "east"},
                        {"label": " South", "value": "south"},
                        {"label": " West", "value": "west"},
                        {"label": " All Regions", "value": "all"}
                    ],
                    value="all",
                    inline=True,
                    inputStyle={"marginRight": "5px", "marginLeft": "20px"}
                )
            ],
            style={
                "backgroundColor": CARD_BG,
                "padding": "1.5rem",
                "borderRadius": "10px",
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
                "marginBottom": "2rem",
                "boxShadow": "0 4px 6px rgba(0,0,0,0.3)"
            }
        ),

        html.Div(
            children=[dcc.Graph(id="sales-chart")],
            style={
                "backgroundColor": CARD_BG, 
                "padding": "1rem", 
                "borderRadius": "10px", 
                "boxShadow": "0 4px 6px rgba(0,0,0,0.3)"
            }
        )
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_sales_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df.query("region == @selected_region")


    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        template="plotly_dark",
        color_discrete_sequence=[ACCENT_COLOR]
    )

    fig.update_layout(
        title=f"Sales Trend: {selected_region.title()}",
        xaxis_title="Transaction Date",
        yaxis_title="Total Sales (USD)",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)