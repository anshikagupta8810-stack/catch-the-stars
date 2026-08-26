import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Stars")

clock = pygame.time.Clock()

# Colors
BLACK = (15, 15, 30)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
BLUE = (50, 150, 255)
RED = (255, 80, 80)

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 70)

# Basket
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 60
basket_speed = 8

# Star
star_size = 20
star_x = random.randint(0, WIDTH - star_size)
star_y = -star_size
star_speed = 5

score = 0
lives = 3


def reset_star():
    global star_x, star_y, star_speed

    star_x = random.randint(0, WIDTH - star_size)
    star_y = -star_size
    star_speed = 5 + score * 0.15


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        basket_x -= basket_speed

    if keys[pygame.K_RIGHT]:
        basket_x += basket_speed

    basket_x = max(
        0,
        min(WIDTH - basket_width, basket_x)
    )

    star_y += star_speed

    basket_rect = pygame.Rect(
        basket_x,
        basket_y,
        basket_width,
        basket_height
    )

    star_rect = pygame.Rect(
        star_x,
        star_y,
        star_size,
        star_size
    )

    if basket_rect.colliderect(star_rect):
        score += 1
        reset_star()

    if star_y > HEIGHT:
        lives -= 1
        reset_star()

    if lives <= 0:

        screen.fill(BLACK)

        game_over = big_font.render(
            "GAME OVER",
            True,
            RED
        )

        final_score = font.render(
            f"Final Score: {score}",
            True,
            WHITE
        )

        restart = font.render(
            "Press R to Restart or Q to Quit",
            True,
            WHITE
        )

        screen.blit(
            game_over,
            (WIDTH // 2 - game_over.get_width() // 2, 180)
        )

        screen.blit(
            final_score,
            (WIDTH // 2 - final_score.get_width() // 2, 280)
        )

        screen.blit(
            restart,
            (WIDTH // 2 - restart.get_width() // 2, 350)
        )

        pygame.display.update()

        waiting = True

        while waiting:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:
                        score = 0
                        lives = 3
                        reset_star()
                        waiting = False

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

        continue

    screen.fill(BLACK)

    pygame.draw.rect(
        screen,
        BLUE,
        (basket_x, basket_y, basket_width, basket_height)
    )

    pygame.draw.circle(
        screen,
        YELLOW,
        (
            star_x + star_size // 2,
            star_y + star_size // 2
        ),
        star_size // 2
    )

    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    lives_text = font.render(
        f"Lives: {lives}",
        True,
        WHITE
    )

    screen.blit(score_text, (20, 20))
    screen.blit(
        lives_text,
        (WIDTH - 120, 20)
    )

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
