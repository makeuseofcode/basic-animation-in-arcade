import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.frame_counter = 0
        self.frames = [arcade.color.BLUE, arcade.color.GREEN, arcade.color.RED]
        self.frame_rate = 1  # Adjust this value to control the animation speed

    def on_draw(self):
        arcade.start_render()
        frame_index = self.frame_counter // self.frame_rate % len(self.frames)
        if self.player_x < SCREEN_WIDTH // 2:
            frame_index = len(self.frames) - 1 - frame_index
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, self.frames[frame_index])

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 10
            self.frame_counter += 1
        elif key == arcade.key.RIGHT:
            self.player_x += 10
            self.frame_counter += 1

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
