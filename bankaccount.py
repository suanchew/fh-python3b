class BankAccount: 
    """Bank Account protected by a pin number."""

    def __init__(self, pin): 
        """Initial account balance is 0 and pin is 'pin'."""
        self.balance = 0
        self.pin = pin

    def show(self):
        print ("{} {}".format(self.pin, self.balance))

    def valid_pin (self, pin):
        if not self.pin == pin:
            return False
        return True

    def get_pin(self, pin):
        if not self.valid_pin(pin):
            return False
        return pin

    def set_pin(self, pin):
        if not self.valid_pin(pin):
            return False
        self.pin = pin
        return True

    def get_balance(self, pin):
        if not self.valid_pin(pin):
            return False
        return self.balance

    def set_balance(self, pin, new_balance):
        if not self.valid_pin(pin):
            return False
        self.balance = new_balance
        return True

    def whole_amounts(self, amount):
        if not float(amount).is_integer():
            return False
        return True

    def deposit(self, pin, amount): 
        """Increment account balance by amount and return new balance."""
        if not self.whole_amounts(amount):
            return False
        self.set_balance(pin, self.get_balance(pin)+amount)
        return self.get_balance(pin)

    def withdraw(self, pin, amount): 
        """Decrement account balance by amount and return amount withdrawn."""
        if not self.whole_amounts(amount) or amount > self.get_balance(pin):
            return False
        self.set_balance(pin, self.get_balance(pin)-amount)
        return amount

    def change_pin(self, oldpin, newpin): 
        """Change pin from oldpin to newpin."""
        if not self.valid_pin(pin):
            return False
        self.set_pin(pin, newpin)


class SavingsAccount(BankAccount):

    def __init__(self, pin, interestrate): 
        BankAccount.__init__(self, pin, "SavingsAccount")
        self.interest_rate = interestrate

    def add_interest_to_balance(self, pin):
        self.set_balance(pin, self.interest_rate * self.get_balance(pin))

class FeeSavingsAccount(SavingsAccount):

    def __init__(self, pin, fee): 
        BankAccount.__init__(self, pin, "FeeSavingsAccount")
        self.fee = fee

    def withdraw(self, pin, amount):
        SavingsAccount.withdraw(self, pin, amount)
        SavingsAccount.set_balance(self, pin, SavingsAccount.get_balance(self, pin)-self.fee)

if __name__ == '__main__':

    pin = "123"
    
    a = BankAccount(pin)
    a.show()

    try:
        # if not a.withdraw(pin, 1000000):
        #     raise Exception("{} cannot be withdrawn".format(1000000))
        if not a.deposit(pin, 100.00):
            raise Exception("{} not whole amount".format(100.00))
        if not a.withdraw(pin, 0.99):
            raise Exception("{} cannot be withdrawn".format(0.99))
    except Exception as e:
        print(e)
    
    a.show()
        