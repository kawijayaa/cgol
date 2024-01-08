import os
import random
import time

def display_game(game):
    for y in range(len(game)):
        print(" ".join(game[y]))

def tick(game):
    for y in range(len(game)):
        for x in range(len(game[y])):
            if (get_neighbor(game, x, y) < 2 or get_neighbor(game, x, y) > 3) and game[y][x] == "■":
                game[y][x] = " "
            elif get_neighbor(game, x, y) == 3 and game[y][x] == " ":
                game[y][x] = "■"
    
    return game

def get_neighbor(game, x, y):
    count = 0
    for y_check in range(y-1, y+2):
        for x_check in range(x-1, x+2):
            if (y_check in range(0, len(game)) and x_check in range(0, len(game))) and game[y_check][x_check] == "■":
                count += 1

    return count 

if __name__ == "__main__":
    GAME_SIZE = 40
    CHANCE = random.random()*10 + 5

    game = [[random.choices(["■", " "], cum_weights=(CHANCE, 100-CHANCE))[0] for _ in range(GAME_SIZE)] for _ in range(GAME_SIZE)] 

    while True:
        os.system("clear")
        display_game(game)
        game = tick(game)
        time.sleep(0.075)