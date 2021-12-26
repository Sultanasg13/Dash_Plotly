import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output 





app = dash.Dash(__name__)

# -- Import and clean data (importing csv into pandas)
df = pd.read_csv("Data2.csv")

print(df['CATEGORY'])
# df.reset_index(inplace=True)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Advertisment Spending", style={'text-align': 'center'}),
    dcc.Graph(id='my_app', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='my_app', component_property='figure')]
)
def update_graph():

    traceQ2 = go.Bar(
        name = 'Q2',
        x = df["CATEGORY"],
        y = df["Q2(spend)"]
    ) 

    traceQ3 = go.Bar(
        name = 'Q3',
        x = df["CATEGORY"],
        y = df["Q3(spend)"
              ]
    )     
    data1 = [traceQ2,traceQ3]

    fig = go.Figure(data = data1)

    return (fig)


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)