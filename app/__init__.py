from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	db.init_app(app)
	migrate.init_app(app, db)
	mail.init_app(app)

	from app.api import bp as api_bp
	app.register_blueprint(api_bp, url_prefix='/api')

	# if not app.debug:
	# 	if app.config['MAIL_SERVER']:
	# 		auth = None
	# 		if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
	# 			auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
	# 			secure = None
	# 		if app.config['MAIL_USE_TLS']:
	# 			secure = ()

	return app


from app import models
