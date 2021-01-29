import re
from modules.IPlugin import IPlugin

class RegexFromTargetToDestination(IPlugin):

    def __init__(self):
        super().__init__()
        self.pluginName = "RegExFromTargetToDestination"
        self.pluginAutor = "Sebastian Rottgardt"
        self.pluginVersion = 0.1
        self.pluginDescription = "Execute Regex Pattern from Target Column and write the found Match to Destination Column"
        self.pluginCommand = "regex"
        self.commandData = None

    def preExecute(self):
        self.execute()

    def execute(self):
        message = []
        for rowsData in self.commandData.getItems():

            # check targetColumn exists
            if self.commandData.getTargetColumn() in rowsData:

                result = re.search(self.commandData.getOptionsValue(), rowsData[self.commandData.getTargetColumn()])
                if(result):
                    result = result.group(1)
                else:
                    result = ''
                rowsData[self.commandData.getDestinationColumn()] = result
            else:
                rowsData[self.commandData.getTargetColumn()] = "targetColumn not exists"
            
            message.append(rowsData)

        if message is not None:
            self.commandData.setItems(message) 