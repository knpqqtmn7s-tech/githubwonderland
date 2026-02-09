from data.fake_db import games_db

def get_games():
    return games_db

def create_game(game_data):
    new_game = {
        "gameId": len(games_db) + 1,
        "title": game_data.title,
        "releaseDate": game_data.releaseDate
    }
    games_db.append(new_game)
    return new_game
