import dash
import json
from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from components.carousel import create_carousel
from components.badge import create_tag_group
from pages.fyp_page import create_fyp_layout

dash.register_page(__name__, path_template="/projects/<project_id>", name="Project")

with open("src/project_config.json") as f:
    projects = {p["id"]: p for p in json.load(f)}


def layout(project_id=1):
    project = projects.get(project_id)

    if not project:
        return html.Div("Project not found", className="text-danger")

    # custom page for fyp
    if project_id == "final-year-project":
        return create_fyp_layout(project)

    description = [project["description"]]
    if "external_link" in project:
        description.append(" ")
        description.append(
            html.A(
                "More Details...",
                href=project["external_link"],
                target="_blank",
                style={"color": "#0084FF", "textDecoration": "underline"},
            )
        )

    return dbc.Container(
        [
            dbc.Row(
                [
                    html.Div(
                        # Back button
                        dmc.Anchor(
                            dmc.Button(
                                "← Back",
                                id="back-btn",
                                variant="outline",
                                size="md",
                                color="#24DEF7",
                                style={"borderWidth": "0.15rem"},
                                className="mb-3",
                            ),
                            href="/",
                        )
                    ),
                    # Project title
                    html.H1(
                        project["title"],
                        className="mb-4 fw-bold text-primary text-white",
                    ),
                    # Image display
                    dbc.Col(create_carousel(project)),
                    # Description section
                    html.H3(
                        "Description",
                        className="mb-2 fw-bold",
                        style={
                            "color": "#24DEF7",
                        },
                    ),
                    html.P(
                        description,
                        className="mb-3",
                        style={
                            "fontSize": "calc(1vw + 0.3rem)",
                            "color": "rgba(255, 255, 255, 0.8)",
                        },
                    ),
                    # Skills & Tools section
                    html.H3(
                        "Skills & Tools",
                        className="mb-2 fw-bold",
                        style={"color": "#24DEF7"},
                    ),
                    create_tag_group(project["skills_tools"], "indigo", "cyan"),
                    # Keywords section
                    html.H3(
                        "Keywords",
                        className="mb-2 fw-bold",
                        style={"color": "#24DEF7"},
                    ),
                    create_tag_group(project["keywords"], "#24DEF7", "teal"),
                    html.Div(
                        id={"type": "nav-buttons-container", "project_id": project_id},
                        className="mt-5 mb-4",
                    ),
                ],
                style={
                    "marginLeft": "5rem",
                    "marginRight": "5rem",
                    "paddingTop": "1rem",
                },
            ),
        ],
        fluid=True,
        style={
            "backgroundColor": "#0A1930",
        },
    )
