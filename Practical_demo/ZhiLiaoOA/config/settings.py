import datetime

# 设置session
SECRET_KEY = 'FH2349THF2W347T89D'
# 设置session过期时间
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=7)

# database info config
HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '1234'
DATABASE = 'zhiliaooa'
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'


# email config
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '1418681525@qq.com'
MAIL_PASSWORD = 'lmxvvsbpvfsuggjd'
MAIL_DEFAULT_SENDER = '1418681525@qq.com'


try:
    from .localsettings import *
except ImportError:
    pass
