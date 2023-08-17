import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Düşen Bloklar Oyunu")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_width = 60
player_height = 20
player_color = RED
player_position = [WIDTH // 2, HEIGHT - player_height * 2]
player_velocity = 8

block_width = 50
block_height = 50
block_color = BLUE
blocks = []

clock = pygame.time.Clock()

def draw_player():
    pygame.draw.rect(screen, player_color, pygame.Rect(player_position[0], player_position[1], player_width, player_height))

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, block_color, block)

def check_collision(player_rect, blocks):
    for block in blocks:
        if player_rect.colliderect(block):
            return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_position[0] > 0:
        player_position[0] -= player_velocity
    if keys[pygame.K_RIGHT] and player_position[0] < WIDTH - player_width:
        player_position[0] += player_velocity

    if random.randint(0, 100) < 10:
        block_x = random.randint(0, WIDTH - block_width)
        block_y = -block_height
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

    screen.fill(WHITE)

    draw_player()
    draw_blocks()

    player_rect = pygame.Rect(player_position[0], player_position[1], player_width, player_height)
    if check_collision(player_rect, blocks):
        pygame.quit()
        sys.exit()

    for block in blocks:
        block.y += 5
        if block.y > HEIGHT:
            blocks.remove(block)

    pygame.display.flip()

    clock.tick(60)
