# data_pipeline

data_pipeline is a Python library for dealing with datasets.


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
LOG_SAVEBODY=TRUE #TRUE|FALSE
DEBUG=TRUE #TRUE|FALSE
```
3) Install Dependencys in requirements.txt
```python
pip install -r requirements.txt 
```
4) Start the Flask Application
```python
python start.py  
```
5) Manipulate Data

## Modules

data_pipeline is easy to extend, all functionalities are divided into modules.

The plugin system makes it very easy to add functionalities needed for editing data.


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

## License
