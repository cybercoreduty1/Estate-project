import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY","dev_secret_keys")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://postgres:password@localhost/smarthomesnija_db"
                                             )
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
