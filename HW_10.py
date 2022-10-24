import uuid
import datetime


class BankAccount:
    deposit = 0

    def __init__(self, name, percentage, money):
        """ Initialize self"""
        self.name = name
        self.__percentage = percentage
        self.uuid = uuid.uuid4()
        self.date_account_creation = datetime.date.today()
        self.money = money
        BankAccount.deposit += money

    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, percentage):
        self.__percentage = percentage

    def __str__(self):
        return f'Your ID:{uuid.uuid4()}, name {self.name} your %{self.percentage}, your money:{self.money}'

    def refill_funds(self, summa):
        self.money += summa
        BankAccount.deposit += summa

    def withdrawal_funds(self, summa):
        if self.money >= summa:
            self.money -= summa
            BankAccount.deposit -= summa
        else:
            self.money = 0
            BankAccount.deposit = 0

    def __del__(self):
        print(f' {self.name}, your bank count was closed because of bank licvidation, refund amount is {self.money}')
        self.withdrawal_funds(self.deposit)

    @property
    def get_todays_profit(self):
        """Returns today's profit"""
        return self.money * self.percentage / 100 / 365

    def money_transfer(self, other_account, summa):
        """ Method for transfer money"""
        if other_account.money >= summa:
            self.money += summa
            other_account.money -= summa
        else:
            self.money += other_account.money
            other_account.money = 0

    @staticmethod
    def hello_msg():
        """Hello message"""
        print('We save and protect your money')


alex = BankAccount('Alex', 10, 55000)
tom = BankAccount('Tom', 5, 100000)
alex.percentage = 20
tom.withdrawal_funds(45699)
alex.refill_funds(10000)
alex.money_transfer(tom, 5000)

