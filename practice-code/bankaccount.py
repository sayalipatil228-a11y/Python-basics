class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

#-------Main Program----------

with open("accounts.txt", "r") as file:
    data = file.readlines()
    name, balance = data.split(",")

acc = BankAccount(name, int(balance))

for line in data:
    name, balance = line.strip().split(",")
        
# print("Name:", acc.name)
# print("Balance:", acc.get_balance())
