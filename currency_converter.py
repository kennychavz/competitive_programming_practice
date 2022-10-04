# pylint: disable=missing-docstring

# add some currency rates
RATES = {
    'USDEUR': 0.85,
    'GBPEUR': 1.13,
    'CHFEUR': 0.86,
    'EURGBP': 0.885,
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    # we declare the variables to make it easier to manipulate
    quantity = amount[0]
    current_curr = amount[1]
    #first we want to find the currency rate proper to currency traded and desired
    for pair, rate in RATES.items():
        if current_curr not in pair:
            continue
        if currency not in pair:
            continue
        # now we should have the desired key for our rate, we separate key in 2
        base, quote = pair[0:3], pair[3:6]
        # scenario 1: if the currency is the base one of the rate we divide it
        # by the rate
        if currency == base:
            return round(quantity / rate, 2)
        # scenario2: if the currency is the quote currency of the rate we multiply
        # if by the rate
        if currency == quote:
            return round(quantity * rate,2)
