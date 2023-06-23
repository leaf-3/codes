class Config(object):
    SECRET_KEY = 'secret_key!'
    DEBUG = True
    #数据库配置
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = '192.168.2.70'
    PORT = '3306'
    DATABASE = 'sys_shop'

    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)