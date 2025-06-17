class BankAccount:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Replenishment: +{amount}")
        else:
            print(f"Invalid number")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
        else:
            print(f"Invalid number")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, user_id, pin, balance=0):
        if user_id in self.accounts:
            print("Account has ben exist")
            return False
        self.accounts[user_id] = BankAccount(user_id, pin, balance)
        return True

    def auth(self, user_id, pin):
        if user_id in self.accounts and pin == self.accounts[user_id].pin:
            return self.accounts[user_id]
        else:
            print("Invalid PIN or user_id")
            return None

    def run(self):
        print("---- Good morning in bankomat")
        account_number = int(input("Enter number of bank account"))
        pin = int(input("Enter PIN....."))

        account = self.auth(account_number, pin)

        if account:
            while True:
                print("\nEnter make:")
                print("1. Check balance")
                print("2. Top up account")
                print("3. Withdraw funds")
                print("4. Transaction history")
                print("5. Exit")

                choice = input("Your choice:")

                match choice:
                    case "1":
                        print(f"Your balance: {account.get_balance()}")
                    case "2":
                        try:
                            amount = float(input("Enter summ for top up"))
                            account.deposit(amount)
                        except ValueError:
                            print("Invalid format of summ")
                    case "3":
                        try:
                            amount = float(input("Enter summ for withdraw"))
                            account.withdraw(amount)
                        except ValueError:
                            print("Invalid format of summ")
                    case "4":
                        history = account.get_transactions()
                        if history:
                            print("History of Transactions:")
                            for item in history:
                                print(item)
                        else:
                            print("History of transactions is empty")
                    case "5":
                        print("Thank u for used bankomat")
                        break
                    case _:
                        print("Invalid of variant")
        else:
            print("Auth is break")


atm = ATM()

atm.create_account(1, 123, 100)

atm.run()
