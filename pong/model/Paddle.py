class Paddle:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.width = 1
        self.height = height
        self.speed = 5

    def go_up(self):
        self.y -= 1
        print(f"Raquete movida para cima: nova posição ({self.x}, {self.y})")

    def go_down(self):
        self.y += 1
        print(f"Raquete movida para baixo: nova posição ({self.x}, {self.y})")

    def draw(self):
        print(f"Desenhando raquete na posição ({self.x}, {self.y})")
