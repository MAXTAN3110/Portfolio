import os, smtplib
from pathlib import Path
from email.mime.text import MIMEText
import json
import dash
from dash import ctx, ALL, MATCH
from dash.dependencies import Input, Output, State
from dotenv import load_dotenv
from components.project_nav_buttons import create_project_nav_buttons
from components.alert import create_success_alert, create_warning_alert

src_dir = Path(__file__).parent.parent
json_path = src_dir / "project_config.json"
with open(json_path, "r") as f:
    PROJECTS = json.load(f)
PROJECT_IDS = [project["id"] for project in PROJECTS]

json_path = src_dir / "info_config.json"
with open(json_path, "r") as f:
    CONFIG = json.load(f)

# Load environment variables
load_dotenv()
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")


def register_server_callbacks(app):

    @app.callback(
        Output("navbar-collapse", "is_open"),
        Input("navbar-toggler", "n_clicks"),
        State("navbar-collapse", "is_open"),
    )
    def toggle_navbar_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open
        return is_open

    @app.callback(
        Output({"type": "nav-buttons-container", "project_id": ALL}, "children"),
        Input({"type": "nav-buttons-container", "project_id": ALL}, "id"),
    )
    def create_nav_buttons(container_ids):
        if not container_ids:
            return []

        results = []
        for container_id in container_ids:
            project_id = container_id["project_id"]
            buttons = create_project_nav_buttons(project_id, PROJECTS)
            results.append(buttons)
        return results

    # Callback for navigation button clicks
    @app.callback(
        Output("url", "pathname"),
        Input({"type": "nav-btn", "action": ALL, "project_id": ALL}, "n_clicks"),
        prevent_initial_call=True,
    )
    def navigate_projects(n_clicks_list):
        """
        Handle navigation button clicks
        """

        if not any(n_clicks_list) or not ctx.triggered:
            return dash.no_update

        # Get the triggered button info
        triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]
        button_info = json.loads(triggered_id)  # Convert string back to dict

        current_project_id = button_info["project_id"]
        action = button_info["action"]

        try:
            current_index = PROJECT_IDS.index(current_project_id)
        except ValueError:
            return dash.no_update

        # Navigate to appropriate project
        if action == "prev" and current_index > 0:
            target_project_id = PROJECT_IDS[current_index - 1]
            return f"/projects/{target_project_id}"
        elif action == "next" and current_index < len(PROJECT_IDS) - 1:
            target_project_id = PROJECT_IDS[current_index + 1]
            return f"/projects/{target_project_id}"

        return dash.no_update

    # Callback for Image Click and Modal Display
    @app.callback(
        [Output("image-modal", "opened"), Output("modal-image", "src")],
        Input({"type": "project-image", "src": ALL}, "n_clicks"),
        State({"type": "project-image", "src": ALL}, "id"),
        prevent_initial_call=True,
    )
    def show_modal(n_clicks_list, ids):
        triggered = ctx.triggered_id

        if any(n_clicks_list) and triggered and triggered["type"] == "project-image":
            return True, triggered["src"]
        return dash.no_update, dash.no_update

    # Callback for handling form submission
    @app.callback(
        Output("contact-status", "children"),
        Input("contact-submit-btn", "n_clicks"),
        [
            State("contact-name", "value"),
            State("contact-email", "value"),
            State("contact-title", "value"),
            State("contact-message", "value"),
        ],
        prevent_initial_call=True,
    )
    def handle_contact_form(n_clicks, name, email, title, message):
        """
        Handle contact form submission
        """
        if not n_clicks:
            return ""

        # Validate inputs
        if not all([name, email, title, message]):
            return create_warning_alert("Please fill in all fields before submitting.")

        # Basic email validation
        if "@" not in email or "." not in email:
            return create_warning_alert(
                "Please enter a valid email address.",
            )

        # Compose email
        msg = MIMEText(
            f"""
            Hello,

            You received a message from your portfolio site:

            Name: {name}
            Email: {email}
            Title: {title}

            Message:
            {message}
            """.strip(),
            "plain",
        )
        msg["Subject"] = title
        msg["From"] = SMTP_USER
        msg["To"] = CONFIG["email"]

        # Send email via SMTP
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.ehlo()
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
            server.quit()

        except Exception as e:
            return create_warning_alert(f"Failed to send email: {e}")

        return create_success_alert("Message sent successfully!")
