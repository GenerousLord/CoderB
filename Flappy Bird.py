import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
#mixer.music.load('background.wav')
#mixer.music.play(-1)
sucuk = pygame.image.load('N_b6N3.png')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

bird_position = [100, HEIGHT // 2]
bird_velocity = 0
gravity = 0.5
jump_strength = -10

pipe_width = 70
pipe_gap = 200
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def draw_bird():
    pygame.draw.circle(screen, BLUE, bird_position, 20)

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if pipe.colliderect(pygame.Rect(bird_position[0] - 20, bird_position[1] - 20, 40, 40)):
            return True
    if bird_position[1] <= 0 or bird_position[1] >= HEIGHT:
        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength
        if event.type == SPAWNPIPE:
            pipe_height = random.randint(100, 400)
            top_pipe = pygame.Rect(WIDTH, 0, pipe_width, pipe_height)
            bottom_pipe = pygame.Rect(WIDTH, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_height - pipe_gap)
            pipe_list.append(top_pipe)
            pipe_list.append(bottom_pipe)

    bird_velocity += gravity
    bird_position[1] += bird_velocity

    screen.fill(WHITE)

    draw_pipes(pipe_list)
    draw_bird()

    if check_collision(pipe_list):
        pygame.quit()
        sys.exit()

    for pipe in pipe_list:
        pipe.x -= 5
        if pipe.x + pipe_width < 0:
            pipe_list.remove(pipe)
            score += 1

    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(30)

