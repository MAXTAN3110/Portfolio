import dash_bootstrap_components as dbc
from dash import html
from dash_iconify import DashIconify


def create_navbar():
    """
    Creates a responsive navbar for portfolio website with collapsible navigation
    """
    navbar = dbc.Navbar(
        dbc.Container(
            [
                # Left side - Brand/Header
                dbc.NavbarBrand("Max Tan", href="/", className="fw-bold fs-4 ms-3"),
                # Toggle button for mobile
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                # Collapsible navigation section
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(
                                dbc.NavLink(
                                    [
                                        DashIconify(icon="mdi:home", className="me-2"),
                                        html.Span("Home", className="fw-bold"),
                                    ],
                                    href="#home",
                                    external_link=True,
                                    className="d-flex align-items-center justify-content-center px-3",
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    [
                                        DashIconify(
                                            icon="mdi:account", className="me-2"
                                        ),
                                        html.Span("About", className="fw-bold"),
                                    ],
                                    href="#about",
                                    external_link=True,
                                    className="d-flex align-items-center justify-content-center px-3",
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    [
                                        DashIconify(
                                            icon="mdi:code-braces", className="me-2"
                                        ),
                                        html.Span("Projects", className="fw-bold"),
                                    ],
                                    href="#projects",
                                    external_link=True,
                                    className="d-flex align-items-center justify-content-center px-3",
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    [
                                        DashIconify(icon="mdi:email", className="me-2"),
                                        html.Span("Contact", className="fw-bold"),
                                    ],
                                    href="#contact",
                                    external_link=True,
                                    className="d-flex align-items-center justify-content-center px-3",
                                )
                            ),
                        ],
                        className="ms-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ],
            fluid=True,
        ),
        color="#19335A",
        dark=True,
        sticky="top",
    )

    return navbar
