class Pad:
    def __init__(self, x, y, width, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = 10
        self.speed = speed

    def go_right(self):
        self.x += self.speed
        print("Pad movido para a direita")

    def go_left(self):
        self.x -= self.speed
        print("Pad movido para a esquerda")

    def draw(self):
        print(f"Desenhando pad na posição ({self.x}, {self.y})")
