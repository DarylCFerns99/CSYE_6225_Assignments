from flask import request, Response, json, Blueprint
# from src.controllers.health_check_controller import health_check
from src import db
from sqlalchemy.sql import text

# main blueprint to be registered with application
api = Blueprint('', __name__)
# # register new routes with api blueprint
# api.register_blueprint(health_check, url_prefix="")

@api.route('/healthz')
def handle_check_health():
    resp = None
    try:
        # Check if payload has data
        if request.data:
            resp = Response(
                status=400,
                mimetype=None
            )
        else:
            # Check if database connection is established
            try:
                db.session.execute(text('SELECT 1'))
                resp = Response(
                    status=200,
                    mimetype=None
                )
            except Exception as e:
                resp = Response(
                    status=503,
                    mimetype=None
                )

    except Exception as e:
        resp = Response(
            status=500,
            mimetype=None
        )
    
    resp.headers['Cache-control'] = 'no-cache, no-store, must-revalidate'
    return resp