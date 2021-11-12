# Currency Converter

## The basics
This is a basic currency converter built with *Python3* that makes use of *Flask*, *Jinja*, and the *[forex-python](https://forex-python.readthedocs.io/en/latest/index.html)* module. 

## Input validation
For user input validation, *flash* is being used. Helper functions under `helpers.py` will validate user input for valid currencies (validated against the API valid currencies), and amount.

## Testing
Doctests were written for the helper functions. Unit tests were also written and are part of this project (please refer to `tests.py` file).

## User Flow
Users will be presented with the home page of the website and **FROM** and **TO** currency entries are expected, as well as the **amount** to be converted. The list of supported currencies can be found [here](https://forex-python.readthedocs.io/en/latest/currencysource.html#list-of-supported-currency-codes). Once user input validation is completed (and passed), the conversion takes place and a screen with the conversion results is rendered, with the option to start a new conversion.