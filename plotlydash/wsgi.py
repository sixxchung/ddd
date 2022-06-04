"""Application entry point."""
from dash_on_flask import init_dash_APP_on_flask

app = init_dash_APP_on_flask()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
