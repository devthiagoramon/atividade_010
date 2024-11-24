from breakout.model.Ball import Ball
from breakout.model.Brick import Brick
from breakout.model.Paddle import Paddle


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = Ball(screen_width // 2, screen_height - 3, 1, -1)
        self.paddle = Paddle(screen_width // 2 - 5, screen_height - 1, 10)
        self.bricks = self.create_bricks()

    def create_bricks(self):
        bricks = []
        rows, cols = 5, 10
        brick_width = self.screen_width // cols
        for row in range(rows):
            for col in range(cols):
                bricks.append(Brick(col * brick_width, row))
        return bricks

    def update(self):
        self.ball.move()
        # Bounce on walls
        if self.ball.x <= 0 or self.ball.x >= self.screen_width - 1:
            print("Bola bateu na parede lateral")
            self.ball.bounce_horizontal()
        if self.ball.y <= 0:
            print("Bola bateu no teto")
            self.ball.bounce_vertical()
        # Bounce on paddle
        if (self.ball.y == self.paddle.y - 1 and
                self.paddle.x <= self.ball.x < self.paddle.x + self.paddle.width):
            print("Bola bateu na raquete")
            self.ball.bounce_vertical()
        # Check collision with bricks
        for brick in self.bricks:
            if brick.visible and brick.x == self.ball.x and brick.y == self.ball.y:
                print("Bola destruiu um tijolo")
                brick.visible = False
                self.ball.bounce_vertical()
        # Ball out of bounds
        if self.ball.y > self.screen_height:
            print("Bola saiu da tela. Fim de jogo!")
            return False
        return True
