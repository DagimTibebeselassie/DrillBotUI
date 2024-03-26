import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

app = dash.Dash(__name__, external_stylesheets=['/assets/styles.css'])
upBtn = r"\assets\UpBtn.png"
downBtn = r"\assets\downBtn.png"
leftBtn = r"\assets\leftBtn.png"
rightBtn = r"\assets\rightBtn.png"
stopBtn = r"\assets\stopBtn.png"


navbar = html.Div([
    html.Nav([
        html.H1("FOCUSbot", className="logo"),
        html.A("Home", href="/home", className="nav-link", style={"color": "black", "font-size": "20px"}),
        html.A("Control Panel", href="/page-1", className="nav-link", style={"color": "black", "font-size": "20px"}),
        html.A("Data Collection", href="/page-2", className="nav-link", style={"color": "black", "font-size": "20px"}),
    ], className="navbar")
])

def add_grid():
    # Create the grid layout
    layout = go.Layout(
        title='Joystick',
        xaxis=dict(title='X', range=[-1, 1]),
        yaxis=dict(title='Y', range=[-1, 1]),
        width=500,
        height=500,
        showlegend=False,
    )

    # Create the scatter plot (grid)
    scatter = go.Scatter(
        x=[-1, 0, 1, -1, 0, 1, -1, 0, 1],
        y=[1, 1, 1, 0, 0, 0, -1, -1, -1],
        mode='markers',
        marker=dict(size=1),
        showlegend=False
    )

    # Create the figure object
    fig = go.Figure(data=[scatter], layout=layout)

    return fig



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', children=[
        html.H3('Page Content'),
        dcc.Markdown('''
            This is the default content of the page.
        ''')
    ]),
    html.Div([
    dcc.Graph(
        id='grid',
        figure=add_grid(),
        style={'width': '50%', 'height': 'auto'}
    )
], style={'width': '30%', 'margin': '10px'}),
    html.Div([
            dcc.Input(
                id='samples',
                type='number',
                value=1,  
                min=0,
                style={'position': 'absolute','height': '45px','width': '75px', "border-radius":'20px','left': '1000px','top': '500px','text-align': 'center'}
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),
        html.Div([
            dcc.Input(
                id='minutes',
                type='number',
                value=0,  
                min=0,
                style={'position': 'absolute','height': '45px','width': '75px', "border-radius":'20px','left': '1100px','top': '500px','text-align': 'center' }
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),
        html.Div([
            dcc.Input(
                id='seconds',
                type='number',
                value=0,  # Default value
                min=0,
                style={'position': 'absolute','height': '45px','width': '75px', "border-radius":'20px','left': '1200px','top': '500px','text-align': 'center'}
            ),
        ], style={'display': 'inline-block'}),
    html.Div([
        html.Div('Samples', style={'position':'absolute','left': '1010px','top': '550px'}),
        html.Div('Minutes', style={'position':'absolute','left': '1110px','top': '550px'}),
        html.Div('Seconds', style={'position':'absolute','left': '1210px','top': '550px'}),
    ]),
    html.Div([
    html.Button([
        html.Img(src=upBtn, style={'width': '70px', 'height': '70px', 'margin-right': '5px'})
    ], id='upBtn'),
    html.Button([
        html.Img(src=downBtn, style={'width': '70px', 'height': '70px', 'margin-right': '5px'})
    ], id='downBtn'),
    html.Button([
        html.Img(src=leftBtn, style={'width': '70px', 'height': '70px', 'margin-right': '5px'})
    ], id='leftBtn'),
    html.Button([
        html.Img(src=rightBtn, style={'width': '70px', 'height': '70px', 'margin-right': '5px'})
    ], id='rightBtn'),
    html.Button([
        html.Img(src=stopBtn, id="stopImg")
    ], id='stopBtn')
], style={"width": "10px"}),
    html.Div([
        html.Button("RESET", id = "reset_button", className = "reset")
    ]),
    html.Div([
        html.Button("SAMPLE", id = "sample_button", className = "sample")
    ]),
    html.Div([
        html.Div([
            html.H5("Accelerometer"),
            html.Div([
                html.P("X:"),
                html.P("0.00"),
                html.P("Y:"),
                html.P("0.00"),
                html.P("Z:"),
                html.P("0.00")
            ], style={"width": "15px"})
        ], style={'flex': '1', 'flex-grow': 0.2}),
        html.Div([
            html.H5("Gyroscope"),
            html.Div([
                html.P("X:"),
                html.P("0.00"),
                html.P("Y:"),
                html.P("0.00"),
                html.P("Z:"),
                html.P("0.00")
            ], style={"width": "15px"})
        ], style={'flex': '1', 'flex-grow': 0.2}),
        html.Div([
            html.H5("GPS Data"),
            html.Div([
                html.P("Lat:"),
                html.P("0.00"),
                html.P("Long:"),
                html.P("0.00")
            ], style={"width": "15px"})
        ], style={'flex': '1', 'flex-grow': 0.2}),
    ], style={'display': 'flex', "width": "700px"}),
    html.Div([
    html.Div([
        html.Iframe(src="", width="200", height="200"),
        html.Iframe(src="", width="200", height="200"),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-end'})
])
])

# Callback to update the page content based on the URL and add the grid when needed
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def update_page_content(pathname):
    if pathname == '/page-1':
        content = [
            html.H3('Control Panel')
        ]
    elif pathname == '/home':
        content = [
            html.H3('Home')
        ]
    elif pathname == '/page-2':
        content = [
            html.H3('Data Collection')
        ]
    else:
        content = [
            html.H3('Home')
        ]
    
    return content

if __name__ == '__main__':
    app.run_server(debug=True)
