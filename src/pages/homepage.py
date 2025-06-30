import dash
from dash import html
from sections import (
    about_section,
    home_section,
    projects_section,
    contact_section,
    footer_section,
)

dash.register_page(__name__, path="/", name="Home")


layout = html.Div(
    [
        # navbar.create_navbar(),
        home_section.create_home_section(),
        about_section.create_about_section(),
        projects_section.create_project_section(),
        contact_section.create_contact_section(),
        footer_section.create_footer_section(),
    ]
)

