import pygame

pygame.init()

width, height = 1200, 900
screen = pygame.display.set_mode((width, height))

ballx = width/2
bally = height/2
paddlevel = 10
vel = 10
run = False

# rect = pygame.Rect(0, 0, 118, 30)
rects = []
for row in range(0, 8):
    for column in range(0, width, 120):
        rect = pygame.Rect(column, 30*row, 118, 28)
        rects.append(rect)

    
paddle = pygame.Rect(0, height-20, 120, 20)



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
        ballx += vel
        bally += vel

    screen.fill((0, 0, 0))
    for rect in rects:
        pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.circle(screen, (255, 255, 255), (ballx, bally), 10)
    pygame.display.flip()

pygame.quit()