from modules.IPlugin  import IPlugin

class IF_GreaterThan(IPlugin):

    def __init__(self):
        super().__init__()
        self.pluginName = "IF - Greater Than"
        self.pluginAutor = "Sebastian Rottgardt"
        self.pluginVersion = 0.1
        self.pluginDescription = "adds one larger than comparison ( targetColumn first - OptionsValue second), returns true or false"
        self.pluginCommand = "if-greaterthan"
        
    def preExecute(self):
        self.execute()

    def execute(self):
        message = []
        for rowsData in self.commandData.getItems():

            # check targetColumn exists
            if self.commandData.getTargetColumn() in rowsData:
       
                if int(rowsData[self.commandData.getTargetColumn()]) > int(self.commandData.getOptionsValue()):
                    result = True
                else:
                    result = False
                    
                rowsData[self.commandData.getDestinationColumn()] = result    
            else:
                rowsData[self.commandData.getTargetColumn()] = "targetColumn not exists"
            
            message.append(rowsData)

        if message is not None:
            self.commandData.setItems(message) 
    


