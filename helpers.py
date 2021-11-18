from forex_python.converter import CurrencyRates, CurrencyCodes

def is_valid_currency(currency): 
    """
    Verify if currency entered in DOM is valid/supported by forex-converter

    >>> is_valid_currency('USD')
    True
    
    >>> is_valid_currency('EUR')
    True
    
    >>> is_valid_currency('ABC')
    False
    """
    c = CurrencyCodes()
    return c.get_currency_name(currency) is not None

def is_valid_amount(amount):
    """
    Verify if amount entered is valid (number and greater than or equal to zero)
    >>> is_valid_amount('123.599')
    True
    
    >>> is_valid_amount('-109')
    False
    
    >>> is_valid_amount('abcde')
    False

    """

    try:
        float(amount)
    except ValueError: 
        return False
    else: 
        if float(amount) >= 0:
            return True
        else: 
            return False

def get_currencies():
    """
    Get list of supported currencies
    >>> get_currencies()
    ['AUD - Australian dollar', 'BGN - Bulgarian lev', 'BRL - Brazilian real', 'CAD - Canadian dollar', 'CHF - Swiss franc', 'CNY - Chinese/Yuan renminbi', 'CZK - Czech koruna', 'DKK - Danish krone', 'EUR - European Euro', 'GBP - British pound', 'HKD - Hong Kong dollar', 'HRK - Croatian kuna', 'HUF - Hungarian forint', 'IDR - Indonesian rupiah', 'INR - Indian rupee', 'ISK - Icelandic króna', 'JPY - Japanese yen', 'KRW - South Korean won', 'MXN - Mexican peso', 'MYR - Malaysian ringgit', 'NOK - Norwegian krone', 'NZD - New Zealand dollar', 'PHP - Philippine peso', 'PLN - Polish zloty', 'RON - Romanian leu', 'RUB - Russian ruble', 'SEK - Swedish krona', 'SGD - Singapore dollar', 'THB - Thai baht', 'TRY - Turkish new lira', 'USD - United States dollar', 'ZAR - South African rand']
    """

    c = CurrencyRates()
    c_codes = CurrencyCodes()
    currs_obj = c.get_rates('USD').keys()
    curr_codes = [curr for curr in currs_obj]
    curr_codes.append('USD')
    currencies = []
    for curr in curr_codes:
        name = c_codes.get_currency_name(curr)
        currencies.append(f"{curr} - {name}")
    currencies.sort()
    return currencies
