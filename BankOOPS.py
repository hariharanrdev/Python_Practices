import datetime as dt
import pandas as pd

class Bank:
    bname = 'power'
    branch = 'Peelamaedu'
    ifsc = 'PBI00120'
    addr = 'nava india'

    def __init__(self, name, mob, adr, bal):
        self.name = name
        self.mob = mob
        self.adr = adr
        self.bal = bal
        self.st = {'Date': [], 'Desc': [], 'Cr': [], 'Dr': [], 'Bal': []}

    def _update_st(self, desc, cr='-', dr='-', bal=0):
        """Helper method to keep dictionary lengths consistent"""
        self.st['Date'].append(dt.datetime.today().strftime('%Y-%m-%d'))
        self.st['Desc'].append(desc)
        self.st['Cr'].append(cr)
        self.st['Dr'].append(dr)
        self.st['Bal'].append(bal)

    def deposit(self, amt):
        if amt > 100:
            self.bal += amt
            print(f'{amt} RS successfully Deposited. Total: {self.bal}')
            self._update_st(f'Deposit', cr=amt, bal=self.bal)
        else:
            print('Minimum deposit is 100')

    def withdraw(self, amt):
        if 100 < amt <= self.bal:
            self.bal -= amt
            print(f'{amt} RS successfully Withdrawn. Total: {self.bal}')
            self._update_st(f'Withdrawal', dr=amt, bal=self.bal)
        else:
            print('Invalid amount or insufficient balance')
            
    def transfer(self, amt, Per):
        if 100 < amt <= self.bal:
            self.bal -= amt
            Per.bal += amt
            print(f'{amt} RS successfully Transferred to {Per.name}')
            self._update_st(f'Transfer to {Per.name}', dr=amt, bal=self.bal)
            Per._update_st(f'Transfer from {self.name}', cr=amt, bal=Per.bal)
        else:
            print('Invalid amount or insufficient balance')
    
    def statement(self):
        print(f"\n--- Statement for {self.name} ---")
        df = pd.DataFrame(self.st)
        print(df if not df.empty else "No transactions yet.")

Gowtham = Bank('Gowtham', 9874563210, 'cbe', 2000)
Bala = Bank('Bala', 987654213, 'madurai', 5000)
