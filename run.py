Player_Name = 'Matt'
Player_Attack = 10
Player_Health = 16
Health = 100

Player = {'name': 'Matt', 'attack': 10, 'heal': 16, 'health': 100}
Opponent = {'name': 'Max', 'attack': 12, 'health': 100}
Game_In_Progress = True

while Game_In_Progress == True:

    print('Please select action')
    print('1) Attack')
    print('2) Heal')

    Player_Selection = input()
    if Player_Selection == '1':
        Opponent['health'] = Opponent['health'] - Player['attack']
        Player['health'] = Player['health'] - Opponent['attack']
        print(Opponent['health'])
        print(Player['health'])
    elif Player_Selection == '2':
        print('Heal player')
    else:
        print('invalid Input')
        
    if Player['health'] <= 0:
        Game_In_Progress = False


        