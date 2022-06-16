'''Imports a random intiger.
   Returns ramdom intiger'''
from random import randint
GAME_IN_PROGRESS = True
GAME_RESULTS = []


def attack_func():
    '''Allocates intiger for player/opponent attack
    Returns random intiger between 10 and 20'''
    return randint(opponent['attack_min'],
                   opponent['attack_max'])


def end_of_game(winner_name):
    '''Allocates winner at end of game
    Returns print statement with winner name'''
    print(f'{winner_name} won this time')


# Main game loop
while GAME_IN_PROGRESS is True:
    COUNTER = 0
    ANOTHER_ROUND = True
    player = {'name': 'Matt', 'attack_min': 10,
              'attack_max': 20,  'heal': 16, 'health': 100}
    opponent = {'name': 'Max', 'attack_min': 10,
                'attack_max': 20, 'health': 100}

    print('--- ' * 11)
    print('Welcome to Mortal Typthon! Please enter player name:')
    player['name'] = input()

    print('--- ' * 6)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(opponent['name'] + ' has ' + str(opponent['health']) + ' health')

    # Recurring round loop
    while ANOTHER_ROUND is True:

        COUNTER = COUNTER + 1
        PLAYER_WON = False
        OPPONENT_WON = False

        print('--- ' * 6)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Display Results')

        player_selection = input()

        if player_selection == '1':
            opponent['health'] = opponent['health'] - attack_func()
            if opponent['health'] <= 0:
                PLAYER_WON = True
            else:
                player['health'] = player['health'] - attack_func()
                if player['health'] <= 0:
                    OPPONENT_WON = True

        elif player_selection == '2':
            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] - attack_func()
            if player['health'] <= 0:
                OPPONENT_WON = True

        elif player_selection == '3':
            ANOTHER_ROUND = False
            GAME_IN_PROGRESS = False

        elif player_selection == '4':
            for player_stats in GAME_RESULTS:
                print(player_stats)

        else:
            print('invalid Input')

        if PLAYER_WON is False and OPPONENT_WON is False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(opponent['name'] + ' has ' + str(
                opponent['health']) + ' left')

        elif PLAYER_WON:
            end_of_game(player['name'])
            game_result = {'name': player['name'], 'health': player['health'],
                           'no of rounds': COUNTER}
            GAME_RESULTS.append(game_result)
            ANOTHER_ROUND = False

        elif OPPONENT_WON:
            end_of_game(opponent['name'])
            game_result = {'name': player['name'], 'health': player['health'],
                           'no of rounds': COUNTER}
            GAME_RESULTS.append(game_result)
            ANOTHER_ROUND = False
