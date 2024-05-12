class Account:

    def __init__(self,acc_num,opening_balance):
        self.acc_num=acc_num
        self.opening_balance=opening_balance

    # str method to display balance
    def __str__(self):
        return self.opening_balance

    # deposit method for accepting deposits

    def deposit(self,deposit_amt):
        self.opening_balance+=deposit_amt

    # withdrwal method for accepting withdrawal

    def withdrawal(self,withdraw_amt):
        if withdraw_amt>self.opening_balance:
            print('Funds not available,please try to withdraw lower amount')
        else:
            self.opening_balance-=withdraw_amt

# creating checking account as a child cass of Account and displaying checking account info

class CheckingAccount(Account):

    #def __init__(self,acc_num,opening_balance):
        # base class __init__
    super().__init__(Account.acc_num,Account.opening_balance)

    # Define a __str__ method that returns a string specific to Checking accounts

    def __str__(self):
        return 'Checking Account {} and balance is {} ',format(self.acc_num,Account.__str__(self))

c=CheckingAccount(12345,1520)
print(c)