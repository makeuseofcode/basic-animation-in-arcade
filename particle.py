import arcade
import random

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Particle class
class Particle:
    def __init__(self, x, y, dx, dy, radius, color, lifespan):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        self.lifespan = lifespan

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.lifespan -= 1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

# Game class
class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Particle Example")
        self.particles = []

    def setup(self):
        # Create particles
        for _ in range(100):
            x = random.randrange(SCREEN_WIDTH)
            y = random.randrange(SCREEN_HEIGHT)
            dx = random.uniform(-1, 1)
            dy = random.uniform(-1, 1)
            radius = random.uniform(2, 5)
            color = arcade.color.WHITE
            lifespan = random.randint(60, 120)
            particle = Particle(x, y, dx, dy, radius, color, lifespan)
            self.particles.append(particle)

    def on_draw(self):
        arcade.start_render()
        for particle in self.particles:
            particle.draw()

    def update(self, delta_time):
        for particle in self.particles:
            particle.update()

            if particle.lifespan <= 0:
                self.particles.remove(particle)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
