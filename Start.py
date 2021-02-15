import os
from gevent.pywsgi import WSGIServer
from app import app
from ProjectSettings import Settings

_localsettings = Settings()
http_server = WSGIServer((_localsettings.HOST, _localsettings.PORT), app)
http_server.serve_forever()
