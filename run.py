player_name = 'Matt'
player_attack = 10
player_heal = 16
health = 100

player = {'name': 'Matt', 'attack': 10, 'heal': 16, 'health': 100}
opponent = {'name': 'Max', 'attack': 12, 'health': 100}
game_in_progress = True

while game_in_progress == True:

    print('Please select action')
    print('1) Attack')
    print('2) Heal')

    player_selection = input()
    if player_selection == '1':
        opponent['health'] = opponent['health'] - player['attack']
        player['health'] = player['health'] - opponent['attack']
        print(opponent['health'])
        print(player['health'])
    elif player_selection == '2':
        print('Heal player')
    else:
        print('invalid Input')