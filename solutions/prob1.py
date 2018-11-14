a, b = " / __ ", '\ \__/'
c, d = '/ /  \\', ' \____'
list1 = [1, 5, 9, 13, 17, 21]
list2 = [2, 6, 10, 14, 18, 22]
list3 = [3, 7, 11, 15, 19]
for n in range(23):
    if n in list1: line = (a+b)*7
    elif n in list2: line = (c+d)*7
    elif n in list3: line = (b+a)*7
    else: line = (d+c)*7
    new = line[0:82]
    print(new)