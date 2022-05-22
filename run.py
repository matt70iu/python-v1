PLAYER_NAME = 'Matt'
PLAYER_ATTACK = 10
PLAYER_HEAL = 16
HEALTH = 100

player = {'name': 'Matt', 'attack': 10, 'heal': 16, 'health': 100}
opponent = {'name': 'Max', 'attack': 12, 'health': 100}
GAME_IN_PROGRESS = True

while GAME_IN_PROGRESS is True:

    PLAYER_WON = False
    OPPONENT_WON = False

    print('Please select action')
    print('1) Attack')
    print('2) Heal')

    player_selection = input()

    if player_selection == '1':
        opponent['health'] = opponent['health'] - player['attack']
        if opponent['health'] <= 0:
            PLAYER_WON = True         
        else:
            player['health'] = player['health'] - opponent['attack']
            if player['health'] <= 0:
                OPPONENT_WON = True              

        print(opponent['health'])
        print(player['health'])
    elif player_selection == '2':
        print('Heal player')
    else:
        print('invalid Input')

    if PLAYER_WON is True or OPPONENT_WON is True:
        GAME_IN_PROGRESS = False
