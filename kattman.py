import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Pac-Man properties
pac_man_position = [width // 2, height // 2]
pac_man_speed = 5  # Adjust the speed as needed
pac_man_direction = [pac_man_speed, 0]

# Load Pac-Man image
pac_man_image = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.circle(pac_man_image, yellow, (15, 15), 15)
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and abs(pac_man_direction[1]) == abs(pac_man_speed):
                pac_man_direction = [pac_man_speed, 0]
            elif event.key == pygame.K_DOWN and abs(pac_man_direction[0]) == abs(pac_man_speed):
                pac_man_direction = [0, pac_man_speed]
            elif event.key == pygame.K_LEFT and abs(pac_man_direction[1]) == abs(pac_man_speed):
                pac_man_direction = [-pac_man_speed, 0]
            elif event.key == pygame.K_UP and abs(pac_man_direction[0]) == abs(pac_man_speed):
                pac_man_direction = [0, -pac_man_speed]

    pac_man_position[0] += pac_man_direction[0]
    pac_man_position[1] += pac_man_direction[1]

    # Clear the screen
    screen.fill(black)

    # Blit Pac-Man onto the screen
    screen.blit(pac_man_image, pac_man_position)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(30)
