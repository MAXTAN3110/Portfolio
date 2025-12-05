# api/index.py

import sys
import os

# make sure /src is in the path so imports work on Vercel
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from src.app import app as dash_app

# Vercel exposes this Flask server
app = dash_app.server
