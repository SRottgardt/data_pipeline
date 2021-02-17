from modules.IPlugin  import IPlugin

class IF_Columns_SmallerThan(IPlugin):

    def __init__(self):
        super().__init__()
        self.pluginName = "IF Columns Smaller Than"
        self.pluginAutor = "Sebastian Rottgardt"
        self.pluginVersion = 0.1
        self.pluginDescription = "adds a smaller than comparison statement between two data sets(columns), returns true or false"
        self.pluginCommand = "if-columns-smallerthan"
        
    def preExecute(self):
        self.execute()

    def execute(self):
        message = []
        for rowsData in self.commandData.getItems():

            # check targetColumn exists
            if self.commandData.getTargetColumn() in rowsData:
                
                if rowsData[self.commandData.getTargetColumn()] >= rowsData[self.commandData.getOptionsValue()]:
                    result = True
                else:
                    result = False

                rowsData[self.commandData.getDestinationColumn()] = result    
            else:
                rowsData[self.commandData.getTargetColumn()] = "targetColumn not exists"
            
            message.append(rowsData)

        if message is not None:
            self.commandData.setItems(message) 
