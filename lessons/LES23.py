# div - обязательный имееной параметр
import logging


def div_nums(*args, **kwargs):
    upper = 0
    if "div" not in kwargs:
        raise Exception('No div in kwargs')
    div = kwargs['div']
    kwargs.pop('div')
    if div != 0:
        for x in args + tuple(kwargs.values()):
            if type(x) == int or type(x) == float:
                upper += x
            else:
                try:
                    upper += float(x)
                    continue
                except (ValueError, TypeError):
                    pass
    else:
        raise Exception('Can not divide to 0')
    return upper / div


# logging.debug()
