from config import app
from flask_restful import Api

__all__ = ["api"]

api = Api(app)