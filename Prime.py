'''
This is a simple module for checking weather the given number is prime or not
'''
def check_number(n_a):
    ''' This method takes a number as input and prints waether it is prime or not'''
    count = 0
    for i in range(1, n_a//2+1):
        if n_a%i == 0:
            count += 1
    if count > 1:
        print('NotPrime')
    else:
        print('Prime')
