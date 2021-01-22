from modules.IPlugin import IPlugin

class UnknownCommand(IPlugin):

    def __init__(self):
        super().__init__()
        self.pluginName = "UnknownCommand"
        self.pluginAutor = "Sebastian Rottgardt"
        self.pluginVersion = 0.1
        self.pluginDescription = "Unknown Command Handler"
        self.pluginCommand = "unknown"
        self.commandData = None
        
    def preExecute(self):
        self.execute()

    def execute(self):

        message = []
        for rowsData in self.commandData.getItems():
            result = "Command unknown for action={0}.".format(self.commandData.getOption())
            rowsData[self.commandData.destinationColumn] = result
            
            message.append(rowsData)
            
        self.commandData.setItems(message) 
        return message