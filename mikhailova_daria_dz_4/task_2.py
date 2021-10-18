from cbr_parser.utils import extract_data


def currency_rates(name):
    course = extract_data('Value')
    course = [float(el.replace(',', '.')) for el in course]
    name_currency = extract_data('CharCode')
    conversion_dict = dict(zip(name_currency, course))
    return f'{name}:{conversion_dict[name]}'


print(currency_rates('CHF'))


