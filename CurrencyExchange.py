from FileManager import FileManager
from HistoryMessages import HistoryMessages
import requests

class CurrencyExchange:
    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        self.url = "https://fake-api.apps.berlintech.ai/api/currency_exchange"
        

    def write_to_history(self, hist_dict):
        self.file_manager.add_to_json(hist_dict, self.hist_file_path) 


    def get_exchange_rates(self):
        response =  requests.get(self.url)
        exchange_rates = response.json()
        return exchange_rates
    

    def exchange_currency(self, currency_from, currency_to, amount):
        exchange_rates = self.get_exchange_rates()
        exchange_amount = None
        status = "failure"  
        try:
            amount = float(amount)  # Convert amount to float
            if exchange_rates:  # Check if exchange rates have been retrieved
                if currency_from not in exchange_rates or currency_to not in exchange_rates:
                    print("Currency exchange failed!")
                else:
                    rate_from = exchange_rates[currency_from]
                    rate_to = exchange_rates[currency_to]
                    exchange_amount = (amount / rate_from) * rate_to
                    status = "success" 
            else:
                print("Currency exchange failed!")
        except ValueError:
            print("Currency exchange failed!")

        history_message = HistoryMessages.exchange(status, amount, exchange_amount, currency_from, currency_to)
        self.write_to_history(history_message)
        return exchange_amount