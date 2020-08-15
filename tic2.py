print("Welcome to tictactoe game")
print("To play this game we need two players")
print("we are showing the positions")


def stru(h):             #this going to print the structure
  c=0
  d=0
  print('---------------------')
  for j in l:
    c+=1
    print('| ',j,' |',end='')
    if c==3:
      c=0
      d+=1
      print('\n')
      print('---------------------')


      
l=[ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ]  # for displaying the positions
stru(l)

########################################################


def check(cl):        ## this is used to check the winner
  if (cl[0]==cl[1] and cl[1]==cl[2] and cl[1]!=' ') or  (cl[3]==cl[4] and cl[4]==cl[5] and cl[5]!=' ') or (cl[6]==cl[7] and cl[7]==cl[8] and cl[8]!=' ') or (cl[0]==cl[3] and cl[3]==cl[6] and cl[6]!=' ') or (cl[1]==cl[4] and cl[4]==cl[7] and cl[7]!=' ') or (cl[2]==cl[5] and cl[5]==cl[8] and cl[8]!=' ') or (cl[0]==cl[4] and cl[4]==cl[8] and cl[8]!=' ') or (cl[2]==cl[4] and cl[4]==cl[6] and cl[6]!=' '):
    return True
  else:
    return False

#####################################################################


def cake(ck,hq):      ## This function is used to check any over writing is taking place
  if ck[hq]==' ':
    return False
  else:
    print("/////////you can't overwrite//////////////////////")
    return True










#####################################################################
# for selectring which player to play first
import random
l1=input("enter your name")
print('\n\n')
l2=input("enter your opponent name")
print('\n\n')
xpq=random.randint(1,2)         # For selecting random player as first
if xpq==1:
    print('\n\n')
    print(l1,"you are the first player\n")
    print(l2,"you are the secound player")
else:
    print('\n\n')
    t=l1
    l1=l2
    l2=t
    print(l1,"you are the first player\n")
    print(l2,"you are the secound player")

#####################################################################

## This block of code is for printing which player got X and O
 
l=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

g=True
while(g):
  print(l1,"choose X or O the other player will get what u haven't choosen")
  p1=input()
  if p1.upper()=='X':
    p2='O'
  else:
    p2='X'
  if p1.upper()=='X' or p1.upper()=='O':
    print(l1,"has taken",p1)
    print(l2,"you get",p2)
    g=False
  else:
    print("choose any one of the given two options only")

####################################################################

##############################################################

    
lol=0  # It is used to calculate number of operations to provid tie came 
won=0
for psk in range(1,10):
  lol+=1
  what=True
  why=True
  while(what):
      if psk%2==1:       # This if case decides which player has to play
        po=int(input('player one enter ur position'))
        what=cake(l,po)
        if what!= True:
          l[po]=p1
          stru(l)        # To print the present structure
        if check(l):
          print(l1,', you won the game')
          won=1
          break        # to come out of while loop
      else:
        po=int(input('player two enter ur position'))
        what=cake(l,po)
        if what!= True:
          l[po]=p2
          stru(l)
        if check(l):
          print(l2,' you won the game')
          won=1
          break            # to come out of while loop
  if won==1:                 # to come out of the for loop
      break
  if lol==9:
    print("There is tie between",l1,'and',l2)
    break
