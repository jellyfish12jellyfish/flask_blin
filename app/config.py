from password_login import my_password, my_key


class Configuration(object):
    DEBUG = True
    STATIC_URL = '/static/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:' + my_password + '@localhost/test'
    SECRET_KEY = my_key

    ### flask security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
