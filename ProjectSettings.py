from decouple import config

class Settings():
    DEBUG = None
    HOST = None
    PORT = None
    LOG_ENABLED = None
    LOG_SAVEBODY = None
    LOG_FILE_PATH = None
    LOG_FORMAT = None
    def __init__(self):
        """load all settings from .env file with the help of decouple
        """
        self.DEBUG = config('DEBUG', default=False, cast=bool)
        self.HOST = config('HOST', default='127.0.0.1', cast=str)
        self.PORT = config('PORT', default=8080, cast=int)
        self.LOG_ENABLED = config('LOG_ENABLED', default=False, cast=bool)
        self.LOG_FILE_PATH = config('LOG_FILE_PATH', default='debug.log', cast=str)
        self.LOG_FORMAT =  config('LOG_FORMAT', default='[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s', cast=str)
        self.LOG_SAVEBODY = config('LOG_SAVEBODY', default=False, cast=bool)
