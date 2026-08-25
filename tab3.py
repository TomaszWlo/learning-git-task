from dash import html, dcc


def render_tab(df):

    layout = html.Div([
        html.H1(
            'Kanały sprzedaży',
            style={'text-align': 'center'}
        ),

        html.Div([
            html.Div([
                dcc.Graph(id='bar-sales-days')
            ], style={'width': '50%'}),

            html.Div([
                dcc.Dropdown(
                    id='store-dropdown',
                    options=[
                        {'label': store, 'value': store}
                        for store in df['Store_type'].unique()
                    ],
                    value=df['Store_type'].unique()[0]
                ),

                dcc.Graph(id='gender-store')
            ], style={'width': '50%'})

        ], style={'display': 'flex'})
    ])

    return layout