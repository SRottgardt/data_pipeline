from decouple import config

class Settings():
    DEBUG = None
    HOST = None
    PORT = None
    LOG_ENABLED = None
    LOG_SAVEBODY = None
    
    def __init__(self):
        """load all settings from .env file with the help of decouple
        """
        self.DEBUG = config('DEBUG', default=False, cast=bool)
        self.HOST = config('HOST', default='127.0.0.1', cast=str)
        self.PORT = config('PORT', default=8080, cast=int)
        self.LOG_ENABLED = config('LOG_ENABLED', default=False, cast=bool)
        self.LOG_SAVEBODY = config('LOG_SAVEBODY', default=False, cast=bool)
