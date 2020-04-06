import sys,pygame
pygame.init()

size = width,height = 1000, 700
speed = [2,2]
black = 60,190,170

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    ballrect = ballrect.move(speed)
    if ballrect.left< 0 or ballrect.right > width:
       while 1:
            speed[0] = -speed[0]    
            pygame.time.delay(16)
            pygame.display.flip()
    if ballrect.top <0 or ballrect.bottom>height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball,ballrect)
    pygame.display.flip()
    
