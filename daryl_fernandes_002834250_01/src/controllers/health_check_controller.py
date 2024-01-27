from flask import request, Response, json, Blueprint
from src import db
from sqlalchemy.sql import text

# user controller blueprint to be registered with api blueprint
health_check = Blueprint("healthcheck", __name__)

# route for login api/users/signin
@health_check.route('/healthz', methods = ["GET"])
def handle_check_health():
    try:
        # Check if payload has data
        if request.data:
            return Response(
                status=400,
                mimetype=None
            )
        
        # Check if database connection is established
        try:
            db.session.execute(text('SELECT 1'))
            return Response(
                status=200,
                mimetype=None
            )
        except Exception as e:
            return Response(
                status=503,
                mimetype=None
            )

    except Exception as e:
        return Response(
            status=500,
            mimetype=None
        )