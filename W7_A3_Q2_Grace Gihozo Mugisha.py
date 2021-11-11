class BankAccount:  # Create a class BankAccount.Then define a function using __init__

    no_of_cust = 0
    acc_num = 12350

    def __init__(self, name, acc_type, initial_depo, pin):
        self.name = name
        self.cust_acc_num = BankAccount.acc_num
        self.acc_type = acc_type
        self.acc_balance = initial_depo
        self.pin = pin

        BankAccount.acc_num = BankAccount.acc_num + 1
        BankAccount.no_of_cust = BankAccount.no_of_cust + 1

    # Function to display the amount
    def basic_details(self):
        print(f"user:{self.name}\n Account NO : {self.cust_acc_num}\n Balance:{self.acc_balance}")

    # Function to deposit amount
    def deposit(self, amount1):
        amount = int(input("Enter the deposit amount:"))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            print(f"Transaction completed . current balance:{self.acc_balance}")
        else:
            print("Invalid amount transaction aborted")

    # Function to withdraw the amount
    def withdraw(self):
        amount = int(input("Enter the withdraw amount:"))
        if self.acc_balance >= amount > 0:
            self.acc_balance = self.acc_balance - amount
            print(f"Transaction completed . current balance:{self.acc_balance}")
        else:
            print("Invalid amount transaction aborted")

    # Function to transfer money to other user
    def transfer(self, other):
        amount = int(input("Enter the transfer amount:"))
        if self.acc_balance >= amount > 0:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance = other.acc_balance + amount
            print(f"Transaction completed . current balance:{self.acc_balance}")
        else:
            print("Invalid amount transaction aborted")


# Here I declare that the SavingAccount class inherits from the BankAccount

class SavingAccount(BankAccount):

    # I get access to BankAccount class using init super function

    def __init__(self, name, acc_type, initial_depo, pin, interest_rate):
        super().__init__(name, acc_type, initial_depo, pin)
        self.interest_rate = interest_rate

    # Function to saving interest the amount
    def SavingInterest(self, ):
        amount = self.acc_balance * self.interest_rate
        print("Your Saving account have been add interest on your balance after one month :", amount)


# Here I declare that the CurrentAccount class inherits from the BankAccount

class CurrentAccount(BankAccount):

    # I get access to BankAccount class using init super function

    def __init__(self, name, acc_type, initial_depo, pin, interest_rate):
        super().__init__(name, acc_type, initial_depo, pin)
        self.interest_rate = interest_rate

    # Function to current interest the amount
    def CurrentInterest(self, ):
        amount = self.acc_balance * self.interest_rate
        print("Your Current account have been add interest on your balance after one month :", amount)



# creating an object of class
# Calling functions with that class object


if __name__ == "__main__":
    cust1 = CurrentAccount(name="Grace", acc_type="CURRENT ACCOUNT", initial_depo=10000, pin=3333, interest_rate=0.01)
    cust2 = SavingAccount(name="Ines", acc_type="SAVING ACCOUNT", initial_depo=5000, pin=1234, interest_rate=0.03)
    print("NO.of customers is", BankAccount.no_of_cust)
    # print(cust1.basic_details())
    # print(cust2.basic_details())
    # cust1.deposit()
    # print(cust1.basic_details())
    # cust1.withdraw()
    # print(cust1.basic_details())
    # cust1.transfer(cust2)
    # print(cust2.basic_details())
    print(cust1.basic_details())
    cust1.CurrentInterest()
    print(cust2.basic_details())
    cust2.SavingInterest()

