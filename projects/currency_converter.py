# Real time currency convertor using real time API

import requests

url = 'https://api.currencylayer.com/live?access_key=c4b8564c1549483f3f08c48a77eb5fe7'

def currency_converter():
    from_currency = input("From Country: ").upper()
    to_currency = input("To Country: ").upper()
    amount = float(input("Enter amount: "))
    try:
        # send a get request
        response = requests.get(url)
        # parse the response
        data = response.json()
        

        # check if the get request was successful
        if data.get("success"):
            # get the exchange rates for the currencies
            base_rate_from = data['quotes'].get(f"USD{from_currency}")
            base_rate_to = data['quotes'].get(f"USD{to_currency}")


            if base_rate_from and base_rate_to:
                conversion_rate = base_rate_from / base_rate_to
                converted_amount = amount * conversion_rate
                print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
            else:
                print(f"Exchange rate for {from_currency} and {to_currency} not found")
        else:
            print(f"Failed to fetch data from API.", data.get('error', {}))
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    currency_converter()