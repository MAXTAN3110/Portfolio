import json
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash_iconify import DashIconify

with open("src/info_config.json") as f:
    CONFIG = json.load(f)


def create_footer_section():
    layout = dbc.Container(
        [
            dbc.Row(
                [
                    # Left Column - About/Description
                    dbc.Col(
                        [
                            html.H4(
                                CONFIG["name"],
                                className="text-white fw-bold mb-3",
                                style={"fontSize": "calc(0.8vw+0.6rem)"},
                            ),
                            html.P(
                                "Intrigued by data, inspired by patterns, "
                                "always exploring the story behind the numbers.",
                                className="text-white",
                                style={
                                    "color": "rgba(255, 255, 255, 0.8)",
                                    "lineHeight": "1.6",
                                    "fontSize": "calc(0.7vw+0.5rem)",
                                },
                            ),
                        ],
                        width=8,
                        className="mb-3 ps-5 pe-3",
                    ),
                    # Right Column - Contact Information
                    dbc.Col(
                        [
                            html.H4(
                                "Get In Touch",
                                className="text-white fw-bold mb-3",
                                style={"fontSize": "calc(0.8vw+0.6rem)"},
                            ),
                            # Email
                            html.Div(
                                [
                                    DashIconify(
                                        icon="mdi:email",
                                        className="me-2",
                                        style={"color": "#24DEF7"},
                                    ),
                                    html.Span(
                                        CONFIG["email"],
                                        className="text-white",
                                        style={
                                            "color": "rgba(255, 255, 255, 0.8)",
                                        },
                                    ),
                                ],
                                className="d-flex align-items-center mb-2",
                                style={"fontSize": "calc(0.7vw + 0.5rem)"},
                            ),
                            # Phone
                            html.Div(
                                [
                                    DashIconify(
                                        icon="line-md:phone-filled",
                                        className="me-2",
                                        style={"color": "#24DEF7"},
                                    ),
                                    html.Span(
                                        CONFIG["phone"],
                                        className="text-white",
                                        style={
                                            "color": "rgba(255, 255, 255, 0.8)",
                                        },
                                    ),
                                ],
                                className="d-flex align-items-center mb-2",
                                style={"fontSize": "calc(0.7vw + 0.5rem)"},
                            ),
                            # LinkedIn
                            html.Div(
                                [
                                    DashIconify(
                                        icon="mdi:linkedin",
                                        className="me-2",
                                        style={"color": "#24DEF7"},
                                    ),
                                    dcc.Link(
                                        "Personal LinkedIn",
                                        href=CONFIG["LinkedIn"],
                                        target="_blank",
                                        style={
                                            "color": "#24DEF7",
                                            "textDecoration": "none",
                                        },
                                        className="text-decoration-underline",
                                    ),
                                ],
                                style={"fontSize": "calc(0.7vw + 0.5rem)"},
                                className="d-flex align-items-center mb-3",
                            ),
                        ],
                        width=4,
                    ),
                ],
                className="mb-3 g-4",
                style={"marginLeft": "7rem", "marginRight": "7rem"},
            ),
            # Divider Line
            html.Hr(
                style={
                    "borderColor": "white",
                    "borderWidth": "2px 0 0 0",
                    "opacity": "0.7",
                    "maxWidth": "75vw",
                    "margin": "1rem auto",
                }
            ),
            # Copyright Section
            dbc.Row(
                [
                    dbc.Col(
                        html.P(
                            f"Copyright © 2025 {CONFIG['name']}",
                            className="text-center text-white mb-0",
                            style={
                                "color": "rgba(255, 255, 255, 0.6)",
                                "fontSize": "calc(0.3vw + 0.7rem)",
                            },
                        ),
                        width=12,
                    )
                ]
            ),
        ],
        fluid=True,
        style={
            "backgroundColor": "black",
            "padding": "3rem 2rem 2rem 2rem",
            "marginTop": "auto",
        },
    )
    return layout
