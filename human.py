import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Car Test")
clock = pygame.time.Clock()

# Starting position
x = 500
y = 350

angle = 0
speed = 0

ACCEL = 0.2
MAX_SPEED = 8
FRICTION = 0.05
TURN_SPEED = 3

# Make the car once instead of every frame
car = pygame.Surface((60, 30))
car.fill((220, 220, 220))

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Gas and reverse
    if keys[pygame.K_w]:
        speed += ACCEL

    if keys[pygame.K_s]:
        speed -= ACCEL

    # Keep speed within limits
    if speed > MAX_SPEED:
        speed = MAX_SPEED
    elif speed < -MAX_SPEED / 2:
        speed = -MAX_SPEED / 2

    # Turn only if moving
    if abs(speed) > 0.1:
        if keys[pygame.K_a]:
            angle += TURN_SPEED

        if keys[pygame.K_d]:
            angle -= TURN_SPEED

    # Friction
    if speed > 0:
        speed -= FRICTION
        if speed < 0:
            speed = 0
    elif speed < 0:
        speed += FRICTION
        if speed > 0:
            speed = 0

    # Move in the direction we're facing
    rad = math.radians(angle)
    x += math.cos(rad) * speed
    y -= math.sin(rad) * speed

    # Draw
    screen.fill((30, 30, 30))

    rotated_car = pygame.transform.rotate(car, angle)
    rect = rotated_car.get_rect(center=(x, y))

    screen.blit(rotated_car, rect)
    pygame.display.flip()

pygame.quit()