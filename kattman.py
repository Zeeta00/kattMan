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
pac_man_direction = [0, 0]

# Load Pac-Man image

pac_man_image = pygame.image.load("kattManRight.png")
# pygame.draw.circle(pac_man_image, yellow, (15, 15), 15)

pac_man_size = (50, 50)  # Set the desired size for Pac-Man
pac_man_image = pygame.transform.scale(pac_man_image, pac_man_size)
pac_man_position = pac_man_image.get_rect()
pac_man_position.center = (width // 2, height // 2)  # Set the initial position of Pac-Man


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pac_man_direction = [pac_man_speed, 0]
            elif event.key == pygame.K_DOWN:
                pac_man_direction = [0, pac_man_speed]
            elif event.key == pygame.K_LEFT:
                pac_man_direction = [-pac_man_speed, 0]
            elif event.key == pygame.K_UP:
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
