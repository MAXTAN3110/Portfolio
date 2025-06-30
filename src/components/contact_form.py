import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html


def create_contact_form():
    # Contact Form
    return (
        dmc.Card(
            html.Div(
                [
                    # Name Input
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText(
                                "Name",
                                style={
                                    "backgroundColor": "#24DEF7",
                                    "color": "#0A1930",
                                    "fontWeight": "bold",
                                    "minWidth": "80px",
                                },
                            ),
                            dbc.Input(
                                id="contact-name",
                                placeholder="Your full name",
                                type="text",
                                style={
                                    "backgroundColor": "#DCDEE4",
                                    "color": "#0A1930",
                                },
                            ),
                        ],
                        className="mb-3",
                    ),
                    # Email Input
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText(
                                "Email",
                                style={
                                    "backgroundColor": "#24DEF7",
                                    "color": "#0A1930",
                                    "fontWeight": "bold",
                                    "minWidth": "80px",
                                },
                            ),
                            dbc.Input(
                                id="contact-email",
                                placeholder="your.email@example.com",
                                type="email",
                                style={
                                    "backgroundColor": "#DCDEE4",
                                    "color": "#0A1930",
                                },
                            ),
                        ],
                        className="mb-3",
                    ),
                    # Title Input
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText(
                                "Title",
                                style={
                                    "backgroundColor": "#24DEF7",
                                    "color": "#0A1930",
                                    "fontWeight": "bold",
                                    "minWidth": "80px",
                                },
                            ),
                            dbc.Input(
                                id="contact-title",
                                placeholder="Subject of your message",
                                type="text",
                                style={
                                    "backgroundColor": "#DCDEE4",
                                    "color": "#0A1930",
                                },
                            ),
                        ],
                        className="mb-3",
                    ),
                    # Message Section with Header
                    html.Div(
                        [
                            html.Label(
                                "Message",
                                htmlFor="contact-message",
                                style={
                                    "color": "#0A1930",
                                    "fontWeight": "bold",
                                    "marginBottom": "8px",
                                    "display": "block",
                                },
                            ),
                            dbc.Textarea(
                                id="contact-message",
                                placeholder="Enter your message...",
                                rows=5,
                                style={
                                    "backgroundColor": "#DCDEE4",
                                    "color": "#333",
                                    "border": "1px solid #ddd",
                                    "resize": "vertical",
                                },
                            ),
                        ],
                        className="mb-4",
                    ),
                    # Submit Button
                    dbc.Row(
                        dbc.Col(
                            dmc.Button(
                                "Send",
                                id="contact-submit-btn",
                                size="md",
                                variant="filled",
                                rightSection=DashIconify(
                                    icon="ri:send-plane-fill", color="#0A1930"
                                ),
                                className="send-button",
                            ),
                            width="auto",
                        ),
                        justify="end",
                        className="text-center",
                    ),
                    html.Div(id="contact-status"),
                ]
            ),
            withBorder=False,
            radius="lg",
            className="contact-group px-4",
            id="contact",
        ),
    )
