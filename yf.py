import pygame
import random

pygame.init()

# Oyun alanı boyutları
WIDTH, HEIGHT = 800, 600

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Ekran oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Protect the Castle")

# Tank oluştur
tank = pygame.image.load("tank.png")
tank_rect = tank.get_rect()
tank_rect.center = (WIDTH // 2, HEIGHT - 50)

# Kale oluştur
castle_health = 100
font = pygame.font.Font(None, 36)

# Arkadaki çizgi
line_rect = pygame.Rect(0, HEIGHT - 40, WIDTH, 2)

# Düşmanlar listesi
enemies = []

# Mermiler listesi
bullets = []

# Zamanlayıcılar
enemy_spawn_timer = pygame.time.get_ticks()
last_shot_time = 0
bullet_speed = 5
player_speed = 5
enemies_killed = 0
current_level = 1

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if pygame.time.get_ticks() - last_shot_time >= 500:
                bullet = pygame.Rect(tank_rect.centerx - 2, tank_rect.top, 4, 10)
                bullets.append(bullet)
                last_shot_time = pygame.time.get_ticks()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tank_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        tank_rect.x += player_speed

    current_time = pygame.time.get_ticks()
    if current_time - enemy_spawn_timer >= 1000:
        enemy = pygame.Rect(random.randint(0, WIDTH - 50), 0, 50, 50)
        enemies.append(enemy)
        enemy_spawn_timer = current_time

    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, line_rect)

    for enemy in enemies:
        enemy.y += 2 + current_level
        pygame.draw.rect(screen, RED, enemy)

        if enemy.colliderect(line_rect):
            castle_health -= 10
            enemies.remove(enemy)

        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    for bullet in bullets:
        bullet.y -= bullet_speed
        pygame.draw.rect(screen, GREEN, bullet)

        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                enemies_killed += 1

        if bullet.y < 0:
            bullets.remove(bullet)

    if enemies_killed >= 10:
        enemies_killed = 0
        current_level += 1
        castle_health = 100
        enemy_spawn_timer = current_time
        player_speed -= 1

    screen.blit(tank, tank_rect)

    castle_health_text = font.render(f"Castle Health: {castle_health}", True, RED)
    castle_health_text_rect = castle_health_text.get_rect(topleft=(10, 10))
    screen.blit(castle_health_text, castle_health_text_rect)

    level_enemies_text = font.render(f"Level: {current_level}   Killed Enemies: {enemies_killed}", True, RED)
    level_enemies_text_rect = level_enemies_text.get_rect(midtop=(WIDTH // 2, 10))
    screen.blit(level_enemies_text, level_enemies_text_rect)

    pygame.display.flip()

    if castle_health <= 0:
        running = False

    pygame.time.delay(10)

pygame.quit()
