class Ball:
    def __init__(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.is_ghost = False

    def move(self):
        print(f"Movendo bola para ({self.x}, {self.y})")
        self.x += self.x_velocity
        self.y += self.y_velocity

    def bounce_horizontal(self):
        self.x_velocity = -self.x_velocity

    def bounce_vertical(self):
        self.y_velocity = -self.y_velocity

    def ball_hit(self):
        print("Bola colidiu")

    def turn_into_ghost(self):
        self.is_ghost = True
        print("Bola transformada em fantasma")
