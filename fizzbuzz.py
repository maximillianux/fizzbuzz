for x in range(1,100):
    (q,r) = divmod(x,3)
    if r == 0:
        print ("fizz"),
    if r != 0:
        (a,b) = divmod(x,5)
        if b == 0:
            print("buzz"),
        else:
            print (x)