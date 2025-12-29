import datetime as dt
import pandas as pd

class Bank:
    bname='Power'
    branch='PLamedu'
    ifsc='PBI00420'
    addr='Spectra Building'

    def __init__(self,name,mob,adr,bal):
        self.name=name
        self.mob=mob
        self.adr=adr
        self.bal=bal
        self.st={'Date':[''],'Desc':[''],'CR':[''],'DR':[''],'Bal':[self.bal]}

    def details(self):
        print(f'===== Bank Details =====\n'
              f'Bank Name: {self.bname}\n'
              f'Branch: {self.branch}\n'
              f'Ifc: {self.ifsc}\n'
              f'Address: {self.addr}\n'
              f'{"="*25}'
              f'===== Cust Details =====\n'
              f'Bank Name: {self.name}\n'
              f'Branch: {self.branch}\n'
              f'Ifc: {self.ifsc}\n'
              f'Address: {self.addr}\n'
              f'Balance: {self.bal}\n'
              f'{"="*25}')
        
    def deposit(self,amt):
        if amt > 100:
            self.bal += amt
            print(f'{amt} RS Sucessfully Deposited\n'
                  f'Your Total Bal: {self.bal}\n')
            self.st['Date'].append(dt.datetime.today().date())
            self.st['Desc'].append('Deposited')
            self.st['CR'].append(amt)
            self.st['DR'].append('-')
            self.st['Bal'].append(self.bal)
        else:
            print('Enter Valid Amount')            
            
    def withdraw(self, amt):
        if amt > 100 and amt <= self.bal:
            self.bal -= amt
            print(f"{amt} Rs withdrawn successfully")
            print(f"Your total balance: {self.bal}")
            self.st['Date'].append(dt.datetime.today().date())
            self.st['Desc'].append('Withdrawed')
            self.st['CR'].append('-')
            self.st['DR'].append(amt)
            self.st['Bal'].append(self.bal)
        else:
            print("Invalid withdraw amount")

    def transfer(self, amt, ben):
        if amt > 100 and amt <= self.bal:
            self.bal -= amt
            ben.bal += amt
            print(f"{amt} Rs transferred successfully")
            print(f"Your balance: {self.bal}")
            self.st['Date'].append(dt.datetime.today().date())
            self.st['Desc'].append(f'Transfered from {self.name}')
            self.st['CR'].append('-')
            self.st['DR'].append(amt)
            self.st['Bal'].append(self.bal)

            ben.st['Date'].append(dt.datetime.today().date())
            ben.st['Desc'].append(f'Transfer from {self.name}')
            ben.st['CR'].append(amt)
            ben.st['DR'].append('-')
            ben.st['Bal'].append(ben.bal)
        else:
            print("Transfer failed")

    def statement(self):
        print(pd.DataFrame(self.st))
        print('-'*30)
         
Gowtham = Bank('Gowtham',6381059233,'cbi',1000)
Jeni = Bank('Jeni',8882291035,'karur',2000)
Cna = Bank('Cna',9889978899,'Erode',4000)
Madhu = Bank('Madhu',6367063670,'Chennai',5000)
Arun = Bank('Arun',7332566110,'T Veli',3500)