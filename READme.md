# Bank Terminal App
The Bank Terminal App is a command-line application that simulates basic banking operations such as account management, deposit, withdrawal, and transaction history tracking.

**Features**
Account Management: Create and manage bank accounts.
Deposit: Add funds to an account.
Withdrawal: Withdraw funds from an account.
Transaction History: View transaction history for an account.

**Installation**
Clone the repository: git clone https://github.com/yourusername/bank-terminal-app.git
Navigate to the project directory: cd bank-terminal-app
Install dependencies: pip install -r requirements.txt
Usage
---(Run the application: python app.py)
Follow the on-screen prompts to perform various banking operations.

## Terminal Interface
- Implement an intuitive terminal interface with prompts for available commands.
- Users should be able to select actions by entering the corresponding command numbers.

## Basic Account Operations
- Implement the following operations:
  1. View balance
  2. Deposit funds
  3. Withdraw funds
  4. View transaction history
  5. Currency exchange

- Pay attention to specific implementation details:
  - When depositing funds, validate the correctness of the provided amount. The value should be a positive integer. Information about the deposit attempt should be added to the history file. In case of incorrectly specified value of account replenishment, the message "Invalid amount for deposit!" should be displayed.
  - During withdrawal, validate the correctness of the provided amount. Additionally, check for sufficient funds in the account. If funds are insufficient, display the message "Invalid amount for debit!" Information about the withdrawal attempt should be added to the history file.
  - When viewing the transaction history, read the history from a JSON file and display it line by line in the terminal.
  - For currency exchange, send an HTTP request to the server (server link: https://fake-api.apps.berlintech.ai/api/currency_exchange) to receive a JSON with the latest exchange rates (all values are relative to EURO). Use the data obtained for conversion. In case of an incorrectly specified value from the user, display the message "Currency exchange failed!".

## Logging Transaction History
- Logging should be implemented for deposit, withdrawal, and currency exchange operations. Logs should be added to the "history.json" file.
- The structure for each type of operation is as follows:
  1. Deposit:
     ```json
     {
       "operation_type": "deposit",
       "status": "success/failure",
       "amount_of_deposit": <value of attempted deposit>,
       "total_balance": <balance value after deposit attempt>
     }
     ```
  2. Withdrawal:
     ```json
     {
       "operation_type": "debit",
       "status": "success/failure",
       "amount_of_deposit": <value of attempted withdrawal>,
       "total_balance": <balance value after withdrawal attempt>
     }
     ```
  3. Currency Exchange:
     ```json
     {
       "operation_type": "exchange",
       "status": "success/failure",
       "pre_exchange_amount": <amount before exchange>,
       "exchange_amount": <amount after exchange>,
       "currency_from": <currency of exchange>,
       "currency_to": <currency for which the exchange was made>
     }
     ```

## Classes
- Create a class for the account with relevant properties (balance, transaction history) and methods (deposit, withdrawal, get balance).
- Create a currency exchange class with currency rates and methods for currency exchange and rate updates (using network requests).

## Project Stage (Student Activity Breakdown and breakdown)
- **Step 1: Download Project and Install Dependencies**: Project has been downloaded and all the dependencies installed successfully.
- **Step 2: Implement FileManager Class**: Student has successfully created all methods described in the assignment.
- **Step 3: Implement Methods in Account Class**: Student has successfully created all methods described in the assignment.
- **Step 4: Implement Methods in CurrencyExchange Class**: Student has successfully created all methods described in the assignment.
- **Step 5: Maintain Project in GIT**: Each step from 2 to 4 is committed to separate branches. Each contribution is committed separately. Project is submitted as a GitHub project with dependencies file, excluding the virtual environment folder.

