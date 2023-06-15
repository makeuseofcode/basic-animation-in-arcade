import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.frame_counter = 0

    def on_draw(self):
        arcade.start_render()
        if self.frame_counter < 10:
            arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.BLUE)
        elif self.frame_counter < 20:
            arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.GREEN)
        else:
            arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.RED)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 10
            self.frame_counter = (self.frame_counter + 1) % 30
        elif key == arcade.key.RIGHT:
            self.player_x += 10
            self.frame_counter = (self.frame_counter + 1) % 30

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
