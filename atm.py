class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_ls = []

    def withdraw(self, request):
        print "welcome to", self.bank_name
        print "current balance =", self.balance
        print "========================="

        cash = [100, 50, 10, 5, 4, 3, 2, 1]
        if request > self.balance:
            print "there is no money sufficient"
            print "========================="
        elif request <= self.balance:
            self.withdrawals_ls.append(request)
            self.balance -= request
            for i in cash:
                while request >= i:
                    print "give:", i
                    request -= i
            print "========================="

        else:
            print "Request should be more than zero"
            print "========================="

        return self.balance
    
    def show_withdrawals(self):
        for withdrawal in self.withdrawals_ls:
            print "withdrawals:", withdrawal
        print "========================="


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(80)
atm1.show_withdrawals()

atm2.withdraw(100)
atm2.withdraw(200)
atm2.show_withdrawals()
