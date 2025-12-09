import arcade

class Wall(arcade.Sprite):
    def __init__(self, x, y, size=32):
        super().__init__()
        # ריבוע כחול כהה
        self.texture = arcade.make_soft_square_texture(
            size,
            arcade.color.DARK_BLUE,
            255,
            255
        )
        self.center_x = x
        self.center_y = y
