from modules.CommandData import CommandData

class IPlugin(object):
    def __init__(self):
        """create the plugin interface
        """
        self.pluginName = ""
        self.pluginAutor = ""
        self.pluginVersion = 0
        self.pluginDescription = ""
        self.pluginCommand = ""
        self.commandData = None

    def setData(self, _commandData):
        """

        Args:
            _commandData ([CommandData]): load the data from pipeline 
        """
        self.commandData = _commandData

    def preExecute(self):
        """method for preparing your data, load stuff, get information from other sources 
        """
        print("preExecute not overriden")
        self.execute()

    def execute(self):
        """manipulate data and do your stuff
        """
        print("execute not overriden")
        self.postExecute()

    def postExecute(self):
        """method for closing your connections/files 
        """
        print("postExecute not overriden")
