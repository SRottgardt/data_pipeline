# data_pipeline

data_pipeline is a Python library for dealing with datasets.
Another example to show the functionality of the data pipeline is the following, you can first clean the data using a regex then remove an unnecessary space. Additionally you can check if a certain value was found, once such a value was found further actions can be executed.

## Installation

1) Clone the repository
2) Change the environment variables in .env
```
HOST=0.0.0.0
#0.0.0.0 for all interfaces
#127.0.0.1 only for the same device
PORT=8080
LOG_ENABLED=TRUE #TRUE|FALSE
LOG_TYPE=FILE #NONE|FILE
# Only for LOG_TYPE FILE
LOG_FILE_PATH=log.log
LOG_FORMAT=('[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')
# Only for LOG_TYPE FILE
LOG_SAVEBODY=TRUE #TRUE|FALSE
DEBUG=TRUE #TRUE|FALSE
```
3) Install Dependencys in requirements.txt
```python
pip install -r requirements.txt 
```
4) Start the Flask Application
```python
python Start.py  
```
5) Manipulate Data

## Modules

data_pipeline is easy to extend, all functionalities are divided into modules.

The plugin system makes it very easy to add functionalities needed for editing data.

If you want to develop a plugin, the structure for a plugin is as follows:

Create a new File in modules/plugins with the name of your Plugin

Add this skeleton class to your file

```python
from modules.IPlugin  import IPlugin

class NewPlugin(IPlugin): # Rename your Class

    def __init__(self):
        super().__init__()
        self.pluginName = "Your Plugin Name"
        self.pluginAutor = "Your Name"
        self.pluginVersion = 0.1
        self.pluginDescription = "Your Description"
        self.pluginCommand = "your acronym"
        
    def preExecute(self):
        # do your stuff, open connections, read files
        self.execute()

    def execute(self):
        for rowsData in self.commandData.getItems():
        # do your stuff
        
    def postExecute(self):
        # do your stuff, close connection, close file
        pass

```    




## Usage

The individual steps run one after the other and can be combined, for example, a regex can be executed first on existing data, followed by a trim.

The structure of ColumnData must remain, the field option, optionValue, targetColumn and destinationColumn are mandatory fields.

The items array contains the data sets for data processing.

```
Send a JSON Request(POST) to the Flask Application Example:  http://127.0.0.1:8080/pipe/
Example:
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
```

Response:
```
        [
            {
                "digits": "XFRD-8324-ERWH-3231",
                "text": "XFRD-8324-ERWH-3231 Lorem ipsum dolor sit amet, consectetur! Maecenas sit amet tincidunt elit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames! Maecenas sit amet tincidunt elit.lor from lorem faucibus!"
            }
        ]
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Todo
* Dashboard
* Logging
* Different actions for certain events

## License

data_pipeline is distributed under Apache 2.0 with Commons Clause license.


