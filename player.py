import json
import os
import random
from websocket import create_connection

# Game configuration, set coresrv in hostfile
server_url = 'ws://coresrv:9091'
player_name = os.environ.get('PLAYER', 'PLAYER')

# WebSocket connection
ws = create_connection(server_url)

# Game state
game_state = {
    'tick': 0,
    'players': [],
    'systems': {},
    'fleets': [],
    'stats': {
        'ship_cnt': [],
        'system_cnt': [],
    },
}

# Function to send moves to the server
def send_move(origin_id, destination_id, ship_count):
    move = f'MOV {player_name} {origin_id} {destination_id} {ship_count}'
    print('Sending data: ' + move)
    ws.send(move)

# Function to send upgrades to the server
def send_upgrade(destination_id):
    move = f'UPG {player_name} {destination_id}'
    print('Sending data: ' + move)
    ws.send(move)

# Strategy function (to be implemented)
def make_move():
    # Implement your game strategy here
    # Analyze the current game state (game_state object)
    # Make decisions on which moves to make
    # Use the send_move function to send moves to the server
    for system_id, system in game_state['systems'].items():
        if len(system['fleets']) == 1 and system['fleets'][0]['owner'] == player_name and system['fleets'][0]['count'] > 20:
            if random.random() < 0.5:
                random_target = random.randint(0, len(game_state['systems']) - 1)
                send_move(system['id'], random_target, system['fleets'][0]['count'])
            else:
                send_upgrade(system['id'])

# WebSocket event loop
while True:
    message = ws.recv()
    data = json.loads(message)

    # Update game state based on the received message
    game_state['tick'] = data['tick']
    game_state['players'] = data['players']
    game_state['stats'] = data['stats']
    print(f"Processing tick: {game_state['tick']}")

    # Update systems dictionary
    for system in data['systems']:
        game_state['systems'][system['id']] = system

    game_state['fleets'] = data['fleets']

    # Call the strategy function to make moves
    make_move()

# Close the WebSocket connection
ws.close()
