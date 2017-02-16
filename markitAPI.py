import requests

class Markit():

    def get_symbol():
        print(' ')
        company_name = input("What company do you want a symbol for? ")
        markit_api = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json/?input='
        symbol_urie = markit_api + company_name
        symbol_response = requests.get(symbol_urie)
        for _ in symbol_response.json():
            #print(' ')
            #print(_)
            #print(type(_))
           print("Name: " + _['Name'])
           print("Exchange: " + _['Exchange'])
           print("Symbol: " + _['Symbol'])

    def get_quote():
        print('')
        ticker_symbol = input("What symbol do you want a quote for? ")
        markit_api = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json/?symbol='
        quote_urie = markit_api + ticker_symbol
        quote_response = requests.get(quote_urie)

        for _ in quote_response.json():
            print(' ')
            print(_, quote_response.json()[_])
