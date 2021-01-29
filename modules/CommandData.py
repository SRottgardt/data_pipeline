class CommandData:

    def __init__(self, rows: str, option: str, optionValue: str, targetColumn: str, destinationColumn: str):
        """Example of a CommandData JSON Body
      {
        "columnData": [
            {
                "option": "regex",
                "optionValue": "([a-zA-Z]{4}-[0-9]{4}-[a-zA-Z]{4}-[0-9]{4})",
                "targetColumn": "text",
                "destinationColumn": "digits"
            },
            {
                "option": "trim",
                "optionValue": "",
                "targetColumn": "digits",
                "destinationColumn": "digits"
            }
        ],
        "items": [
            {
                "text": "XFRD-8324-ERWH-3231 Lorem ipsum dolor sit amet, consectetur! Maecenas sit amet tincidunt elit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames! Maecenas sit amet tincidunt elit.lor from lorem faucibus!"
            }
        ]
    }

    results in a response in following format
        [
            {
                "digits": "XFRD-8324-ERWH-3231",
                "text": "XFRD-8324-ERWH-3231 Lorem ipsum dolor sit amet, consectetur! Maecenas sit amet tincidunt elit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames! Maecenas sit amet tincidunt elit.lor from lorem faucibus!"
            }
        ]

        Args:
            rows (str): represent the items json array
            option (str): represent the columnData option value
            optionValue (str): represent the columnData optionValue
            targetColumn (str): represent the columnData targetColumn
            destinationColumn (str): represent the columnData destinationColumn
        """
        self.Items = rows
        self.option = option
        self.optionValue = optionValue
        self.targetColumn = targetColumn
        self.destinationColumn = destinationColumn

    # represent the columnData array value of option
    def getOption(self):
        return self.option

    # represent the columnData array value of optionValue
    def getOptionsValue(self):
        return self.optionValue

    # represent the columnData array value of targetColumn
    def getTargetColumn(self):
        return self.targetColumn

    # represent the columnData array value of destionationColumn
    def getDestinationColumn(self):
        return self.destinationColumn

    # set the value of items array
    def setItems(self, items):
        self.Items = items

    # represent the items array value
    def getItems(self):
        return self.Items
