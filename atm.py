class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_ls = []

    @staticmethod
    def process_request(request):
        cash = [100, 50, 10, 5, 4, 3, 2, 1]
        for i in cash:
            while request >= i:
                print "Give:", i
                request -= i
        print "========================="

    def withdraw(self, request):
        print "Welcome to", self.bank_name
        print "Current balance =", self.balance
        print "Money required:", request
        print "========================="

        if request > self.balance:
            print "There is no money sufficient"
            print "========================="

        elif request <= 0:
            print "Request should be more than zero"
            print "========================="

        else:
            self.withdrawals_ls.append(request)
            self.balance -= request
            self.process_request(request)

        return self.balance

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_ls:
            print "Withdrawals:", withdrawal
        print "========================="


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(80)
atm1.withdraw(0)
atm1.show_withdrawals()

atm2.withdraw(100)
atm2.withdraw(200)
atm2.withdraw(-75)
atm2.show_withdrawals()
