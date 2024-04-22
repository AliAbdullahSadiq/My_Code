import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for the game
FULLSCREEN_MODE = False  # Set to True for full-screen, False for windowed mode

# Get the size of the current display
display_info = pygame.display.Info()
DISPLAY_WIDTH, DISPLAY_HEIGHT = display_info.current_w, display_info.current_h

# Set the window size to full screen or half screen based on FULLSCREEN_MODE
if FULLSCREEN_MODE:
    SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAY_WIDTH, DISPLAY_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
else:
    SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Pong')

# Constants
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 15, int(SCREEN_HEIGHT * 0.125)  # Paddle height is 12.5% of screen height
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
BALL_SPEED_INCREMENT = 0.5 # The amount by which to increase ball speed after each score
PADDLE_SPEED = 5  # The speed of the paddles

# Initialize font
font = pygame.font.Font(None, 74)

# Initialize positions and velocities
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_vel = [random.choice((-3, 3)), random.choice((-3, 3))]
paddle1_pos = [10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2]
paddle2_pos = [SCREEN_WIDTH - PADDLE_WIDTH - 10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2]
paddle1_vel = [0, 0]  # [X, Y] velocity for the left paddle
paddle2_vel = [0, 0]  # [X, Y] velocity for the right paddle

# Initialize scores
score1 = 0
score2 = 0

# Initialize the clock
clock = pygame.time.Clock()

def ball_reset(side):
    global ball_pos, ball_vel
    # Place the ball just outside the screen on the side it exited
    ball_pos = [-BALL_SIZE, SCREEN_HEIGHT // 2] if side == "left" else [SCREEN_WIDTH, SCREEN_HEIGHT // 2]
    # Give the ball a momentary pause before moving towards the center
    ball_vel = [random.choice((2, -2)), 0]

def increase_ball_speed():
    global ball_vel
    ball_vel[0] += BALL_SPEED_INCREMENT if ball_vel[0] > 0 else -BALL_SPEED_INCREMENT
    ball_vel[1] += BALL_SPEED_INCREMENT if ball_vel[1] > 0 else -BALL_SPEED_INCREMENT

def game_over_screen():
    screen.fill(BLACK)
    text = font.render('Game Over', True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(text, text_rect)
    
    final_score_text = font.render(f"Final Score: {score1} - {score2}", True, WHITE)
    final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(final_score_text, final_score_rect)
    
    pygame.display.flip()
    pygame.time.wait(3000)

# Game loop
running = True
game_over = False
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if FULLSCREEN_MODE and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Allow exiting full-screen with ESC
                running = False

    if not game_over:
        # Move the ball
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # Ball collision with top and bottom
        if ball_pos[1] <= 0 or ball_pos[1] >= SCREEN_HEIGHT - BALL_SIZE:
            ball_vel[1] = -ball_vel[1]

        # Ball collision with paddles
        if paddle1_pos[0] < ball_pos[0] < paddle1_pos[0] + PADDLE_WIDTH and paddle1_pos[1] < ball_pos[1] + BALL_SIZE // 2 < paddle1_pos[1] + PADDLE_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_pos[0] = paddle1_pos[0] + PADDLE_WIDTH  # Move the ball outside the paddle
        elif paddle2_pos[0] < ball_pos[0] + BALL_SIZE < paddle2_pos[0] + PADDLE_WIDTH and paddle2_pos[1] < ball_pos[1] + BALL_SIZE // 2 < paddle2_pos[1] + PADDLE_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_pos[0] = paddle2_pos[0] - BALL_SIZE  # Move the ball outside the paddle

        # Update paddle positions based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1_vel[1] = -PADDLE_SPEED
        elif keys[pygame.K_s]:
            paddle1_vel[1] = PADDLE_SPEED
        else:
            paddle1_vel[1] = 0
        
        if keys[pygame.K_a] and paddle1_pos[0] > 0:
            paddle1_vel[0] = -PADDLE_SPEED
        elif keys[pygame.K_d] and paddle1_pos[0] < SCREEN_WIDTH * 0.3 - PADDLE_WIDTH:
            paddle1_vel[0] = PADDLE_SPEED
        else:
            paddle1_vel[0] = 0
        
        if keys[pygame.K_UP]:
            paddle2_vel[1] = -PADDLE_SPEED
        elif keys[pygame.K_DOWN]:
            paddle2_vel[1] = PADDLE_SPEED
        else:
            paddle2_vel[1] = 0
        
        if keys[pygame.K_LEFT] and paddle2_pos[0] > SCREEN_WIDTH * 0.7:
            paddle2_vel[0] = -PADDLE_SPEED
        elif keys[pygame.K_RIGHT] and paddle2_pos[0] < SCREEN_WIDTH - PADDLE_WIDTH:
            paddle2_vel[0] = PADDLE_SPEED
        else:
            paddle2_vel[0] = 0

        # Update paddle positions
        paddle1_pos[0] += paddle1_vel[0]
        paddle1_pos[1] += paddle1_vel[1]
        paddle2_pos[0] += paddle2_vel[0]
        paddle2_pos[1] += paddle2_vel[1]

        # Keep paddles on the screen and within their respective 30% boundaries
        paddle1_pos[0] = max(0, min(SCREEN_WIDTH * 0.3 - PADDLE_WIDTH, paddle1_pos[0]))
        paddle1_pos[1] = max(0, min(SCREEN_HEIGHT - PADDLE_HEIGHT, paddle1_pos[1]))
        paddle2_pos[0] = max(SCREEN_WIDTH * 0.7, min(SCREEN_WIDTH - PADDLE_WIDTH, paddle2_pos[0]))
        paddle2_pos[1] = max(0, min(SCREEN_HEIGHT - PADDLE_HEIGHT, paddle2_pos[1]))

        # Ball out of bounds
        if ball_pos[0] < -BALL_SIZE:
            score2 += 1
            ball_reset("left")
            increase_ball_speed()  # Increase ball speed after scoring
        elif ball_pos[0] > SCREEN_WIDTH:
            score1 += 1
            ball_reset("right")
            increase_ball_speed()  # Increase ball speed after scoring

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (*paddle1_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE, (*paddle2_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.ellipse(screen, WHITE, (*ball_pos, BALL_SIZE, BALL_SIZE))
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