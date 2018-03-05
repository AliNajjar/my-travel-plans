def withdraw(balance, request):
    
    print "current balance =", balance
    cash = [100, 50, 10, 5, 4, 3, 2, 1]
    if request > balance:
        print "there is no money sufficient"
    elif request <= balance:
        balance -= request
        for i in cash:
            while request >= i:
                print "give:", i
                request -= i
        print "---------------"

    else:
        print "Request should be more than zero"

    return balance

balance = 500

balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)