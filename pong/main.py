from model.Game import Game
import time


def main():
    screen_width, screen_height = 40, 20
    game = Game(screen_width, screen_height)
    while True:
        print("\n" + "=" * 40)
        game.update()
        time.sleep(0.5)
        print("\n" + "=" * 40)


if __name__ == '__main__':
    main()
