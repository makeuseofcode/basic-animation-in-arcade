import arcade

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Interactive Animation")
        self.player_x = 400
        self.player_y = 300
        self.player_radius = 30
        self.player_color = RED
        self.animation_radius = 60
        self.animation_color = WHITE
        self.animation_active = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, 
                                  self.player_y, 
                                  self.player_radius, 
                                  self.player_color)
        if self.animation_active:
            arcade.draw_circle_filled(self.player_x, 
                                       self.player_y, 
                                       self.animation_radius, 
                                       self.animation_color)

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.player_x - self.player_radius <= 
            x <= self.player_x + self.player_radius and
                self.player_y - self.player_radius <= 
            y <= self.player_y + self.player_radius):
            self.animation_active = True

    def update(self, delta_time):
        if self.animation_active:
            self.animation_radius += 1
            if self.animation_radius > 100:
                self.animation_active = False
                self.animation_radius = 0

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
