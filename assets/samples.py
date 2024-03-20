app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content'),
    html.Label(''),
    html.Div([
        html.Div([
            dcc.Input(
                id='samples',
                type='number',
                value=1,  # Default value
                min=0,
                style={'height': '35','width': '45px', "border-radius":'50px'}
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),
        html.Div([
            dcc.Input(
                id='minutes',
                type='number',
                value=0,  # Default value
                min=0,
                style={'height': '35','width': '45px', "border-radius":'50px'}
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),
        html.Div([
            dcc.Input(
                id='seconds',
                type='number',
                value=0,  # Default value
                min=0,
                style={'height': '35','width': '45px', "border-radius":'50px'}
            ),
        ], style={'display': 'inline-block'}),
    ]),
    html.Div([
        html.Div('Samples', style={'position':'absolute'}),
        html.Div('Minutes', style={'position':'absolute','margin-left': '75px'}),
        html.Div('Seconds', style={'position':'absolute', 'margin-left': '149px'}),
    ]),
])
