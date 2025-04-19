import pygame

pygame.init()

width, height = 1200, 900
screen = pygame.display.set_mode((width, height))

ballx = width/2
bally = height/2
paddlevel = 10
velx = 5
vely = 5
run = False

# rect = pygame.Rect(0, 0, 118, 30)
rects = []
for row in range(0, 3):
    for column in range(0, width, 120):
        rect = pygame.Rect(column, 30*row, 118, 28)
        rects.append(rect)

    
paddle = pygame.Rect(0, height-20, 120, 20)
ball = pygame.Rect(width/2-10, height/2-10, 20, 20)

def collision():
    global velx, vely, rects
    if paddle.colliderect(ball) or ball.y < 2 or ball.y > height - 22:
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
            rects.remove(rect)
        
    if len(rects) == 0:
        print('you win')

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and paddle.x >= 0:
        paddle.x -= paddlevel
    elif keys[pygame.K_d] and paddle.x <= width-120:
        paddle.x += paddlevel

    if run:
        ball.x += velx
        ball.y += vely
        collision()

    screen.fill((0, 0, 0))
    for rect in rects:
        pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.circle(screen, (255, 255, 255), ball.center, 10)
    # pygame.draw.rect(screen, (255, 0, 0), ball, 1)
    pygame.display.flip()

pygame.quit()