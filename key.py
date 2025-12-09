import arcade

class Key(arcade.Sprite):
    def __init__(self, x, y, texture_path="assets/key.png"):
        super().__init__(texture_path, scale=1.0)

        # מאפייני המחלקה כפי שהוגדרו בתרגיל
        self.texture = arcade.load_texture(texture_path)  # הטקסטורה של המפתח
        self.center_x = x  # מיקום בציר X
        self.center_y = y  # מיקום בציר Y