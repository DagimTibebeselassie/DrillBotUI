html.Div([
            dcc.Input(
                id='samples',
                type='number',
                value=1,  # Default value
                min=0,
                style={'position': 'absolute','height': '35px','width': '55px', "border-radius":'50px','left': '1050px','top': '600px','text-align': 'center'}
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),
        html.Div([
            dcc.Input(
                id='minutes',
                type='number',
                value=0,  # Default value
                min=0,
                style={'position': 'absolute','height': '35px','width': '55px', "border-radius":'50px','left': '1125px','top': '600px','text-align': 'center' }
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),
        html.Div([
            dcc.Input(
                id='seconds',
                type='number',
                value=0,  # Default value
                min=0,
                style={'position': 'absolute','height': '35px','width': '55px', "border-radius":'50px','left': '1199px','top': '600px','text-align': 'center'}
            ),
        ], style={'display': 'inline-block'}),
    html.Div([
        html.Div('Samples', style={'position':'absolute','left': '1050px'}),
        html.Div('Minutes', style={'position':'absolute','left': '1125px'}),
        html.Div('Seconds', style={'position':'absolute','left': '1199px'}),
    ]),
