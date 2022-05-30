from random import randint
GAME_IN_PROGRESS = True


def opponent_attack_func():
    return randint(opponent['attack_min'],
                   opponent['attack_max'])


while GAME_IN_PROGRESS is True:
    ANOTHER_ROUND = True
    player = {'name': 'Matt', 'attack': 10, 'heal': 16, 'health': 100}
    opponent = {'name': 'Max', 'attack_min': 10,
                'attack_max': 20, 'health': 100}

    print('--- ' * 8)
    print('Enter player name')
    player['name'] = input()

    print('--- ' * 8)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(opponent['name'] + ' has ' + str(opponent['health']) + ' health')

    while ANOTHER_ROUND is True:
        PLAYER_WON = False
        OPPONENT_WON = False

        print('--- ' * 8)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

        player_selection = input()

        if player_selection == '1':
            opponent['health'] = opponent['health'] - player['attack']
            if opponent['health'] <= 0:
                PLAYER_WON = True
            else:
                player['health'] = player['health'] - opponent_attack_func()
                if player['health'] <= 0:
                    OPPONENT_WON = True

        elif player_selection == '2':
            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] - opponent_attack_func()
            if player['health'] <= 0:
                OPPONENT_WON = True

        elif player_selection == '3':
            ANOTHER_ROUND = False
            GAME_IN_PROGRESS = False
        else:
            print('invalid Input')

        if PLAYER_WON is False and OPPONENT_WON is False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(opponent['name'] + ' has ' + str(
                opponent['health']) + ' left')

        elif PLAYER_WON:
            print(player['name'] + ' won')
            ANOTHER_ROUND = False

        elif OPPONENT_WON:
            print('Your Opponent wins!')
            ANOTHER_ROUND = False
