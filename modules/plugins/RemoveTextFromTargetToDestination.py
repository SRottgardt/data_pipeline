from os import remove
from modules.IPlugin  import IPlugin

class RemoveTextFromTargetToDestination(IPlugin):

    def __init__(self):
        super().__init__()
        self.pluginName = "RemoveTextFromTargetToDestination"
        self.pluginAutor = "Sebastian Rottgardt"
        self.pluginVersion = 0.1
        self.pluginDescription = "Remove Text from targetColum to Destination Column"
        self.pluginCommand = "removeText"
        
    def preExecute(self):
        self.execute()

    def execute(self):
        message = []

        for rowsData in self.commandData.getItems():

            # check targetColumn exists
            if self.commandData.getTargetColumn() in rowsData:
                rowsData[self.commandData.getDestinationColumn()] = rowsData[self.commandData.getTargetColumn()].replace(self.commandData.getOptionsValue(), '')
            else:
                rowsData[self.commandData.getTargetColumn()] = "targetColumn not exists"
            message.append(rowsData)
                
        if message is not None:
            self.commandData.setItems(message) 