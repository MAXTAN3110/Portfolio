import dash_bootstrap_components as dbc
from dash import html
from components.contact_form import create_contact_form


def create_contact_section():
    layout = dbc.Container(
        [
            dbc.Row(
                [
                    html.Div(
                        [
                            # Header
                            html.H2(
                                "Contact",
                                className="text-center text-white pt-3 mb-2 fw-bold display-4",
                            ),
                            # Description
                            html.P(
                                "Have a question or want to work together? Send me a message and I'll get back to you as soon as possible.",
                                className="text-center mb-4",
                                style={
                                    "fontSize": "calc(1vw + 0.5rem)",
                                    "color": "rgba(255, 255, 255, 0.8)",
                                },
                            ),
                        ],
                        className="mb-3",
                        style={"maxWidth": "70vw"},
                    ),
                ],
                justify="center",
            ),
            dbc.Row(create_contact_form()),
        ],
        id="contact",
        fluid=True,
        className="py-5",
        style={"backgroundColor": "#0A1930", "minHeight": "100vh"},
    )
    return layout
