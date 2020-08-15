'''This is simple python module used to check the opposite seat number of the given seat number'''
D = {1:[12, 'WS'], 2:[11, 'MS'], 3:[10, 'AS'], 4:[9, 'AS'], 5:[8, 'MS'], 6:[7, 'WS']\
     , 7:[6, 'WS'], 8:[5, 'MS'], 9:[4, 'AS'], 10:[3, 'AS'], 11:[2, 'MS'], 0:[1, 'WS']}
N = int(input('Test cases should be between 1 and 105  :'))
if N in range(1, 106):
    L = []
    for i in range(N):
        e = int(input('Input should be in range of 1 to 108  :'))
        L.append(e)
    print('\n\n')
    for i in L:
        if i in range(1, 109):
            rem = i % 12
        #print(rem)
            quo = i // 12
            if rem == 0:
                quo -= 1
        #print(quo)
            v = D.get(rem)
            print(v[0]+12*quo, ' ', v[1])
        else:
            print('Input is out of range')
else:
    print('Test cases out of Range')
