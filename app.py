from ProjectSettings import Settings
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
    
    def post(self):
        response = request.get_json()

        if (response is not None):

            # Check for items
            if "items" not in response:
                message = {"error": "json not contains items"}
                return message

            for idx, columnDataRow in enumerate(response["columnData"]):
                columnDataRowOption = columnDataRow["option"]
                print("Loading working row: {0} with method: {1}".format(idx, columnDataRowOption))

                # validate structure of json
                validateResult = self.validateColumnDataStructure(columnDataRow) 

                if validateResult is not None:
                    return validateResult
                 
                _commandData = CommandData(
                    response["items"], # json items
                    columnDataRowOption, # columnData -> option
                    columnDataRow["optionValue"], # columnData -> optionValue
                    columnDataRow["targetColumn"], # columnData -> targetColumn
                    columnDataRow["destinationColumn"]) # columnData -> destinationColumn

                for plugin in _plugins.getLoadedPlugins():
                    # Check for known plugin command in all loaded plugins
                    if columnDataRowOption in _plugins.getPluginsCommands():
                        # Match the plugincommand with the plugin 
                        if (plugin.pluginCommand == columnDataRowOption):
                            # set data
                            plugin.setData(_commandData)
                            # add worker
                            _worker.addJob(plugin)
                    else:
                        # no plugin command found -> add a unknown command job
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
            return message

    def validateColumnDataStructure(self, row: str) -> str:
        """
        Args:
            row (str): contains the json row with data

        Returns:
            str: returns a exception message or none
        """
        #check for optionValue
        if "optionValue" not in row:
            message = {"error": "json columnData not contains optionValue"}
            return message

        # check for targetColumn
        if "targetColumn" not in row:
            message = {"error": "json columnData not contains targetColumn"}
            return message

        # check for destinationColumn
        if "destinationColumn" not in row:
            message = {"error": "json columnData not contains destinationColumn"}
            return message

        # check for option
        if "option" not in row:
            message = {"error": "json columnData not contains option"}
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
    localsettings = Settings()
    app.run(host=localsettings.HOST, port=localsettings.PORT, debug=localsettings.DEBUG)
