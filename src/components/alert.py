import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


def create_warning_alert(message):
    return dbc.Alert(
        message,
        color="warning",
        dismissable=True,
        className="mt-3 text-center",
        style={"backgroundColor": "rgba(255, 193, 7, 0.3)", "color": "#e4ad06"},
    )


def create_success_alert(message):
    return dbc.Alert(
        [
            DashIconify(
                icon="lets-icons:check-fill",
                className="me-2",
                style={"color": "#32d157"},
            ),
            message,
        ],
        color="success",
        dismissable=True,
        className="mt-3 text-center",
        style={
            "backgroundColor": "rgba(40, 167, 69, 0.2)",
            "color": "#28a745",
        },
    )
