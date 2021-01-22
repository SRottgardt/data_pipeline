from modules.IPlugin import IPlugin

class TrimFromTargetToDestination(IPlugin):

    def __init__(self):
        super().__init__()
        self.pluginName = "TrimFromTargetToDestination"
        self.pluginAutor = "Sebastian Rottgardt"
        self.pluginVersion = 0.1
        self.pluginDescription = "Execute Trim Method from Target Column and write the new Value to Destination Column"
        self.pluginCommand = "trim"
        self.commandData = None
        
    def preExecute(self):
        self.execute()

    def execute(self):
        message = []

        for rowsData in self.commandData.getItems():
            rowsData[self.commandData.getDestinationColumn()] = rowsData[self.commandData.getTargetColumn()].strip()
            message.append(rowsData)

        if message is not None:
            self.commandData.setItems(message) 