from flask_restful import Resource
from sqlalchemy import text

from app.helpers.database import db


class IndexController(Resource):
    def get(self):
        return {"versao": "1.0.1"}, 200


class HealthController(Resource):
    def get(self):
        try:
            db.session.execute(text("SELECT 1"))

            return {
                "status": "healthy",
                "message": "Database connection verified."
            }, 200

        except Exception as e:
            return {
                "status": "unhealthy",
                "message": str(e)
            }, 500