from flask import Flask, json, jsonify, request
from flask.views import MethodView
from Worker import Worker
from PluginCollection import PluginCollection
from modules.CommandData import CommandData
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
_plugins = PluginCollection('modules')
_worker = Worker()

class HandleData(MethodView):
    methods = ['POST']
    _commandData = None

    def post(self):
        response = request.get_json()
        if (response is not None):

            for idx, columnDataRow in enumerate(response["columnData"]):
                columnDataRowOption = columnDataRow["option"]
                print("Loading working row:{0} with method: {1}".format(idx, columnDataRowOption))
                _commandData = CommandData(response["items"], columnDataRowOption, columnDataRow["optionValue"],columnDataRow["targetColumn"], columnDataRow["destinationColumn"])

                for plugin in _plugins.getLoadedPlugins():
                    # Check for known plugin Command
                    if columnDataRowOption in _plugins.getPluginsCommands():
                        # Match for plugin execution
                        if (plugin.pluginCommand == columnDataRowOption):
                            # set data
                            plugin.setData(_commandData)
                            # add worker
                            _worker.addJob(plugin)
                    else:
                        # Unknown Command
                        unknownHandler = _plugins.getPluginByCommand("unknown")
                        unknownHandler.setData(_commandData)
                        _worker.addJob(unknownHandler)

                # run jobs
                _worker.executeJobs()

            # remove job que
            _worker.clearJobs()
            # return json resultset
            return jsonify(_commandData.getItems())
        else:
            message = {"error": "Request is empty"}
            print(request.json)
            return message




app.add_url_rule('/pipe/', view_func=HandleData.as_view('handledata'))


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
