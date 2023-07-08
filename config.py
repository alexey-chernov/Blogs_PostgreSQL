import os
import psycopg2



class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY") or "remember-to-add-secret-key"
    SQLALCHEMY_DATABASE_URI = (
        'postgresql+psycopg2://blogsadmin:blogsbase@10.66.66.1/blogs'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "change-me")
