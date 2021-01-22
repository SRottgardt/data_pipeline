class CommandData:

    def __init__(self, rows, option, optionValue, targetColumn, destinationColumn):
        self.Items = rows
        self.option = option
        self.optionValue = optionValue
        self.targetColumn = targetColumn
        self.destinationColumn = destinationColumn

    def getItems(self):
        return self.Items

    def getOption(self):
        return self.option

    def getOptionsValue(self):
        return self.optionValue

    def getTargetColumn(self):
        return self.targetColumn

    def getDestinationColumn(self):
        return self.destinationColumn

    def setItems(self, items):
        self.Items = items
