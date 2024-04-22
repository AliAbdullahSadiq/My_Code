import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Initialize font
font = pygame.font.Font(None, 74)

# Initialize positions
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_vel = [random.choice((-2, 2)), random.choice((-2, 2))]
paddle1_pos = [10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2]
paddle2_pos = [SCREEN_WIDTH - PADDLE_WIDTH - 10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2]
ball_speed = 2

# Initialize scores
score1 = 0
score2 = 0

# Initialize the clock
clock = pygame.time.Clock()

def ball_reset():
    global ball_pos, ball_vel, ball_speed
    ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    
    # Increase speed as the score increases
    ball_speed += 0.3
    
    # Randomize the direction
    ball_vel = [random.choice((-ball_speed, ball_speed)), random.choice((-ball_speed, ball_speed))]

def game_over_screen():
    screen.fill(BLACK)
    text = font.render('Game Over', True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()

# Game loop
running = True
game_over = False
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Move the ball
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # Ball collision with top and bottom
        if ball_pos[1] - BALL_SIZE // 2 <= 0 or ball_pos[1] + BALL_SIZE // 2 >= SCREEN_HEIGHT:
            ball_vel[1] = -ball_vel[1]

        # Ball collision with paddles
        ball_rect = pygame.Rect(ball_pos[0] - BALL_SIZE // 2, ball_pos[1] - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        paddle1_rect = pygame.Rect(paddle1_pos[0], paddle1_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT)
        paddle2_rect = pygame.Rect(paddle2_pos[0], paddle2_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT)

        if ball_rect.colliderect(paddle1_rect) or ball_rect.colliderect(paddle2_rect):
            ball_vel[0] = -ball_vel[0]

        # Ball out of bounds
        if ball_pos[0] < 0:
            score2 += 1
            ball_reset()
        elif ball_pos[0] > SCREEN_WIDTH - BALL_SIZE:
            score1 += 1
            ball_reset()

        # Update paddle positions based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_pos[1] > 0:
            paddle1_pos[1] -= 5
        if keys[pygame.K_s] and paddle1_pos[1] < SCREEN_HEIGHT - PADDLE_HEIGHT:
            paddle1_pos[1] += 5
        if keys[pygame.K_UP] and paddle2_pos[1] > 0:
            paddle2_pos[1] -= 5
        if keys[pygame.K_DOWN] and paddle2_pos[1] < SCREEN_HEIGHT - PADDLE_HEIGHT:
            paddle2_pos[1] += 5

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (*paddle1_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE, (*paddle2_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.ellipse(screen, WHITE, (ball_pos[0] - BALL_SIZE // 2, ball_pos[1] - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE))
        score_text = font.render(f"{score1}  {score2}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 10))

        # Game Over condition
        if score1 == 10 or score2 == 10:
            game_over = True

    else:
        game_over_screen()
        running = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
