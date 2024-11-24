from Ball import *
from pong.model.Paddle import Paddle


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = Ball(screen_width // 2, screen_height - 3, 1, -1)
        self.pad = Paddle(screen_width // 2 - 5, screen_height - 1, 10, 2)
        self.bricks = self.create_bricks()
        self.points = 0
        self.lifes = 3

    def start_game(self):
        print("Jogo iniciado!")

    def create_bricks(self):
        bricks = []
        rows, cols = 5, 10
        brick_width = self.screen_width // cols
        for row in range(rows):
            for col in range(cols):
                bricks.append(bricks(col * brick_width, row, brick_width, 20, 1, (255, 0, 0)))
        return bricks

    def draw_bricks(self):
        for brick in self.bricks:
            brick.draw()

    def is_ball_hit_pad(self, ball, pad):
        return (ball.y == pad.y - 1 and pad.x <= ball.x < pad.x + pad.width)

    def is_ball_hit_brick(self, ball, brick):
        return brick.visible and brick.x <= ball.x < brick.x + brick.width and brick.y <= ball.y < brick.y + brick.height

    def is_ball_hit_wall(self, ball):
        return ball.x <= 0 or ball.x >= self.screen_width - 1

    def is_ball_out_of_bound(self, ball):
        return ball.y > self.screen_height

    def lose_life(self):
        self.lifes -= 1
        print(f"Você perdeu uma vida! Vidas restantes: {self.lifes}")
        if self.lifes <= 0:
            self.game_over()

    def update_points(self, points):
        self.points += points
        print(f"Pontos: {self.points}")

    def game_over(self):
        print("Fim de jogo!")

    def update(self):
        self.ball.move()

        # Colisão com paredes
        if self.is_ball_hit_wall(self.ball):
            print("Bola bateu na parede lateral")
            self.ball.bounce_horizontal()

        # Colisão com o teto
        if self.ball.y <= 0:
            print("Bola bateu no teto")
            self.ball.bounce_vertical()

        # Colisão com o pad
        if self.is_ball_hit_pad(self.ball, self.pad):
            print("Bola bateu no pad")
            self.ball.bounce_vertical()

        # Colisão com tijolos
        for brick in self.bricks:
            if self.is_ball_hit_brick(self.ball, brick):
                print("Bola destruiu um tijolo")
                brick.hit_brick(self.ball)
                self.update_points(brick.point)
                self.ball.bounce_vertical()

        # Bola fora do campo
        if self.is_ball_out_of_bound(self.ball):
            print("Bola saiu do campo")
            self.lose_life()
            return False

        return True
