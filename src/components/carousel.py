import dash
from dash import html
import dash_mantine_components as dmc


def create_carousel(project):
    # Create image display - carousel if multiple images, single image if one
    if len(project["images"]) > 1:
        image_display = dmc.Carousel(
            [
                dmc.CarouselSlide(
                    html.Img(
                        src=dash.get_asset_url(img),
                        id={"type": "project-image", "src": dash.get_asset_url(img)},
                        n_clicks=0,
                        className="w-100 project-image",
                    )
                )
                for img in project["images"]
            ],
            withIndicators=True,
            withControls=True,
            controlsOffset="xs",
            className="mb-4",
            style={"maxWidth": "100%"},
            classNames={"indicator": "dmc-indicator"},
        )
    else:
        image_display = html.Img(
            src=dash.get_asset_url(project["images"][0]),
            id={
                "type": "project-image",
                "src": dash.get_asset_url(project["images"][0]),
            },
            n_clicks=0,
            className="w-100 mb-4 project-image",
        )

    return image_display
