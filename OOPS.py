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

    def details(self):
        print(f'=========Bank Details========= \n'
        f'Bank Name:{self.bname}\n'
        f'Branch:{self.branch}\n'
        f'IFSC:{self.ifsc}\n'
        f'Address:{self.addr}\n'
        f'=========Customer Details========= \n'
        f'Name:{self.name}\n'
        f'Mobile:{self.mob}\n'
        f'Address:{self.adr}\n'
        f'Balance:{self.bal}\n'
        f'{"="*25}')

    def deposit(self, amt):
        if amt>100:
            self.bal += amt
            print(f'{amt} RS successfully Deposited\n'
            f'Your Total Bal:"{self.bal}"')
        else:
            print('Enter Valid amount')

    def withdraw(self, amt):
        if amt>100:
            self.bal -= amt
            print(f'{amt} RS successfully Withdraw\n'
            f'Your Total Bal:"{self.bal}"')
        else:
            print('Enter Valid amount')
            
    def transfer(self, amt, Per):
        if amt>100:
            self.bal -= amt
            Per.bal += amt
            print(f'{amt} RS successfully Transfer to {Per.name}\n'
            f'Your Total Bal:"{self.bal}"')
        else:
            print('Enter Valid amount')

Gowtham = Bank('Gowtham', 9874563210,'cbe',2000)
Jeni = Bank('Jeni',978965413,'krr',4000)
Cna = Bank('Cna',9874563210,'cbe',2000)
madhu = Bank('madhu',9874563210,'cbe',2000)
