import arcade

class ExitDoor(arcade.Sprite):
    def __init__(self, x, y, size=32):
        super().__init__()

        # טקסטורה: ריבוע ירוק כהה
        self.texture = arcade.make_soft_square_texture(
            size,
            arcade.color.DARK_GREEN,
            255,
            255
        )

        # מיקום הדלת
        self.center_x = x
        self.center_y = y
