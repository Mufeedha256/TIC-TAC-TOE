def players():
    player1='n'
    while player1 not in ['X','x','O','o']:
        player1=input("Do you want to be X or O?")
    if player1 in['x','X']:
        player2='O'
    else:
        player2='X'
    return player1,player2
def board(lis):
    print(lis[0]+'|'+lis[1]+'|'+lis[2])
    print(lis[3]+'|'+lis[4]+'|'+lis[5])
    print(lis[6]+'|'+lis[7]+'|'+lis[8])
    
def posi(used_positions):
    choice=''
    while choice not in ['0','1','2','3','4','5','6','7','8'] or choice in used_positions :
        choice=input("please choose an index between 0 and 8 and not choosen already")
    if choice in ['0','1','2','3','4','5','6','7','8']:
            used_positions.append(choice)
    return int(choice)
def replacement(lis,position,current_player):
    lis[position]=current_player
def check_winner(lis):
    if lis[0]==lis[1] and lis[1]==lis[2] :
        print("player {} won".format(lis[0]))
        return True
    elif lis[3]==lis[4] and lis[4]==lis[5] :
        print("player {} won".format(lis[4]))
        return True
    elif lis[6]==lis[7] and lis[7]==lis[8]:
        print("player {} won".format(lis[8]))
        return True
    elif lis[0]==lis[3] and lis[3]==lis[6]:
        print("player {} won".format(lis[0]))
        return True
    elif lis[1]==lis[4] and lis[4]==lis[7]:
        print("player {} won".format(lis[1]))
        return True
    elif lis[2]==lis[5] and lis[5]==lis[8]:
        print("player {} won".format(lis[2]))
        return True
    elif lis[0]==lis[4] and lis[4]==lis[8]:
        print("player {} won".format(lis[0]))
        return True
    elif lis[2]==lis[4] and lis[4]==lis[6]:
        print("player {} won".format(lis[2]))
        return True
    else:
        return False
def continue_game():
    game_on=''
    while game_on not in ['Y','N','y','n']:
        game_on=input("Do you want to continue playing:type Y or N")
    return game_on in ['Y','y']

#initialize:
game_on=True
while game_on:
    lis=['0','1','2','3','4','5','6','7','8']
    used_positions=[]
    print("welcome to the game! \n")
    player_1, player_2=players()
    print('player 1 is {} and player 2 is {}'.format(player_1,player_2))
    current_player=player_1
    next=True
    board(lis)
    while next:
       print("player {}, your turn".format(current_player))
       position=posi(used_positions)
       replacement(lis,position,current_player)
       board(lis)
       winner=check_winner(lis)
       if winner:
           print(winner)
           next=False
           break
       elif len(used_positions)==9:
           print("it's a tie,both of you wins")
           next=False
           break
       else:
           if current_player== player_1:
               current_player=player_2
           else:
               current_player=player_1
    game_on=continue_game()
        