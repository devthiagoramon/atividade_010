class Paddle:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width

    def move(self, direction, screen_width):
        if direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x + self.width < screen_width:
            self.x += 1
        elif direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < screen_width:
            self.y += 1
