import time
import random


ch=['rock','paper','sessior']
print('<<<<<<<<-----------Welcom to ROCK-PAPER-SESSIOR GAME------------------>>>>>>>>>')
time.sleep(1)
UserName=input('Enter your name')
time.sleep(1)
print('{} Your choices are \n 1.ROCK \n2.PAPER \n 3.SESSIOR \n 4.EXIT'.format(UserName))
userPoint=0
tie=0
computerPoints=0



####################################################################################################

'''def scoreCard(a,b,c,d):
    e=14
    f=d.ljust(e)
    print('----------------------------------')
    print('|             ScoreCard          |')
    print('----------------------------------')
    print('|{}|TIE     |COMPUTER|'.format(f))
    print('|{}             |{}       |{}       |'.format(a,b,c))
    print('----------------------------------')'''

def scoreCard(a,b,c,d):
    time.sleep(1)
    e=int(len(d))
    g=e+15
    k=g-11
    h=k%2
    f=d.ljust(e)
    print('-'*g)
    print('|'+' '*(k//2)+'ScoreCard'+' '*(k//2+h)+'|')
    print('-'*g)
    print('|{}'.format(d)+'|TIE|COMPUTER|')
    print('|{}'.format(a)+' '*(e-1)+'|{}'.format(b)+' '*2+'|{}'.format(c)+' '*7+'|')
    print('-'*g)
    
#######################################################################################################


def check(userPoint,tie,computerPoints):
    time.sleep(1)
    if userPoint>computerPoints:
        print('<<<<<<<---------{} you won the game---------->>>>>>>'.format(UserName))
    elif userPoint<computerPoints:
        print('<<<<<<<---------Better luck next time---------->>>>>>>>')
    else:
        print("<<<<<<<<--------you missed it narrowly,it's a tie----------->>>>>>>")
           

###########################################################################################################


while True:
    ComCh=random.choice(ch)
    usip1=input('{} Enter your choice:'.format(UserName))
    time.sleep(1)
    #print('Computer generated input is:',ComCh)
    usip=usip1.lower()
    if ComCh=='rock':
        if usip=='rock' or usip=='1':
            tie+=1
            print('Computer generated input is:',ComCh)
            print("\nIT'S A TIE".center(50,'-'))
            scoreCard(userPoint,tie,computerPoints,UserName)
        elif usip=='paper' or usip=='2':
            userPoint+=1
            print('Computer generated input is:',ComCh)
            print("\nYOU WON".center(50,'-'))
            scoreCard(userPoint,tie,computerPoints,UserName)
        elif usip=='sessior' or usip=='3':
            computerPoints+=1
            print("\nYOU LOST".center(50,'-'))
            print('Computer generated input is:',ComCh)
            scoreCard(userPoint,tie,computerPoints,UserName)
        elif usip=='exit' or usip=='4':
            scoreCard(userPoint,tie,computerPoints,UserName)
            check(userPoint,tie,computerPoints)
            break
        else:
            print('Invalide choice')
    elif ComCh=='paper':
        if usip=='rock' or usip=='1':
            computerPoints+=1
            print("\nYOU LOST".center(50,'-'))
            print('Computer generated input is:',ComCh)
            scoreCard(userPoint,tie,computerPoints,UserName)
        elif usip=='paper' or usip=='2':
            tie+=1
            print('Computer generated input is:',ComCh)
            print("\nIT'S A TIE".center(50,'-'))
            scoreCard(userPoint,tie,computerPoints,UserName)
        elif usip=='sessior' or usip=='3':
            userPoint+=1
            print('Computer generated input is:',ComCh)
            print("\nYOU WON".center(50,'-'))
            scoreCard(userPoint,tie,computerPoints,UserName)
        elif usip=='exit' or usip=='4':
            scoreCard(userPoint,tie,computerPoints,UserName)
            check(userPoint,tie,computerPoints)
            break
        else:
            print('Invalide choice')
    elif ComCh=='sessior':
        if usip=='rock' or usip=='1':
            userPoint+=1
            print('Computer generated input is:',ComCh)
            print("\nYOU WON".center(50,'-'))
            scoreCard(userPoint,tie,computerPoints,UserName)
        elif usip=='paper' or usip=='2':
            computerPoints+=1
            print("\nYOU LOST".center(50,'-'))
            print('Computer generated input is:',ComCh)
            scoreCard(userPoint,tie,computerPoints,UserName)
        elif usip=='sessior' or usip=='3':
            tie+=1
            print("\nIT'S A TIE".center(50,'-'))
            print('Computer generated input is:',ComCh)
            scoreCard(userPoint,tie,computerPoints,UserName)
        elif usip=='exit' or usip=='4':
            scoreCard(userPoint,tie,computerPoints,UserName)
            check(userPoint,tie,computerPoints)
            break
        else:
            print('Invalide choice')
