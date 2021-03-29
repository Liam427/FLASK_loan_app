from flask import Flask
# from loan_app.routes import main_routes#, func_routes
from loan_app.models import db, migrate


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = "APP_SECRETKEY"

    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # from loan_app import util
    # util.get_loan_api()
    # db.session.commit()
    
    from loan_app.routes import main_routes
    app.register_blueprint(main_routes.mainbp)
    # app.register_blueprint(func_routes.func_routes, url_prefix='/menu')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
