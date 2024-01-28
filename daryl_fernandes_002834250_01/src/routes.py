from flask import request, Response, Blueprint
# from src.controllers.health_check_controller import health_check
from src import db
from sqlalchemy.sql import text

# main blueprint to be registered with application
api = Blueprint('', __name__)
# # register new routes with api blueprint
# api.register_blueprint(health_check, url_prefix="")

# updating headers after completion
@api.after_app_request
def add_header(response):
    response.headers["Cache-control"] = "no-cache, no-store, must-revalidate"
    # Pragma cache is depreciated and only used for backward compatibility  HTTP/1.0
    response.headers["Pragma"] = "no-cache"
    # X-Content-Type-Options is used to indicate the content-type
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response

# removing body data from 405 method response
@api.app_errorhandler(405)
def special_exception_handler(error):
    return Response(
        status=405
    )

@api.route('/healthz', methods = ["GET"])
def handle_check_health():
    try:
        # Check if payload or query params are present in request body
        if request.data or request.args:
            return Response(status=400)
        else:
            # Check if database connection is established
            try:
                db.session.execute(text('SELECT 1'))
                return Response(status=200)
            except Exception as e:
                return Response(status=503)

    except Exception as e:
        return Response(status=500)