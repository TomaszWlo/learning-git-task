import os
import datetime as dt
import pandas as pd

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import tab1
import tab2
import tab3

app = Dash(__name__, suppress_callback_exceptions=True)


class db:

    def __init__(self):
        self.transactions = db.transation_init()
        self.cc = pd.read_csv(r'db\country_codes.csv', index_col=0)
        self.customers = pd.read_csv(r'db\customers.csv', index_col=0)
        self.prod_info = pd.read_csv(r'db\prod_cat_info.csv')

    @staticmethod
    def transation_init():

        src = r'db\transactions'
        frames = []

        for filename in os.listdir(src):
            frames.append(
                pd.read_csv(
                    os.path.join(src, filename),
                    index_col=0
                )
            )

        transactions = pd.concat(frames, ignore_index=True)

        def convert_dates(x):
            try:
                return dt.datetime.strptime(x, '%d-%m-%Y')
            except:
                return dt.datetime.strptime(x, '%d/%m/%Y')

        transactions['tran_date'] = transactions['tran_date'].apply(convert_dates)

        return transactions

    def merge(self):

        df = self.transactions.join(
            self.prod_info
                .drop_duplicates(subset=['prod_cat_code'])
                .set_index('prod_cat_code')['prod_cat'],
            on='prod_cat_code',
            how='left'
        )

        df = df.join(
            self.prod_info
                .drop_duplicates(subset=['prod_sub_cat_code'])
                .set_index('prod_sub_cat_code')['prod_subcat'],
            on='prod_subcat_code',
            how='left'
        )

        df = df.join(
            self.customers
                .join(self.cc, on='country_code')
                .set_index('customer_Id'),
            on='cust_id'
        )

        self.merged = df

#--------------------------------

@app.callback(Output('tabs-content','children'),[Input('tabs','value')])
def render_content(tab):

    if tab == 'tab-1':
        return tab1.render_tab(df.merged)
    elif tab == 'tab-2':
        return tab2.render_tab(df.merged)
    elif tab == 'tab-3':
        return tab3.render_tab(df.merged)

## tab1 callbacks

@app.callback(Output('bar-sales','figure'),
    [Input('sales-range','start_date'),Input('sales-range','end_date')])
def tab1_bar_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt'] > 0].groupby([pd.Grouper(key='tran_date', freq='ME'), 'Store_type'])['total_amt'].sum().round(2).unstack()

    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(x=grouped.index,y=grouped[col],name=col,hoverinfo='text',
        hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Przychody',barmode='stack',legend=dict(x=0,y=-0.5)))

    return fig

@app.callback(Output('choropleth-sales','figure'),
            [Input('sales-range','start_date'),Input('sales-range','end_date')])
def tab1_choropleth_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby('country')['total_amt'].sum().round(2)

    trace0 = go.Choropleth(colorscale='Viridis',reversescale=True,
                            locations=grouped.index,locationmode='country names',
                            z = grouped.values, colorbar=dict(title='Sales'))
    data = [trace0]
    fig = go.Figure(data=data,layout=go.Layout(title='Mapa',geo=dict(showframe=False,projection={'type':'natural earth'})))

    return fig

## tab2 callbacks

@app.callback(Output('barh-prod-subcat','figure'),
            [Input('prod_dropdown','value')])
def tab2_barh_prod_subcat(chosen_cat):

    grouped = df.merged[(df.merged['total_amt']>0)&(df.merged['prod_cat']==chosen_cat)].pivot_table(index='prod_subcat',columns='Gender',values='total_amt',aggfunc='sum').assign(_sum=lambda x: x['F']+x['M']).sort_values(by='_sum').round(2)

    traces = []
    for col in ['F','M']:
        traces.append(go.Bar(x=grouped[col],y=grouped.index,orientation='h',name=col))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(barmode='stack',margin={'t':20,}))

    return fig

# tab3 callboacks

@app.callback(
    Output('bar-sales-days', 'figure'),
    [Input('tabs', 'value')]
)
def tab3_sales_by_day(tab):

    grouped = df.merged.groupby(
        ['day_of_week', 'Store_type'],
        observed=True
    )['total_amt'].sum().round(2).unstack()

    traces = []

    for col in grouped.columns:
        traces.append(
            go.Bar(
                x=grouped.index,
                y=grouped[col],
                name=col
            )
        )

    fig = go.Figure(
        data=traces,
        layout=go.Layout(
            title='Sprzedaż według dnia tygodnia i kanału sprzedaży',
            barmode='group'))

    return fig

@app.callback(
    Output('gender-store', 'figure'),
    [Input('store-dropdown', 'value')]
)
def tab3_gender_store(chosen_store):

    grouped = df.merged[
        df.merged['Store_type'] == chosen_store
    ].groupby('Gender')['cust_id'].nunique()

    fig = go.Figure(
        data=[
            go.Pie(
                labels=grouped.index,
                values=grouped.values,
                hole=0.3,
                textinfo='label+percent',
                hovertemplate='%{label}: %{value} klientów<extra></extra>'
            )
        ],
        layout=go.Layout(
            title=f'Klienci według płci - {chosen_store}'
        )
    )

    return fig

#------------------------------


df = db()
df.merge()

df.merged['day_of_week'] = df.merged['tran_date'].dt.day_name()

days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

df.merged['day_of_week'] = pd.Categorical(
    df.merged['day_of_week'],
    categories=days,
    ordered=True
)

grouped = df.merged.groupby(
    ['day_of_week', 'Store_type'],
    observed=True
)['total_amt'].sum().round(2).unstack()


app.layout = html.Div([
    html.Div([
        dcc.Tabs(
            id='tabs',
            value='tab-1',
            children=[
                dcc.Tab(label='Sprzedaż globalna', value='tab-1'),
                dcc.Tab(label='Produkty', value='tab-2'),
                dcc.Tab(label='Kanały sprzedaży', value='tab-3')
            ]
        ),

        html.Div(id='tabs-content')

    ], style={
        'width': '80%',
        'margin': 'auto'
    })
], style={
    'height': '100%'
})


if __name__ == '__main__':
    app.run(debug=True)

