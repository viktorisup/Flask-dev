from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from blog.admin.admin import admin
from blog.api import init_api
from blog.author.views import author
from blog.models.database import db
from blog.article.views import article
from blog.user.views import user
from blog.auth.views import auth, login_manager
# from blog.admin.views import admin_bp
import os


def create_app():
    app = Flask(__name__)
    cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
    app.config.from_object(f"blog.configs.{cfg_name}")

    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)

    admin.init_app(app)

    register_blueprints(app)

    login_manager.init_app(app)

    api = init_api(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)
    app.register_blueprint(author)


