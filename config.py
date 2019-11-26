import logging
import os

logger = logging.getLogger(__name__)


class DevelopmentConfig(object):
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/db.sqlite"

    HOST = "localhost"
    PORT = "5000"
    SECRET_KEY = "test"
    ENCRYPTION_KEY = "test"

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
