import dash
import dash_mantine_components as dmc
from dash import html


def create_badge_components(skill):
    return html.Div(
        [
            html.H6(
                skill["section_title"],
                className="mb-3 text-white",
                style={"fontSize": "calc(1vw + 0.3rem)"},
            ),
            html.Div(
                [
                    create_badge(tool["label"], tool["color"], tool["avatar"])
                    for tool in skill["tools"]
                ],
                className="mb-3",
            ),
        ]
    )


def create_badge(label, color, avatar_src, variant="outline"):
    return dmc.Badge(
        label,
        color=color,
        variant=variant,
        size="lg",
        leftSection=dmc.Avatar(src=dash.get_asset_url(avatar_src), size="xs"),
        className="badge-type-1 me-2 mb-2",
    )


def create_tag_group(items, color1="indigo", color2="cyan"):
    """Component to create a group of tags"""
    return html.Div(
        [
            dmc.Badge(
                item,
                variant="gradient",
                gradient={"from": color1, "to": color2},
                size="xl",
                className="me-2 mb-2 badge-type-2",
            )
            for item in items
        ],
        className="d-flex flex-wrap",
    )
