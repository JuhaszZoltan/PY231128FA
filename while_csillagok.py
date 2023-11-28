s:int = 3
o:int = 4
while s > 0:
    while o > 0:
        print('*', end='')
        o -= 1
    print(end='\n')
    o = 4
    s -= 1