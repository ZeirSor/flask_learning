SECRET_KEY = 'FH2349THF2W347T89D'

HOSTNAME = '127.0.0.1'

PORT = '3306'

USERNAME = 'root'

PASSWORD = '1234'

DATABASE = 'py_orm'

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'

try:
    from .localsettings import *
except ImportError:
    pass
