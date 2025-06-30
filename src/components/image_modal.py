import dash
from dash import dcc, html
import dash_mantine_components as dmc


def create_image_modal():
    return dmc.Modal(
        id="image-modal",
        size="75%",
        centered=True,
        opened=False,
        withCloseButton=True,
        children=html.Img(
            id="modal-image",
            className="w-100 h-auto rounded",
        ),
    )
