from modules.IPlugin import IPlugin

class RemoveColumn(IPlugin):

    def __init__(self):
        super().__init__()
        self.pluginName = "RemoveColumn"
        self.pluginAutor = "Sebastian Rottgardt"
        self.pluginVersion = 0.1
        self.pluginDescription = "Remove a Column from dataset"
        self.pluginCommand = "removecolumn"
        self.commandData = None

    def preExecute(self):
        self.execute()

    def execute(self):
        message = []
        for rowsData in self.commandData.getItems():

            # check targetColumn exists
            if self.commandData.getTargetColumn() in rowsData:
                rowsData.pop(self.commandData.getTargetColumn(), None)
            else:
                rowsData[self.commandData.getTargetColumn()] = "targetColumn not exists"
            
            message.append(rowsData)

        if message is not None:
            self.commandData.setItems(message) 