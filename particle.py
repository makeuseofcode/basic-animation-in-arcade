import pygame
import random

# Initialize Pygame
pygame.init()

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

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Particle System")

# Particle list
particles = []

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Create new particles
    for _ in range(10):
        x = random.uniform(0, SCREEN_WIDTH)
        y = random.uniform(0, SCREEN_HEIGHT)
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)
        radius = random.uniform(2, 5)
        color = WHITE
        lifespan = random.randint(30, 60)
        particle = Particle(x, y, dx, dy, radius, color, lifespan)
        particles.append(particle)

    # Update particles
    for particle in particles:
        particle.update()
        if particle.lifespan <= 0:
            particles.remove(particle)

    # Draw particles
    for particle in particles:
        particle.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
