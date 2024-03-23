import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

app = dash.Dash(__name__, external_stylesheets=['/assets/styles.css'])
upBtn = r"\assets\UpBtn.png"
downBtn = r"\assets\downBtn.png"
leftBtn = r"\assets\leftBtn.png"
rightBtn = r"\assets\rightBtn.png"


# Define the navigation bar layout
navbar = html.Div([
    html.Nav([
        html.H1("FOCUSbot", className="logo"),
        html.A("Home", href="/home", className="nav-link"),
        html.A("Control Panel", href="/page-1", className="nav-link"),
        html.A("Data Collection", href="/page-2", className="nav-link"),
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
        showlegend=False
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


# Define the layout for the entire application
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
            figure=add_grid()
        )
    ]),
    html.Div([
            dcc.Input(
                id='samples',
                type='number',
                className = "samples",
                value=1,  # Default value
                min=0,
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),
        html.Div([
            dcc.Input(
                id='minutes',
                type='number',
                className = "minute",
                value=0,  # Default value
                min=0,
            ),
        ], style={'display': 'inline-block', 'margin-right': '20px'}),
        html.Div([
            dcc.Input(
                id='seconds',
                className = "seconds",
                type='number',
                value=0,  # Default value
                min=0,
            ),
        ], style={'display': 'inline-block'}),
    html.Div([
        html.Div('Samples', style={'position':'absolute'}),
        html.Div('Minutes', style={'position':'absolute','margin-left': '75px'}),
        html.Div('Seconds', style={'position':'absolute', 'margin-left': '149px'}),
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
    ], id='rightBtn')
    ]),
    html.Div([
        html.Button("RESET", id = "reset_button", className = "reset")
    ]),
    html.Div([
        html.Button("SAMPLE", id = "sample_button", className = "sample")
    ])
])

# Callback to update the page content based on the URL and add the grid when needed
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def update_page_content(pathname):
    if pathname == '/page-1':
        content = [
            html.H3('Page 1'),
            dcc.Markdown('''
                This is the content of page 1.
            ''')
        ]
    elif pathname == '/home':
        content = [
            html.H3('Home'),
            dcc.Markdown('''
                This is the content of Home.
            ''')
        ]
    elif pathname == '/page-2':
        content = [
            html.H3('Page 2'),
            dcc.Markdown('''
                This is the content of page 2.
            ''')
        ]
    else:
        content = [
            html.H3('Home'),
            dcc.Markdown('''
                This is the home page.
            ''')
        ]
    
    # Add the grid if needed
    if pathname in ['/page-1', '/home', '/page-2']:
        content.append(
            dcc.Graph(
                id='grid',
                figure=add_grid()
            )
        )
    
    return content

if __name__ == '__main__':
    app.run_server(debug=True)
