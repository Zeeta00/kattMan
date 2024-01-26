import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Pac-Man properties
pac_man_position = [width // 2, height // 2]
pac_man_speed = 15  # Adjust the speed as needed
pac_man_direction = [pac_man_speed, 0]

# Load Pac-Man image

pac_man_startimage = pygame.image.load("kattManRight.png")
pac_man_right_open = pygame.image.load("kattManRight.png")
#pac_man_right_open = pygame.image.load("kattManRight.png")
#pac_man_right_open = pygame.image.load("kattManRight.png")
#pac_man_right_open = pygame.image.load("kattManRight.png")
#pac_man_right_open = pygame.image.load("kattManRight.png")



size_img = 50
pac_man_size = (size_img, size_img)  # Set the desired size for Pac-Man
pac_man_image = pygame.transform.scale(pac_man_startimage, pac_man_size)
pac_man_position = pac_man_image.get_rect()
pac_man_position.center = (width // 2, height // 2)  # Set the initial position of Pac-Man


# Wall properties
wall_thickness = 10

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

    # Check for collision with screen boundaries
    pac_man_position[0] = max(min(pac_man_position[0], width - size_img -wall_thickness), 0+wall_thickness)
    pac_man_position[1] = max(min(pac_man_position[1], height - size_img - wall_thickness), 0+wall_thickness)

    # Clear the screen
    screen.fill(black)

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
