import dash
import dash_core_components as dcc
import dash_html_components as html

# Create the Dash application instance
app = dash.Dash(__name__)

# Define the layout of the application
app.layout = html.Div([
    #TODO
])

# Run the Dash application
if __name__ == '__main__':
    app.run_server(debug=True)
