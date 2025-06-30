import dash
from dash import Dash, html, dcc, _dash_renderer
from callbacks.server_callbacks import register_server_callbacks
from callbacks.client_callbacks import register_client_callback
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from components.navbar import create_navbar
from components.image_modal import create_image_modal

_dash_renderer._set_react_version("18.2.0")

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dmc.styles.ALL],
    external_scripts=[
        "https://code.iconify.design/2/2.2.1/iconify.min.js",
    ],
    use_pages=True,
)

app.layout = dmc.MantineProvider(
    [
        dcc.Location(id="url", refresh="callback-nav"),
        create_navbar(),
        create_image_modal(),
        dash.page_container,
        html.Div(id="anchor-jump", className="d-none"),
    ],
)

register_server_callbacks(app)
register_client_callback(app)

if __name__ == "__main__":
    app.run(debug=True, dev_tools_ui=True, port=8050)
