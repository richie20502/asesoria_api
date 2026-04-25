import os 
class  Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost/users_db"
        );
    SQLALCHEMY_TRACK_MODIFICATIONS = False