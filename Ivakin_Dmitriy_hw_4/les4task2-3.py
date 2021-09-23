import requests
from datetime import datetime


def currency_rates(char_code):
    """
    Считаю использование Decimal в данном случае лишним, так как нам нужно просто сделать вывод без математических
    операций.

    :param char_code: official currency abbreviation
    :return: exchange rate in rubles for the current date
    """
    char_code = char_code.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if char_code not in response:
        return None

    currency_value = response[response.find('<Value>', response.find(char_code)) + 7:
                              response.find('</Value>', response.find(char_code))]
    val_name = response[response.find('<Name>', response.find(char_code)) + 6:
                        response.find('</Name>', response.find(char_code))]
    current_date = datetime.strptime(response[response.find('Date="') + 6:
                                              response.find('Date="') + 16], '%d.%m.%Y').date()

    return f'Курс {char_code} ({val_name}) на текущую дату {current_date}:' \
           f' {float(currency_value.replace(",", ".")):.2f} рублей.'


print(currency_rates('usd'))
print(currency_rates('eur'))
print(currency_rates('jag'))
