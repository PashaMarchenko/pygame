import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))

pygame.display.set_caption('CyberPunk 2k19')

walkRight = [pygame.image.load('static/right_1.png'), pygame.image.load('static/right_2.png'), pygame.image.load('static/right_3.png'), pygame.image.load('static/right_4.png'), pygame.image.load('static/right_5.png'), pygame.image.load('static/right_6.png')]

walkLeft = [pygame.image.load('static/left_1.png'), pygame.image.load('static/left_2.png'), pygame.image.load('static/left_3.png'), pygame.image.load('static/left_4.png'), pygame.image.load('static/left_5.png'), pygame.image.load('static/left_6.png')]

bg = pygame.image.load('static/bg1.png')

playerStand = pygame.image.load('static/idle.png')

clock = pygame.time.Clock()

x = 15
y = 435
widht = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

class bullet():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



def drawW():
    global animCount
    win.blit(bg,(0,0))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y) )
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y) )
        animCount += 1
    else:
        win.blit(playerStand, (x,y))

    pygame.display.update()

run = True

bullets = []

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bul in bullets:
        if bul.x < 500 and bul.x > 0:
            bul.x += bul.vel
        else:
            bul.pop(bullets.index(bul))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5 :
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 800 - widht - 5 :
        x += speed
        right = True
        left = False
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10
    drawW()

pygame.quit()