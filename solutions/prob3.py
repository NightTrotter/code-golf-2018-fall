with open("3.txt", 'r') as f:
    li = f.readlines()

t = li[0]

def func(k,l):
    for n in range(k-1):
        a = max(l)
        while a in l: l.remove(a)
    return max(l)

for n in range(t):
    print func(li[1]*n, li[2]*n)