from random import randint
player=input("rock (r),paper (p) or scissors (s)?")
print(player,'vs',end='')
choosen=randint(1,3)
if choosen==1:
    computer='r'
elif choosen==2:
    computer='p'
else:
    computer='s'

print(computer)

if player==computer:
    print("DRAW")

elif player=='r' and computer=='s':
    print("player wins")

elif player=='r' and computer=='p':
    print("player wins")
    
elif player=='s' and computer=='r':
    print("computer wins")

elif player=='s' and computer=='p':
    print("player wins")

elif player=='p' and computer=='s':
    print("computer wins")

elif player=='p' and computer=='r':
    print("player wins")
