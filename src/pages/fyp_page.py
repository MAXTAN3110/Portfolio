from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from components.carousel import create_carousel
from components.badge import create_tag_group


def create_fyp_layout(project):
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
                        "Explainable AI for Multivariate Time Series Analysis",
                        className="mb-4 fw-bold text-primary text-white",
                    ),
                    # Image display
                    dbc.Col(create_carousel(project)),
                    html.P(
                        [
                            "Final Year Project at Nanyang Technological University",
                            html.Br(),
                            "Awarded A- grade",
                        ],
                        className="mb-3 fst-italic",
                        style={
                            "fontSize": "calc(1vw + 0.3rem)",
                            "color": "rgba(255, 255, 255, 0.8)",
                        },
                    ),
                    # Project scope section
                    html.H3(
                        "Project Scope",
                        className="mb-2 fw-bold",
                        style={
                            "color": "#24DEF7",
                        },
                    ),
                    html.P(
                        [
                            "• Addressing the interpretability challenges of complex black-box AI models.",
                            html.Br(),
                            "• Overcoming limitations of traditional explanation methods for temporal multivariate data.",
                        ],
                        className="mb-3",
                        style={
                            "fontSize": "calc(1vw + 0.3rem)",
                            "color": "rgba(255, 255, 255, 0.8)",
                        },
                    ),
                    # Solution section
                    html.H3(
                        "Solutions",
                        className="mb-2 fw-bold",
                        style={
                            "color": "#24DEF7",
                        },
                    ),
                    html.H5(
                        "1. Conditional Time Variational Autoencoder (CTimeVAE):",
                        className="fw-bold",
                        style={"color": "rgba(255, 255, 255, 0.8)"},
                    ),
                    html.P(
                        "A specialized neural network architecture designed to model and reconstruct complex multivariate time-series data. CTimeVAE preserves temporal dependencies and captures underlying patterns by learning compact, informative representations that reflect the structure of sequential data.",
                        className="mb-3",
                        style={
                            "fontSize": "calc(1vw + 0.3rem)",
                            "color": "rgba(255, 255, 255, 0.8)",
                        },
                    ),
                    html.H5(
                        "2. Time-Enhanced Integrated Gradients (T-EIG):",
                        className="fw-bold",
                        style={"color": "rgba(255, 255, 255, 0.8)"},
                    ),
                    html.P(
                        "An extension of the Integrated Gradients explainability method, adapted for time-series models. T-EIG identifies the most influential features and time steps contributing to a model's prediction, providing more precise and temporally aware explanations of deep learning behavior in sequential data.",
                        className="mb-3",
                        style={
                            "fontSize": "calc(1vw + 0.3rem)",
                            "color": "rgba(255, 255, 255, 0.8)",
                        },
                    ),
                    # Methodology section
                    html.H3(
                        "How it Works",
                        className="mb-2 fw-bold",
                        style={"color": "#24DEF7"},
                    ),
                    html.P(
                        "The framework operates through a two-phase process: CTimeVAE first compresses the original time-series data into a compact, meaningful representation (latent vector) that preserve key temporal patterns. "
                        "This latent vector is subsequently transformed into reconstructed data and fed into an Long Short-Term Memory (LSTM) model for downstream prediction tasks. "
                        "T-EIG then calculates each feature's contribution based on both the latent vector and the final prediction output.",
                        className="mb-3",
                        style={
                            "fontSize": "calc(1vw + 0.3rem)",
                            "color": "rgba(255, 255, 255, 0.8)",
                        },
                    ),
                    # Impact section
                    html.H3(
                        "Impacts",
                        className="mb-2 fw-bold",
                        style={"color": "#24DEF7"},
                    ),
                    html.P(
                        [
                            "• Successfully bridging the gap between model performance and explainability in time-series analysis.",
                            html.Br(),
                            "• Improving complex AI decisions transparency and actionable for real-world applications.",
                        ],
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
                        id={
                            "type": "nav-buttons-container",
                            "project_id": project["id"],
                        },
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
