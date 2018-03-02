def receive(request, money):
    cash = [100, 50, 10, 5, 4, 3, 2, 1]
    if request > money:
        print "there is no money sufficient"
        print "there is only", money
    elif request <= money:
        for i in cash:
            while request >= i:
                print "give:", i
                request -= i
    else:
        print "Request should be more than zero"

receive(258, 500)
