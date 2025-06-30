import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc


def create_project_card(project):
    """Component to create individual project card with hover effects"""
    return dmc.Card(
        children=[
            html.Div(
                [
                    dcc.Link(
                        [
                            # Project cover image
                            html.Img(
                                src=dash.get_asset_url(project["cover"]),
                                className="project-cover w-100 h-100",
                            ),
                            # Overlay with project title (hidden by default)
                            html.Div(
                                [
                                    html.H4(
                                        project["title"],
                                        className="text-center mb-0 fw-bold",
                                        style={"color": "#24DEF7"},
                                    )
                                ],
                                className="project-overlay position-absolute top-0 start-0 w-100 h-100 d-flex flex-column justify-content-center align-items-center rounded",
                            ),
                        ],
                        href=f"/projects/{project['id']}",
                    )
                ],
                className="project-card-container position-relative overflow-hidden",
            )
        ],
        withBorder=False,
        radius="lg",
        className="project-card mx-3 mb-3",
        style={"padding": "0"},
        id={"type": "project-card", "index": project["id"]},
    )


def create_project_grid(projects):
    """Component to create responsive grid of project cards"""
    # Split projects into pairs for two columns
    project_pairs = [projects[i : i + 2] for i in range(0, len(projects), 2)]

    rows = []
    for pair in project_pairs:
        cols = []
        for project in pair:
            cols.append(
                dbc.Col(create_project_card(project), xs=12, sm=12, md=6, lg=6, xl=6)
            )
        # If odd number of projects, fill the last row
        if len(pair) == 1:
            cols.append(dbc.Col())

        rows.append(dbc.Row(cols, className="mb-3"))

    return html.Div(rows)
