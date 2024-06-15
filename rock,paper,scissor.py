import random

while(True):
    player = input ('lets rock paper scissor ')

    data = ['rock' , 'paper' ,'scissors ']
    choisse = random.choice(data)
    print(choisse)

    #rock = scciorr
    #paper = rock
    #sccior = paper


    if (player =='rock' and choisse == 'scissors') or (player == 'paper'and choisse == 'rock') or (player == 'scissors' and choisse == 'paper'):
        print('you won the game')
    elif player == choisse:
        print("tie")
    else:
        print('your lost ')