# UK Postcode
This program supports validating and formatting post codes for UK. 
For more details, check: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting  

A pilot script (script.py) is provided in order to demonstrate in a simple manner the usage of the formatter, validator.  
Also the tests provided help in the understanding of the usage, in case you want to use the library on your project.    

A pipeline on github actions was added.

### Setup
It is recommended to create a venv to run the project.  
To do that, please execute the following commands:  
```
pip install virtualenv  
virtualenv venv  
source venv/bin/activate  
pip install -r ./requirements.txt  
```

### Run the script 
    usage: script.py [-h] [-v TYPE VALUE] [-f]  

      -h, --help            show this help message and exit  
      -v VALIDATE VALIDATE, --validate VALIDATE VALIDATE  
                            First value is which part of postcode you want to validate and Second value is the value.  
                            First value can be anyone of the following values: postcode, area, district, sector, unit  
                            Second value can be any string you want to match against the selected type  
      -f FORMAT, --format FORMAT  
                            The postcode string to format  

You can see the help info by running:
```commandline
python script.py -h
```

### Examples:  
Validate:  
```commandline
python script.py -v postcode "SW1W 0NY"
```

Validate area:  
```commandline
python script.py -v area "SW"
```

Format:  
```commandline
python script.py -f "SW1W 0NY"
```
