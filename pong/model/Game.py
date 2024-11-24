from pong.model.Ball import Ball
from pong.model.Paddle import Paddle


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = Ball(screen_width // 2, screen_height // 2, 1, 1)
        self.paddle_left = Paddle(1, screen_height // 2 - 2, 5)
        self.paddle_right = Paddle(screen_width - 2, screen_height // 2 - 2, 5)
        self.score_left = 0
        self.score_right = 0

    def update(self):
        self.ball.move()
        # Bounce on top and bottom
        if self.ball.y <= 0 or self.ball.y >= self.screen_height - 1:
            print("Bola bateu no topo ou na parte inferior")
            self.ball.bounce_vertical()
        # Bounce on paddles
        if (self.ball.y in range(self.paddle_left.y, self.paddle_left.y + self.paddle_left.width) and
                self.ball.x == self.paddle_left.x):
            print("Bola bateu na raquete esquerda")
            self.ball.bounce_horizontal()
        if (self.ball.y in range(self.paddle_right.y, self.paddle_right.y + self.paddle_right.width) and
                self.ball.x == self.paddle_right.x):
            print("Bola bateu na raquete direita")
            self.ball.bounce_horizontal()
        # Scoring
        if self.ball.x <= 0:
            self.score_right += 1
            print("Jogador da direita marcou um ponto!")
            self.reset_ball()
        elif self.ball.x >= self.screen_width - 1:
            self.score_left += 1
            print("Jogador da esquerda marcou um ponto!")
            self.reset_ball()

    def reset_ball(self):
        self.ball.x = self.screen_width // 2
        self.ball.y = self.screen_height // 2
        self.ball.speed_x *= -1
