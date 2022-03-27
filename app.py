
from dash import *
import plotly.express as px
import pandas as pd
from analysis import Analysis
import openpyxl

dash_app = dash.Dash(__name__)
app=dash_app.server

# Data
order_data = Analysis.getData("my_shop_data.xlsx","order")
employee_data = Analysis.getData("my_shop_data.xlsx","employee")
product_data = Analysis.getData("my_shop_data.xlsx","products")
customer_data = Analysis.getData("my_shop_data.xlsx","customers")


# Total sales by employees
fig2 = px.bar(
    Analysis.totalSalesByEmployees(employee_data,order_data),
    x="employees",
    y="sales",
    title="Total sales by employee",
    barmode="group")

# Sales by employee
fig = px.bar(
    Analysis.salesByEmployee(Analysis.combineFirstLastName(employee_data)[0],employee_data,order_data,product_data),
    title="Sales by employee: "+Analysis.combineFirstLastName(employee_data)[0],
    x="product",
    y="sales",
    barmode="group")

# Total sales by product (x:products,y:sales)
fig3 = px.bar(
    Analysis.totalSalesByProduct(product_data,order_data),
    x="products",
    y="sales",
    title="Total sales by product",
    barmode="group")

names = Analysis.combineFirstLastName(employee_data)
dash_app.layout = html.Div(children=[
    html.Div([
        html.H1(children="Delivery 1"),
        dcc.Graph(
            id="b",
            figure=fig2
        ),
        dcc.Dropdown(
            id="a_dropdown",
            options=names,
            value=names[0],
            clearable=False,
        ),
        dcc.Graph(
            id="a",
            figure=fig
        ),
        dcc.Graph(
            id="aa",
            figure=fig3
        )
    ],style={"width":"50%","display":"block","margin-left":"auto","margin-right":"auto","margin-bottom":"3rem"}),
])

@dash_app.callback(
    Output("a", "figure"),
    Input("a_dropdown", "value"))
def update_bar_chart(name):
    return px.bar(
        Analysis.salesByEmployee(name,employee_data,order_data,product_data),
        title="Sales by employee: "+name,
        x="product",
        y="sales",
        barmode="group")

if __name__ == "__main__":
    dash_app.run_server(debug=True)















#
