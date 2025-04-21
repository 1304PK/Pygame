import pygame
import time

pygame.init()

width, height = 1200, 900
screen = pygame.display.set_mode((width, height))

ballx = width/2
bally = height/2
paddlevel = 13
velx = 10
vely = 10
run = False
font = pygame.font.SysFont('Arial', 30)
score = 0

winStatement = pygame.transform.scale(pygame.image.load('brick_breakers/Assets/win.png'), (462, 264))
winStatement_rect = winStatement.get_rect(topleft = (width/2 - 231, 305))


# rect = pygame.Rect(0, 0, 118, 30) rectangle
brick = pygame.transform.scale(pygame.image.load("brick_breakers/Assets/brick.jpg"), (118, 40))
rects = []
for row in range(2, 5):
    for column in range(0, width, 120):
        # rect = pygame.Rect(column, 30*row, 118, 28)
        rect = brick.get_rect(topleft = (column, 42*row))
        rects.append(rect)

paddle_img = pygame.image.load("brick_breakers/Assets/paddle.jpg")
paddle = paddle_img.get_rect(topleft = (0, height - 12))
# paddle = pygame.Rect(0, height-20, 120, 20)
ball = pygame.Rect(width/2-10, height/2-10, 20, 20)

def updateScore():
    with open("brick_breakers/score.txt", "r") as file:
        max_score = file.read()
        if score > int(max_score):
            with open("brick_breakers/score.txt", "w") as file:
                file.write(str(score))


def collision():
    global velx, vely, rects, score
    
    if paddle.colliderect(ball) or ball.y < 62 or ball.y > height - 22:
        vely *= -1
    elif ball.x < 2 or ball.x > width-22:
        velx *= -1

    for rect in rects:
        if ball.colliderect(rect):
            if velx > 0 and ball.bottom < rect.bottom:
                velx *= -1
            elif velx < 0 and ball.bottom < rect.bottom:
                velx *= -1
            vely *= -1
            score += 1
            rects.remove(rect)
        

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and paddle.x >= 3:
        paddle.x -= paddlevel
    elif keys[pygame.K_d] and paddle.x <= width-122:
        paddle.x += paddlevel

    if run:
        ball.x += velx
        ball.y += vely
        collision()

    screen.fill((37, 32, 41))
    for rect in rects:
        # pygame.draw.rect(screen, (255, 255, 255), rect)
        screen.blit(brick, rect)
    # pygame.draw.rect(screen, (255, 255, 255), paddle)
    screen.blit(paddle_img, paddle)
    pygame.draw.circle(screen, (255, 255, 255), ball.center, 10)
    pygame.draw.line(screen, (255, 255, 255), (0, 60), (width, 60))
    screen.blit(score_text, (0, 12))
    if len(rects) == 0:
        screen.blit(winStatement, winStatement_rect)
        velx, vely = 0, 0
        updateScore()
    
    # pygame.draw.rect(screen, (255, 0, 0), ball, 1)
    pygame.display.flip()

pygame.quit()