from FileManager import FileManager
from HistoryMessages import HistoryMessages

class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        self.file_manager.add_to_json(hist_dict,self.hist_file_path)


    def deposit(self, amount):
        try:
            amount = int(amount)  # Convert amount to integer
            
            if amount <= 0:
                status = "failure"
                print("Invalid amount for deposit!")
            else:
                self.balance += amount
                status = "success"

        except ValueError:
            print("Invalid input for deposit!")
            status = "failure"
        
        history_message = HistoryMessages.deposit(status, amount, self.balance)
        self.write_to_history(history_message)
        # deposit is a @static method in HistoryMessages.
        # so it can be called by HistoryMessages.deposit() without creating instance of History messages class


    def debit(self, amount):
        try:
            amount = int(amount)

            if self.balance < amount:
                status = "failure"
                print("Invalid amount for debit!")
            else:
                self.balance -= amount
                status = "success"

        except ValueError:
            print("Invalid input for debit!")
            status = "failure"
        

        history_message = HistoryMessages.debit(status, amount, self.balance)
        self.write_to_history(history_message)


    def get_balance(self):
        return self.balance


    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        

    def get_history(self):
        history = self.file_manager.read_json(self.hist_file_path)
        return history