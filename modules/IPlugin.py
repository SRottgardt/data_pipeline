from modules.CommandData import CommandData

class IPlugin(object):
    def __init__(self):

        self.pluginName = ""
        self.pluginAutor = ""
        self.pluginVersion = 0
        self.pluginDescription = ""
        self.pluginCommand = ""
        self.commandData = None

    def setData(self, _commandData):
        self.commandData = _commandData

    def preExecute(self):
        print("preExecute not overriden")
        self.execute()

    def execute(self):
        print("execute not overriden")
        self.postExecute()

    def postExecute(self):
        print("postExecute not overriden")
