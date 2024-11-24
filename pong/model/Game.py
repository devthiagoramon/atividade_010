from Ball import Ball
from Paddle import Paddle


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = Ball(screen_width // 2, screen_height // 2)
        self.player_1 = Paddle(2, screen_height // 2 - 2, 5)
        self.player_2 = Paddle(screen_width - 3, screen_height // 2 - 2, 5)
        self.points_player_1 = 0
        self.points_player_2 = 0

    def start_game(self):
        print("Jogo iniciado!")

    def is_ball_hit_pad_1(self, ball, pad):
        return (
            ball.y in range(pad.y, pad.y + pad.height)
            and ball.x == pad.x + 1
        )

    def is_ball_hit_pad_2(self, ball, pad):
        return (
            ball.y in range(pad.y, pad.y + pad.height)
            and ball.x == pad.x - 1
        )

    def is_ball_hit_wall(self, ball):
        return ball.y <= 0 or ball.y >= self.screen_height - 1

    def is_ball_out_of_bound_player_1(self, ball):
        return ball.x <= 0

    def is_ball_out_of_bound_player_2(self, ball):
        return ball.x >= self.screen_width - 1

    def update_points_player_1(self, points_ply_1):
        self.points_player_1 += points_ply_1
        print(f"Pontos do jogador 1: {self.points_player_1}")

    def update_points_player_2(self, points_ply_2):
        self.points_player_2 += points_ply_2
        print(f"Pontos do jogador 2: {self.points_player_2}")

    def game_over(self):
        print("Fim de jogo!")
        print(f"Pontos finais - Jogador 1: {self.points_player_1}, Jogador 2: {self.points_player_2}")

    def update(self):
        self.ball.move()

        # Verificar colisões com paredes
        if self.is_ball_hit_wall(self.ball):
            self.ball.bounce_vertical()

        # Verificar colisões com as raquetes
        if self.is_ball_hit_pad_1(self.ball, self.player_1):
            self.ball.bounce_horizontal()

        if self.is_ball_hit_pad_2(self.ball, self.player_2):
            self.ball.bounce_horizontal()

        # Verificar se a bola saiu do campo
        if self.is_ball_out_of_bound_player_1(self.ball):
            self.update_points_player_2(1)
            self.reset_ball()

        elif self.is_ball_out_of_bound_player_2(self.ball):
            self.update_points_player_1(1)
            self.reset_ball()

    def reset_ball(self):
        self.ball.x = self.screen_width // 2
        self.ball.y = self.screen_height // 2
        self.ball.bounce_horizontal()
