class Bank:

    def __init__(self,owner,current_amount = 0):
        self.owner = owner
        self.current_amount = current_amount
            
 
    def deposit(self,deposit_amount):
        
        deposit_amount = float(deposit_amount)
        if deposit_amount <=0:
            raise ValueError("Enter positive integer")
        else:
            self.current_amount+=deposit_amount
            return f"Your {deposit_amount} deposited  "
              
    def withdraw(self,withdraw_amount):
        self.withdraw_amount = withdraw_amount

        if self.current_amount == 0:
            raise ValueError("your current balance is 0 ")
        elif self.current_amount<self.withdraw_amount:
            raise ValueError("Insufficient balance")    
        else:
            self.current_amount-=self.withdraw_amount
            return f"you withdraw {self.withdraw_amount} Successfully"

    def check_balance(self):
        return f"{self.owner} Account Balance is {self.current_amount} "
    
class SavingAccount(Bank):
    def __init__(self,owner,current_amount=0,interest_rate=0.03):
        super().__init__(owner,current_amount)
        self.interest_rate=interest_rate

    def add_interest(self):
        interest = self.current_amount*self.interest_rate
        self.current_amount+=interest
        return f"interest added: {interest:.2f} new balance {self.current_amount:.2f}"

class CheckingAccount(Bank):
    pass    