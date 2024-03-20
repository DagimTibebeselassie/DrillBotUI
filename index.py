import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=['/assets/styles.css'])

# Define the navigation bar layout
navbar = html.Div([
    html.Nav([
        html.H1("FOCUSbot", className="logo"),
        html.A("Home", href="/home", className="nav-link"),
        html.A("Control Panel", href="/page-1", className="nav-link"),
        html.A("Data Collection", href="/page-2", className="nav-link"),
    ], className="navbar")
])


# Define the layout for the entire application
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return html.Div([
            html.H3('Page 1'),
            dcc.Markdown('''
                This is the content of page 1.
            ''')
        ])
    elif pathname == '/home':
        return html.Div([
            html.H3('Home'),
            dcc.Markdown('''
                This is the content of Home.
            ''')
        ])
    elif pathname == '/page-2':
        return html.Div([
            html.H3('Page 2'),
            dcc.Markdown('''
                This is the content of page 2.
            ''')
        ])
    else:
        return html.Div([
            html.H3('Home'),
            dcc.Markdown('''
                This is the home page.
            ''')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
