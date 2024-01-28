from flask import request, Response, json, Blueprint
from src import db
from sqlalchemy.sql import text

# user controller blueprint to be registered with api blueprint
health_check = Blueprint("healthcheck", __name__)

# updating headers after completion
@health_check.after_app_request
def add_header(response):
    response.headers["Cache-control"] = "no-cache, no-store, must-revalidate"
    # Pragma cache is depreciated and only used for backward compatibility  HTTP/1.0
    response.headers["Pragma"] = "no-cache"
    # X-Content-Type-Options is used to indicate the content-type
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response

# removing body data from 405 method response
@health_check.app_errorhandler(405)
def special_exception_handler(error):
    return Response(status=405)

@health_check.route('/healthz', methods = ["GET"])
def handle_check_health():
    try:
        # Check if payload has data
        if request.data:
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