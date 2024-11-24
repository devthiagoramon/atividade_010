from pong.model.Game import Game
import time


def main():
    screen_width, screen_height = 40, 20
    game = Game(screen_width, screen_height)
    game.start_game()

    while True:
        print("\n" + "=" * 40)
        game.update()
        print("=" * 40)
        time.sleep(0.5)

        # Encerrar o jogo se necessário
        if game.points_player_1 >= 10 or game.points_player_2 >= 10:
            game.game_over()
            break


if __name__ == '__main__':
    main()
