class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.x_velocity = 1
        self.y_velocity = 1

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        print(f"Bola movida para ({self.x}, {self.y})")

    def bounce_horizontal(self):
        self.x_velocity = -self.x_velocity
        print("Bola mudou de direção horizontal")

    def bounce_vertical(self):
        self.y_velocity = -self.y_velocity
        print("Bola mudou de direção vertical")

    def ball_hit(self):
        print("A bola foi atingida!")
