import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import html
from dash_iconify import DashIconify


def create_project_nav_buttons(current_project_id, projects):
    """
    Generate navigation buttons based on current project position
    """
    project_ids = [project["id"] for project in projects]

    try:
        current_index = project_ids.index(current_project_id)
    except ValueError:
        # If project_id not found, return empty div
        return html.Div()

    buttons = []
    has_prev = current_index > 0
    has_next = current_index < len(project_ids) - 1
    # Determine justification class based on which buttons are present
    if has_prev and has_next:
        justify_class = "between"
    elif has_next:  # Only next button
        justify_class = "end"
    elif has_prev:  # Only prev button
        justify_class = "start"
    else:
        return html.Div()  # No buttons if single project

    # Previous button (only if not first project)
    if has_prev:
        prev_project_id = project_ids[current_index - 1]
        buttons.append(
            dbc.Col(
                dmc.Button(
                    "Previous",
                    id={
                        "type": "nav-btn",
                        "action": "prev",
                        "project_id": current_project_id,
                    },
                    variant="outline",
                    size="md",
                    color="#24DEF7",
                    leftSection=DashIconify(icon="mingcute:left-line"),
                    style={"borderWidth": "0.15rem"},
                ),
                width="auto",
            )
        )
    # Next button (only if not last project)
    if has_next:
        next_project_id = project_ids[current_index + 1]
        buttons.append(
            dbc.Col(
                dmc.Button(
                    "Next",
                    id={
                        "type": "nav-btn",
                        "action": "next",
                        "project_id": current_project_id,
                    },
                    variant="outline",
                    size="md",
                    color="#24DEF7",
                    rightSection=DashIconify(icon="mingcute:right-line"),
                    style={"borderWidth": "0.15rem"},
                ),
                width="auto",
            )
        )

    return dbc.Row(buttons, justify=justify_class, className="g-3")
