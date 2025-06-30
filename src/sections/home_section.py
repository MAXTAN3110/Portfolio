from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

with open("src/assets/bot.svg", "r") as f:
    bot_img = f.read()
bot_img = bot_img.replace('fill="#000000"', 'fill="#24DEF7"')


def create_home_section():

    layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H1(
                                [
                                    "Hi, I'm ",
                                    html.Span("Max", style={"color": "#24DEF7"}),
                                    ",",
                                    html.Br(),
                                    "Data Scientist & AI Professional.",
                                ],
                                className="display-4 fw-bold mb-4 text-white",
                            ),
                            html.P(
                                "I specialize in extracting valuable insights from complex datasets and deriving data-driven solutions.",
                                className="mb-4 text-white",
                                style={
                                    "lineHeight": "1.6",
                                    "fontSize": "calc(1vw + 0.7rem)",
                                },
                            ),
                            html.P(
                                "Whether you need comprehensive data analysis or cutting-edge AI insights, I bring technical expertise with real business impact—let's solve something meaningful together.",
                                className="mb-4",
                                style={
                                    "fontSize": "calc(1vw + 0.5rem)",
                                    "color": "rgba(255, 255, 255, 0.8)",
                                },
                            ),
                            dmc.Anchor(
                                dmc.Button(
                                    "Contact Me",
                                    id="contact-btn",
                                    variant="outline",
                                    size="lg",
                                    className="contact-btn mt-3",
                                    style={
                                        "width": "fit-content",
                                        "borderColor": "#24DEF7",
                                        "color": "#24DEF7",
                                        "borderWidth": "0.2rem",
                                    },
                                ),
                                href="#contact",
                            ),
                        ],
                        md=7,
                        className="d-flex flex-column justify-content-center px-5",
                    ),
                    # Right column - SVG Image
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.Img(
                                        src="/assets/bot.svg",  # Replace with your SVG filename
                                        className="w-100 h-auto",
                                        style={
                                            "maxWidth": "400px",
                                            "filter": (
                                                "brightness(0) "
                                                "saturate(100%) "
                                                "invert(64%) "
                                                "sepia(97%) "
                                                "saturate(912%) "
                                                "hue-rotate(150deg) "
                                                "brightness(105%) "
                                                "contrast(94%)"
                                            ),
                                        },
                                    )
                                ],
                                className="text-center",
                            )
                        ],
                        md=5,
                        className="d-flex align-items-center justify-content-center px-5",
                    ),
                ],
                className="align-items-center",
                style={
                    "minHeight": "80vh",
                    "marginTop": "-3.5rem",
                    "marginLeft": "5rem",
                    "marginRight": "5rem",
                    "paddingTop": "5rem",
                },
            )
        ],
        id="home",
        fluid=True,
        style={"backgroundColor": "#0A1930", "minHeight": "100vh"},
    )
    return layout
