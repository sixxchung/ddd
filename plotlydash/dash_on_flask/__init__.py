"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment

def init_dash_APP_on_flask():
    """Construct core Flask application with embedded Dash app."""
    app_flask = Flask(__name__, instance_relative_config=False)
    #app_flask.config.from_object("config.Config")
    #assets = Environment()
    #assets.init_app(app_flask)

    with app_flask.app_context():
        # Import parts of our core Flask app
        #from . import routes
        #from .assets import compile_static_assets

        # Import Dash application
        from .dashboard import init_dashboard

        dash_app = init_dashboard(server=app_flask)

        # Compile static assets
        #compile_static_assets(assets)

        return dash_app
