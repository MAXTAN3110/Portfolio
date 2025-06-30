import json
from pathlib import Path
from dash import html
import dash_bootstrap_components as dbc
from components.project_card import create_project_grid

src_dir = Path(__file__).parent.parent
json_path = src_dir / "project_config.json"
with open(json_path, "r") as f:
    PROJECTS = json.load(f)


def create_project_section():
    layout = dbc.Container(
        [
            dbc.Row(
                [
                    html.Div(
                        [
                            html.H2(
                                "Projects",
                                className="text-center text-white pt-3 mb-2 fw-bold display-4",
                            ),
                            html.P(
                                "Check out these hands-on innovative projects that I've crafted.",
                                className="text-center mb-4",
                                style={
                                    "fontSize": "calc(1vw + 0.5rem)",
                                    "color": "rgba(255, 255, 255, 0.8)",
                                },
                            ),
                        ],
                        className="mb-3",
                    )
                ],
                style={"marginLeft": "5rem", "marginRight": "5rem"},
            ),
            dbc.Row(
                create_project_grid(PROJECTS),
                style={"marginLeft": "5rem", "marginRight": "5rem"},
            ),
        ],
        id="projects",
        fluid=True,
        className="py-5",
        style={"backgroundColor": "#0A1930", "minHeight": "100vh"},
    )

    return layout
