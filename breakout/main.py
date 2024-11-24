from model.Game import Game
import time


def main():
    screen_width, screen_height = 40, 20
    game = Game(screen_width, screen_height)
    game.start_game()

    while True:
        if not game.update():
            break
        time.sleep(0.5)


if __name__ == '__main__':
    main()
