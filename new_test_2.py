import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Katt-Man")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Pac-Man properties
pac_man_speed = 15  # Adjust the speed as needed
pac_man_direction = [pac_man_speed, 0]

# Load Pac-Man image
pac_man_startimage = pygame.image.load("kattManRight.png")
size_img = 50
pac_man_size = (size_img, size_img)  # Set the desired size for Pac-Man
pac_man_image = pygame.transform.scale(pac_man_startimage, pac_man_size)
pac_man_position = pac_man_image.get_rect()
pac_man_position.center = (width // 2, height // 2)  # Set the initial position of Pac-Man

# Wall properties
wall_thickness = 30
wall_width = 30  # Standard width for walls
walls = []

# Function to generate random wall positions
def generate_random_wall():
    wall_height = random.randint(50, 150)
    wall_width = random.randint(50, 150)
    x = random.randint(0, width - wall_width)
    y = random.randint(0, height - wall_height)
    is_vertical = random.choice([True, False])
    if is_vertical:
        return pygame.Rect(x, y, wall_thickness, wall_height)
    else:
        return pygame.Rect(x, y, wall_width, wall_thickness)

# Generate random walls
for _ in range(15):  # Adjust the number of walls as needed
    walls.append(generate_random_wall())

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and abs(pac_man_direction[0]) != abs(pac_man_speed):
                pac_man_direction = [pac_man_speed, 0]
            elif event.key == pygame.K_DOWN and abs(pac_man_direction[1]) != abs(pac_man_speed):
                pac_man_direction = [0, pac_man_speed]
            elif event.key == pygame.K_LEFT and abs(pac_man_direction[0]) != abs(pac_man_speed):
                pac_man_direction = [-pac_man_speed, 0]
            elif event.key == pygame.K_UP and abs(pac_man_direction[1]) != abs(pac_man_speed):
                pac_man_direction = [0, -pac_man_speed]

    pac_man_position[0] += pac_man_direction[0]
    pac_man_position[1] += pac_man_direction[1]

    # Wrap around the screen
    if pac_man_position.right < 0:
        pac_man_position.left = width
    elif pac_man_position.left > width:
        pac_man_position.right = 0
    elif pac_man_position.bottom < 0:
        pac_man_position.top = height
    elif pac_man_position.top > height:
        pac_man_position.bottom = 0

    # Collision detection with walls
    for wall in walls:
        if pac_man_position.colliderect(wall):
            # Pac-Man has collided with a wall, stop movement
            pac_man_position[0] -= pac_man_direction[0]
            pac_man_position[1] -= pac_man_direction[1]

    # Clear the screen
    screen.fill(black)

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, white, wall)

    # Draw wall around the screen
    pygame.draw.rect(screen, white, (0, 0, width, wall_thickness))  # Top wall
    pygame.draw.rect(screen, white, (0, 0, wall_thickness, height))  # Left wall
    pygame.draw.rect(screen, white, (0, height - wall_thickness, width, wall_thickness))  # Bottom wall
    pygame.draw.rect(screen, white, (width - wall_thickness, 0, wall_thickness, height))  # Right wall

    # Blit Pac-Man onto the screen
    screen.blit(pac_man_image, pac_man_position)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(30)
