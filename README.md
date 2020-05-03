# Virginia Covid Charter

The intent of this project is to provide covid spread at a county level for the state of Virginia. 

## Installation

```bash
cd covidcharter
pip install requirements.txt
```

## Usage
 With the current feature set, you must specify a county. If you do not include the county, a list of all possible counties will be given to you.
```bash
python3 main.py --county=Henrico
```

## Contributing
Pull requests are always welcome. 

## Use as a package
If you want to use parts of the service layer as a package, you may pull it as a backage from PyPi: https://pypi.org/project/covidcharter/

## License
[MIT](https://choosealicense.com/licenses/mit/)