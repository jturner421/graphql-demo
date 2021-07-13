from flask import Flask

from api.config import DevelopmentConfig
from api.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    from api.data import all_models
    migrate.init_app(app, db, render_as_batch=True)

    with app.app_context():
        register_blueprints(app)
        # db.create_all()

    @app.shell_context_processor  # Decorator that returns items into a Flask shell session
    def shell_context():
        return {'app': app, 'db': db}

    return app


def register_blueprints(app):
    from api.views import home_views
    app.register_blueprint(home_views.blueprint)
    return app
