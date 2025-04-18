import pygame

pygame.init()

width, height = 1200, 900
screen = pygame.display.set_mode((width, height))

# rect = pygame.Rect(0, 0, 118, 30)
rects = []
for row in range(0, 8):
    for column in range(0, width, 120):
        rect = pygame.Rect(column, 30*row, 118, 28)
        rects.append(rect)
    
paddle = pygame.Rect(0, height-20, 120, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # pygame.draw.rect(screen, (255, 255, 255), rect)
    for rect in rects:
        pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.circle(screen, (255, 255, 255), (width/2, height/2), 10)
    pygame.display.update()

pygame.quit()