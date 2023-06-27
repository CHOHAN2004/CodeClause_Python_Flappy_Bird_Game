import pygame
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 400
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird properties
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
bird_velocity = 0
gravity = 0.3
jump_strength = 6

# Pipe properties
pipe_width = 70
pipe_height = 400
pipe_x = WIDTH
pipe_y = 0
pipe_gap = 150
pipe_speed = 2

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

game_started = False

def draw_bird():
    pygame.draw.circle(window, BLUE, (bird_x, int(bird_y)), bird_radius)

def draw_pipe():
    pygame.draw.rect(window, WHITE, (pipe_x, pipe_y, pipe_width, pipe_height))
    pygame.draw.rect(window, WHITE, (pipe_x, pipe_y + pipe_height + pipe_gap, pipe_width, HEIGHT))

def check_collision():
    if bird_y > HEIGHT - bird_radius or bird_y < bird_radius:
        return True
    if pipe_x <= bird_x <= pipe_x + pipe_width:
        if bird_y - bird_radius < pipe_height or bird_y + bird_radius > pipe_height + pipe_gap:
            return True
    return False

def update_score():
    global score
    score += 1

def display_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_started:
                game_started = True
                bird_velocity = -jump_strength
            elif event.key == pygame.K_UP and game_started:
                bird_velocity = -jump_strength
            elif event.key == pygame.K_DOWN and game_started:
                bird_velocity = jump_strength

    if not game_started:
        # Clear the window
        window.fill((0, 0, 0))
        start_text = font.render("Press SPACE to start", True, WHITE)
        window.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))
        pygame.display.flip()
        continue

    # Update bird position and velocity
    bird_velocity += gravity
    bird_y += bird_velocity

    # Update pipe position
    pipe_x -= pipe_speed

    # Check collision
    if check_collision():
        pygame.quit()
        sys.exit()

    # Check if pipe is off the screen
    if pipe_x + pipe_width < 0:
        pipe_x = WIDTH
        pipe_height = pygame.time.get_ticks() % 200 + 100
        update_score()

    # Clear the window
    window.fill((0, 0, 0))

    # Draw the bird and pipe
    draw_bird()
    draw_pipe()

    # Display the score
    display_score()

    # Update the display
    pygame.display.flip()

    # Set the FPS
    clock.tick(60)
