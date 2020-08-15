
'''This Is a Simple Game To Guess Your Number Between 1 To 63'''
import time
L = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37,\
     39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]
L_2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35,\
       38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59, 62, 63]
L_3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37,\
       38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61, 62, 63]
L_4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40,\
       41, 42, 43, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61, 62, 62]
L_5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48,\
       49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
L_6 = list(map(lambda x: x, (32, 64)))


print('Welcome to the Game'.center(100, '-'))
time.sleep(0.50)
print('In This Game We Will Find Out The Number Between 1 To 63 Which u Guess'.center(20))
print('\n')
time.sleep(1)
print('Rules of the game:')
time.sleep(0.5)
print('u need to say yes or no to the list of numbers which we show')
time.sleep(0.5)
print('Saying wrong we produce a wrong number')
time.sleep(0.5)
print('Guess a Number between 1 to 63'.center(75))

while True:
    S = 0
    time.sleep(0.25)
    print(L)
    time.sleep(0.25)
    i = input('Say weather the number is in the above list')
    if i.lower() == 'yes':
        S += L[0]
    time.sleep(0.25)
    print(L_2)
    time.sleep(0.25)
    i = input('Say weather the number is in the above list')
    if i.lower() == 'yes':
        S += L_2[0]
    time.sleep(0.25)
    print(L_3)
    time.sleep(0.25)
    i = input('Say weather the number is in the above list')
    if i.lower() == 'yes':
        S += L_3[0]
    time.sleep(0.25)
    print(L_4)
    time.sleep(0.25)
    i = input('Say weather the number is in the above list')
    if i.lower() == 'yes':
        S += L_4[0]
    time.sleep(0.25)
    print(L_5)
    time.sleep(0.25)
    i = input('Say weather the number is in the above list')
    if i.lower() == 'yes':
        S += L_5[0]
    time.sleep(0.25)
    print(L_6)
    time.sleep(0.25)
    i = input('Say weather the number is in the above list')
    if i.lower() == 'yes':
        S += L_6[0]
    print('The Number Which you guessed is', S)
    time.sleep(2)
    j = input('If you want to exit the game press exit now or press any key:'.center(100))
    if j.lower() == 'exit':
        break
