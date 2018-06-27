Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> class Account(object):
    def __init__(self, holder, number, balance,credit_line=1500): 
        self.Holder = holder 
        self.Number = number 
        self.Balance = balance
        self.CreditLine = credit_line

    def deposit(self, amount): 
        self.Balance = amount

    def withdraw(self, amount): 
        if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False  
        else: 
            self.Balance -= amount 
            return True

    def balance(self): 
        return self.Balance

    def transfer(self, target, amount):
	if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False  
        else: 
            self.Balance -= amount 
            target.Balance += amount 
            return True
