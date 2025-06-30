import json
from pathlib import Path
import dash_bootstrap_components as dbc
from dash import html
from dash_iconify import DashIconify
from components.badge import create_badge_components

src_dir = Path(__file__).parent.parent
json_path = src_dir / "skill_config.json"
with open(json_path, "r") as f:
    SKILLS = json.load(f)


def create_about_section():
    """
    Creates the about me section with structured content
    """
    layout = dbc.Container(
        [
            # Section Header
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2(
                                "About Me",
                                className="text-center pt-3 mb-2 fw-bold display-4",
                                style={"color": "white"},
                            )
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    # Brief Introduction
                    html.Div(
                        [
                            html.H4(
                                "Background",
                                className="mb-3 fw-bold",
                                style={
                                    "color": "#24DEF7",
                                    "fontSize": "calc(1vw + 0.6rem)",
                                },
                            ),
                            html.P(
                                "I am a dedicated data analyst & machine learning enthusiast located in Singapore. "
                                "I'm passionate about discovering patterns in complex data, using AI to address real challenges, and developing analytical solutions that turn information into action. "
                                "With strong numerical instinct and problem-solving skills, "
                                "I aspire to bridge the gap between raw data and strategic business decisions, "
                                "helping organizations leverage their data assets to drive growth and innovation.",
                                className="mb-4",
                                style={
                                    "color": "rgba(255, 255, 255, 0.9)",
                                    "fontSize": "calc(1vw + 0.25rem)",
                                    "lineHeight": "1.7",
                                },
                            ),
                        ],
                        className="mb-3",
                    ),
                ],
                style={"marginLeft": "5rem", "marginRight": "5rem"},
            ),
            dbc.Row(
                [
                    # Left Column - Introduction & Education/Experience/Coursework
                    dbc.Col(
                        [
                            # Education
                            html.Div(
                                [
                                    html.H4(
                                        [
                                            DashIconify(
                                                icon="mdi:school",
                                                className="me-3",
                                                style={"color": "#24DEF7"},
                                            ),
                                            "Education",
                                        ],
                                        className="mb-3 fw-bold d-flex align-items-center",
                                        style={
                                            "color": "#24DEF7",
                                            "fontSize": "calc(1vw + 0.6rem)",
                                        },
                                    ),
                                    html.P(
                                        [
                                            "Bachelor of Science in Data Science & Artificial Intelligence at Nanyang Technological University",
                                            html.Br(),
                                            "(Aug 2021 - May 2025)",
                                        ],
                                        className="mb-4",
                                        style={
                                            "color": "rgba(255, 255, 255, 0.9)",
                                            "fontSize": "calc(1vw + 0.3rem)",
                                            "paddingLeft": "2.5rem",
                                        },
                                    ),
                                ],
                                className="mb-3",
                            ),
                            # Work Experience
                            html.Div(
                                [
                                    html.H4(
                                        [
                                            DashIconify(
                                                icon="mdi:briefcase",
                                                className="me-3",
                                                style={"color": "#24DEF7"},
                                            ),
                                            "Experience",
                                        ],
                                        className="mb-3 fw-bold d-flex align-items-center",
                                        style={
                                            "color": "#24DEF7",
                                            "fontSize": "calc(1vw + 0.6rem)",
                                        },
                                    ),
                                    html.P(
                                        [
                                            "Data Analyst Intern at Tokyo Electon Singpapore Pte. Ltd.",
                                            html.Br(),
                                            "(Jan 2024 - July 2024)",
                                        ],
                                        className="mb-4",
                                        style={
                                            "color": "rgba(255, 255, 255, 0.9)",
                                            "fontSize": "calc(1vw + 0.3rem)",
                                            "paddingLeft": "2.5rem",
                                        },
                                    ),
                                ],
                                className="mb-3",
                            ),
                            # Coursework
                            html.Div(
                                [
                                    html.H4(
                                        [
                                            DashIconify(
                                                icon="mdi:book-open-blank-variant",
                                                className="me-3",
                                                style={"color": "#24DEF7"},
                                            ),
                                            "Courseworks",
                                        ],
                                        className="mb-3 fw-bold d-flex align-items-center",
                                        style={
                                            "color": "#24DEF7",
                                            "fontSize": "calc(1vw + 0.6rem)",
                                        },
                                    ),
                                    html.P(
                                        """Algorithms Design, Data Analytics, Data Science, Data Visualization, Data Mining,
                                        Database Management System, Machine Learning, 
                                        Deep Learning, Natural Language Processing""",
                                        className="mb-4",
                                        style={
                                            "color": "rgba(255, 255, 255, 0.9)",
                                            "fontSize": "calc(1vw + 0.3rem)",
                                            "paddingLeft": "2.5rem",
                                        },
                                    ),
                                ],
                                className="mb-3",
                            ),
                        ],
                        md=6,
                        className="px-4",
                    ),
                    # Right Column - Skills & Tools
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.H4(
                                        [
                                            DashIconify(
                                                icon="mdi:tools",
                                                className="me-3",
                                                style={"color": "#24DEF7"},
                                            ),
                                            "Skills & Tools",
                                        ],
                                        className="mb-3 fw-bold d-flex align-items-center",
                                        style={
                                            "color": "#24DEF7",
                                            "fontSize": "calc(1vw + 0.6rem)",
                                        },
                                    ),
                                    html.Div(
                                        [
                                            create_badge_components(skill)
                                            for skill in SKILLS
                                        ]
                                    ),
                                ]
                            )
                        ],
                        md=6,
                        className="px-4",
                    ),
                ],
                className="align-items-start",
                style={"marginLeft": "5rem", "marginRight": "5rem"},
            ),
        ],
        id="about",
        fluid=True,
        className="py-5",
        style={"backgroundColor": "#0A1930", "minHeight": "100vh"},
    )

    return layout
