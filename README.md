# Hyxor Game Bot

This is a Python script for playing the Hyxor game using a WebSocket connection. The script connects to the game server, receives game state updates, and sends moves based on a predefined strategy.

## Prerequisites

- Python 3.x
- `websocket-client` library

## Installation

1. Clone the repository or download the script file.

2. Create a virtual environment (optional but recommended):

`python -m venv venv`

3. Activate the virtual environment:
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required dependencies using the provided `requirements.txt` file:

`pip install -r requirements.txt`

## Configuration

- `server_url`: The URL of the game server's WebSocket endpoint. Default is `'ws://coresrv:9091'`.
- `player_name`: The name of the player. Default is `'PLAYER'`. You can set it using the `PLAYER` environment variable.

## Usage

1. Make sure the game server is running and accessible at the specified `server_url`.

2. Run the script using the following command:

`python player.py`

3. The script will connect to the game server and start receiving game state updates.

4. Implement your game strategy in the `make_move()` function. Analyze the current game state (`game_state` object) and make decisions on which moves to make. Use the `send_move()` function to send moves to the server.

5. The script will continuously process game state updates and call the `make_move()` function to make moves based on your strategy.

6. The game will continue until the server closes the connection.

### Testing with Docker

1. Make sure you have Docker installed.
2. Test building the image
`docker build .`
3. Record the image id
4. Download the trial server for dots at [hyxor.com/akama/dots](https://hyxor.com)
`docker pull registry.hyxor.com/akama/dots`
5. Run the game container
`docker run -p 9090:9090 -p 9091:9091 -e LEVEL=level_one --hostname coresrv registry.hyxor.com/akama/dots`
6. Run the player
`docker run <ID>`

## Game State

The game state is stored in the `game_state` dictionary, which contains the following information:

- `tick`: The current tick number.
- `players`: A list of players in the game.
- `systems`: A dictionary of systems, where the keys are system IDs and the values are system objects.
- `fleets`: A list of fleet objects.
- `stats`: A dictionary containing game statistics, such as ship count and system count.

## Sending Moves

To send moves to the server, use the following functions:

- `send_move(origin_id, destination_id, ship_count)`: Sends a move command to move ships from the origin system to the destination system.
- `send_upgrade(destination_id)`: Sends an upgrade command to upgrade a system.

## Customization

Feel free to modify the script and implement your own game strategy in the `make_move()` function. Analyze the game state, make decisions based on the game rules and objectives, and send appropriate moves to the server.

