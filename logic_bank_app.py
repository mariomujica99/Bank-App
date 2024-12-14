import csv
from PyQt6.QtWidgets import *
from gui_bank_app import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_sign_in.clicked.connect(lambda: self.sign_in())
        self.button_enter.clicked.connect(lambda: self.amount_validation())
        self.button_exit.clicked.connect(lambda: self.logout())
        self.label_sign_in_status.setText('')
        self.label_sign_in_text.setText('Welcome! Please enter your information')
        self.label_select.setText('')
        self.label_sign_in_status.setText('')
        self.radio_withdraw.toggled.connect(self.sign_in)
        self.radio_deposit.toggled.connect(self.sign_in)
        self.radio_balance.toggled.connect(self.sign_in)
        self.radio_withdraw.setVisible(False)
        self.radio_deposit.setVisible(False)
        self.radio_balance.setVisible(False)
        self.label_amount.setText('')
        self.input_amount.setVisible(False)
        self.label_transaction_text.setText('')
        self.label_balance_text.setText('')
        self.button_enter.setVisible(False)
        self.button_exit.setVisible(False)

    def sign_in(self):
        bank_users = open('bank_users.csv', 'r')
        bank_users = csv.DictReader(bank_users)
        usernames = []
        pins = []
        balances = []
        for col in bank_users:
            usernames.append(col['Username'])
            pins.append(int(col['PIN']))
            balances.append(float(col['Balance']))

        username = self.input_username.text().strip()
        pin = self.input_PIN.text().strip()
        if username in usernames:
            index = usernames.index(username)
            try:
                pin = int(self.input_PIN.text().strip())
                if pin == pins[index]:
                    self.label_sign_in_status.setText('Sign In Successful')
                    self.label_sign_in_text.setText('')

                    self.label_select.setText('Please Select Your Transaction')

                    self.radio_withdraw.setVisible(True)
                    self.radio_deposit.setVisible(True)
                    self.radio_balance.setVisible(True)

                    if self.radio_withdraw.isChecked():
                        self.label_amount.setText('Amount')
                        self.input_amount.setVisible(True)
                        self.button_enter.setVisible(True)
                        self.button_exit.setVisible(True)
                        amount = float(self.input_amount.text().strip())
                        new_balance = balances[index] - amount
                        self.label_transaction_text.setText(f'You have withdrawn ${amount:.2f}')
                        self.label_balance_text.setText(f'Your balance is: {new_balance}')

                    elif self.radio_deposit.isChecked():
                        self.label_amount.setText('Amount')
                        self.input_amount.setVisible(True)
                        self.button_enter.setVisible(True)
                        self.button_exit.setVisible(True)
                        amount = float(self.input_amount.text().strip())
                        new_balance = balances[index] + amount
                        self.label_transaction_text.setText(f'You have deposited ${amount:.2f}')
                        self.label_balance_text.setText(f'Your balance is: {new_balance}')

                    elif self.radio_balance.isChecked():
                        self.label_balance_text.setText(f'Your balance is: {balances[index]}')
                        self.button_exit.setVisible(True)

                else:
                    self.label_sign_in_status.setText('Sign In Failed')
                    self.label_sign_in_text.setText('Your username or password is incorrect.\nPlease try again.')
            except ValueError:
                self.label_sign_in_status.setText('Sign In Failed')
                self.label_sign_in_text.setText('Your username or password is incorrect.\nPlease try again.')
            except OverflowError:
                self.label_sign_in_status.setText('Sign In Failed')
                self.label_sign_in_text.setText('Your username or password is incorrect.\nPlease try again.')
        else:
            self.label_sign_in_status.setText('Sign In Failed')
            self.label_sign_in_text.setText('Your username or password is incorrect.\nPlease try again.')

    def amount_validation(self):
        amount = self.input_amount.text().strip()
        try:
            amount = float(self.input_PIN.text().strip())
            if amount < 0:
                self.label_transaction_text.setText('Invalid amount.\nPlease try again.')
            else:
                return amount
        except ValueError:
            self.label_transaction_text.setText('Invalid amount.\nPlease try again.')
        except OverflowError:
            self.label_transaction_text.setText('Invalid amount.\nPlease try again.')

    def logout(self):
        if self.group_transactions.checkedButton() is None:
            pass
        elif self.group_transactions.checkedButton() != 0:
            self.group_transactions.setExclusive(False)
            self.group_transactions.checkedButton().setChecked(False)
            self.group_transactions.setExclusive(True)

        self.input_username.clear()
        self.input_PIN.clear()
        self.input_username.setFocus()
        self.label_sign_in_status.setText('')
        self.label_sign_in_text.setText('Welcome! Please enter your information')
        self.label_select.setText('')
        self.label_sign_in_status.setText('')
        self.radio_withdraw.setVisible(False)
        self.radio_deposit.setVisible(False)
        self.radio_balance.setVisible(False)
        self.label_amount.setText('')
        self.input_amount.setVisible(False)
        self.label_transaction_text.setText('')
        self.label_balance_text.setText('')
        self.button_enter.setVisible(False)
        self.button_exit.setVisible(False)