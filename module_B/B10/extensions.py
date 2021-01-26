import json
import requests
from config import values 


def get_key(dict_, value):
    for k, v in dict_.items():
        if v == value:
            return k


class APIException(Exception):
    pass

class Exchage():
    @staticmethod
    def get_price(base, quote, amount):
        if (base.lower() in values):
                base_ticker = values[base.lower()]
        elif base.upper() in values.values():
            base_ticker = base.upper()
            base = get_key(values, base.upper())
        else:
            raise APIException(f'Неизвестная валюта {base.upper()}.\n Чтобы получить список валют введите /values')

        if (quote.lower() in values):
            quote_ticker = values[quote.lower()]
        elif quote.upper() in values.values():
            quote_ticker = quote.upper()
            quote = get_key(values, quote.upper())
        else:
            raise APIException(f'Неизвестная валюта {quote.upper()}.\n Чтобы получить список валют введите /values')
        
        try:
            amount = float(amount.replace(',' , '.'))
        except ValueError:
            raise APIException('Неверный ввод количества. Должно быть целым или десятичным числом')

        if base == quote:
            raise APIException(f'Нет смысла конвертировать {base} в {base}')

        response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_ticker}&symbols={quote_ticker}')
        sum = round(json.loads(response.content)['rates'][quote_ticker] * amount, 2)
        text = f'Цена {amount} {base.lower()} в {quote.lower()} - {sum}'
        return text