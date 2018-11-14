for n in range(100000):
    if str(n)[0] == str(n)[-1]: 
        if n%3 == 0 or n%5==0 or n%7==0: print(n)