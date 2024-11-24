class Ball:
    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        print(f"Posição da bola ({self.x}, {self.y})")
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce_horizontal(self):
        self.speed_x = -self.speed_x

    def bounce_vertical(self):
        self.speed_y = -self.speed_y
