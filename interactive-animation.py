import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interactive Animation")

# Player properties
player_x = 400
player_y = 300
player_radius = 30
player_color = RED

# Animation properties
animation_radius = 60
animation_color = WHITE
animation_active = False

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.Rect(player_x - player_radius, player_y - player_radius,
                           2 * player_radius, 2 * player_radius).collidepoint(mouse_pos):
                animation_active = True

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

    # Update the animation
    if animation_active:
        pygame.draw.circle(screen, animation_color, (player_x, player_y), animation_radius)
        animation_radius += 1
        if animation_radius > 100:
            animation_active = False
            animation_radius = 0

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
