import pygame
import time

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))

# ==================  VARIABLES  ================== #
ballx = width/2
bally = height/2
paddlevel = 13
velx = 10
vely = -4
run = False
font = pygame.font.SysFont('Clash', 30)
score = 0
isPlaying = False

winStatement = pygame.transform.scale(pygame.image.load('brick_breakers/Assets/win.png'), (462, 264))
winStatement_rect = winStatement.get_rect(topleft = (width/2 - 231, 305))
clock = pygame.time.Clock()
running = True


# ================== IMAGES ================== #
brick = pygame.transform.scale(pygame.image.load("brick_breakers/Assets/brick.png"), (70, 35))
rects = []
for row in range(2, 6):
    for column in range(0, width, 70):
        # rect = pygame.Rect(column, 30*row, 118, 28)
        rect = brick.get_rect(topleft = (column, 35*row))
        rects.append(rect)

paddle_img = pygame.image.load("brick_breakers/Assets/paddle.jpg")
paddle = paddle_img.get_rect(topleft = (width/2 - 60, height - 12))
# paddle = pygame.Rect(0, height-20, 120, 20)
ball = pygame.Rect(width/2-10, height/2-10, 20, 20)
introScreen = pygame.transform.scale(pygame.image.load('brick_breakers/Assets/intro_screen.png'), (width, height))
lives = pygame.Rect(500, 15, 20, 20)


# ================== FUNCTIONS ================== #
def updateScore():
    with open("brick_breakers/score.txt", "r") as file:
        max_score = file.read()
        if score > int(max_score):
            with open("brick_breakers/score.txt", "w") as file:
                file.write(str(score))


def collision():
    global velx, vely, rects, score
    if paddle.colliderect(ball) or ball.y < 62 or ball.bottom >= height:
        vely *= -1
    if ball.left == 0 or ball.right == width:
        velx *= -1

    for rect in rects:
        if ball.colliderect(rect):
            if ball.left - rect.left >= -10 and ball.right-rect.right<=10:
                vely *= -1
            if abs(ball.top-rect.top)<10 or abs(ball.bottom - rect.bottom)<10:
                velx *= -1
            score += 1
            rects.remove(rect)
        

# ==================== GAME LOOP ==================== #

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                isPlaying = True
        

    

    if isPlaying:
        ball.x += velx
        ball.y += vely
        collision()

        score_text = font.render(f'{score}', True, (255, 255, 255))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and paddle.x >= 3:
            paddle.x -= paddlevel
        elif keys[pygame.K_d] and paddle.x <= width-122:
            paddle.x += paddlevel

        screen.fill((37, 32, 41))
        for rect in rects:
            screen.blit(brick, rect)
        screen.blit(paddle_img, paddle)
        pygame.draw.circle(screen, (255, 255, 255), ball.center, 10)
        pygame.draw.circle(screen, (255, 255, 255), (500, 30), 10, 1)
        pygame.draw.circle(screen, (255, 255, 255), (525, 30), 10)
        pygame.draw.circle(screen, (255, 255, 255), (550, 30), 10)
        pygame.draw.line(screen, (255, 255, 255), (0, 60), (width, 60))
        screen.blit(score_text, (width/2-score_text.get_width(), 12))
        # pygame.draw.circle(screen, (255, 255, 255), ball.centre, 10)
        
        if len(rects) == 0:
            screen.blit(winStatement, winStatement_rect)
            velx, vely = 0, 0
            updateScore()

    else:
        screen.blit(introScreen, (0, 0))
        
        # pygame.draw.rect(screen, (255, 0, 0), ball, 1)
    pygame.display.flip()

pygame.quit()