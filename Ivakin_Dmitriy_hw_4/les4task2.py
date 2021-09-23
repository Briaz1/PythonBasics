import requests


def currency_rates(char_code):
    """
    Считаю использование Decimal в данном случае лишним, так как нам нужно просто сделать вывод без математических
    операций.
    Использование модуля datetime так же считаю лишним в данной задаче, так как дату там так же нужно просто вывести.

    :param char_code: official currency abbreviation
    :return: exchange rate in rubles for the current date
    """
    char_code = char_code.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_value = response[response.find('<Value>', response.find(char_code)) + 7:
                              response.find('</Value>', response.find(char_code))]
    date = response[response.find('Date="') + 6:response.find('Date="') + 16]
    val_name = response[response.find('<Name>', response.find(char_code)) + 6:
                        response.find('</Name>', response.find(char_code))]

    return f'Курс {char_code} ({val_name}) на текущую дату {date}:' \
           f' {float(currency_value.replace(",", ".")):.2f} рублей.'


print(currency_rates('usd'))
print(currency_rates('eur'))
print(currency_rates('mdl'))
