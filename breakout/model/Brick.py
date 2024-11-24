class Bricks:
    def __init__(self, x, y, width, height, point, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.point = point
        self.color = color
        self.visible = True

    def hit_brick(self, ball):
        self.visible = False
        print(f"Tijolo em ({self.x}, {self.y}) foi destruído")
        return self.point

    def draw(self):
        print(f"Desenhando tijolo na posição ({self.x}, {self.y})")
