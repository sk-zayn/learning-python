class Banking:
  bank_name = 'zain bank'

  def __init__(self, account_no, name, balance = 0):
    self.account = account_no
    self.name = name
    self.balance = balance
    print(f'account created sucessfully for {self.name}')

  def deposit(self, amount):
    if amount > 0:
      self.balance = self.balance + amount
      print(f'Amount {amount} deposited successfully')

    else:
      print('Invalis deposit amount')

  def withdraw(self, amount):
    if amount <= 0:
      print('Invalid withdrewal amount')
    elif amount > self.balance:
      print('Withdrawl amount should not be greater than balance')
    else:
      self.balance = self.balance = amount
      print(f'amount{amount} withdrewn successfully')

  def check_balance(self):
    print(f'Balance amount is: {self.balance}')

  def account_details(self):
    print(self.name, self.balance, self.account)


obj1 = Banking(101, 'zain')
obj1.deposit(2000)
obj1.withdraw(1000)
obj1.check_balance()
obj1.account_details()
