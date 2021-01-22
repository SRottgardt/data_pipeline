from modules.IPlugin  import IPlugin

class AddTextFromTargetToDestination(IPlugin):

    def __init__(self):
        super().__init__()
        self.pluginName = "AddTextFromTargetToDestination"
        self.pluginAutor = "Sebastian Rottgardt"
        self.pluginVersion = 0.1
        self.pluginDescription = "Add Text to Destination Column"
        self.pluginCommand = "addText"
        
    def preExecute(self):
        self.execute()

    def execute(self):
        message = []

        for rowsData in self.commandData.getItems():
            rowsData[self.commandData.getDestinationColumn()] = rowsData[self.commandData.getTargetColumn()] + str(self.commandData.getOptionsValue())
            message.append(rowsData)
                
        if message is not None:
            self.commandData.setItems(message) 