from pygame import *

win = display.set_mode((1024, 1024))
display.set_caption('Maze')
win.blit(transform.scale(image.load('background.jpg'), (1024,1024)),(0,0))

class packmansprite(sprite.Sprite):
    def __init__(self,picture,x,y):
        sprite.Sprite.__init__(self)

        elf.picture = transform.scale(image.load(picture), (100,100))

        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,packman,wall_up1,wall_up2,wall_up3,wall_side):
        keys = key.get_pressed()

        if keys[K_d]:
            self.rect.x += 20
            self.up = False
            self.right = True
            self.down = False
            self.left = False
            if sprite.collide_rect(packman, wall_up1) or sprite.collide_rect(packman, wall_up2) or sprite.collide_rect(
                    packman, wall_up3) or sprite.collide_rect(packman, wall_side):
                if packman.right:
                    packman.rect.x -= 20

        if keys[K_a]:
            self.rect.x -= 20
            self.up = False
            self.right = False
            self.down = False
            self.left = True
            if sprite.collide_rect(packman, wall_up1) or sprite.collide_rect(packman, wall_up2) or sprite.collide_rect(
                    packman, wall_up3) or sprite.collide_rect(packman, wall_side):
                if packman.left:
                    packman.rect.x += 20

        if keys[K_w]:
            self.rect.y -= 20
            self.up = True
            self.right = False
            self.down = False
            self.left = False
            if sprite.collide_rect(packman, wall_up1) or sprite.collide_rect(packman, wall_up2) or sprite.collide_rect(
                    packman, wall_up3) or sprite.collide_rect(packman, wall_side):
                if packman.up:
                    packman.rect.y += 20

        if keys[K_s]:
            self.rect.y += 20
            self.up = False
            self.right = False
            self.down = True
            self.left = False
            if sprite.collide_rect(packman, wall_up1) or sprite.collide_rect(packman, wall_up2) or sprite.collide_rect(
                    packman, wall_up3) or sprite.collide_rect(packman, wall_side):
                if packman.down:
                    packman.rect.y -= 20

        #self.update()

    def draw(self):
        win.blit(self.picture, (self.rect.x,self.rect.y))
class enemysprite(sprite.Sprite):
    down = ''

    def __init__(self,picture,x,y):
        sprite.Sprite.__init__(self)

        self.picture = transform.scale(image.load(picture), (100,100))

        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,y1,y2):
        if self.rect.y <=y1:
            self.down = True
        elif self.rect.y>=y2:
            self.down = False
        if self.down :
            self.rect.y+=10
        else:
            self.rect.y-=10

        #self.update()

    def draw(self):
        win.blit(self.picture, (self.rect.x,self.rect.y))



class wall(sprite.Sprite):
    def __init__(self,picture, x,y, width,height):
        self.picture = transform.scale(image.load(picture),(width,height))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
    def place(self):
        win.blit(self.picture, (self.rect.x, self.rect.y))
class winning(sprite.Sprite):
    def __init__(self,picture, x,y, width,height):
        self.picture = transform.scale(image.load(picture),(width,height))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
    def place(self):
        win.blit(self.picture, (self.rect.x, self.rect.y))

run = True
x = 0
y = 0
packman = packmansprite('glavg.png',20,20)
wall_up1 = wall('wall_up.png',150,624,100,400)
wall_up2 = wall('wall_up.png',150,0,100,400)
wall_up3 = wall('wall_up.png',624,0,100,500)
wall_side = wall ('wall_side.png',624,700,400,100)
enemy = enemysprite('ghost.png', 500,500)
prize = winning('award.png',900,0,100,100)


def losing(packman):
    win.blit(transform.scale(image.load('lose.png'), (1024, 1024)), (0, 0))
    display.update()
    restart = True
    while restart:
        for events in event.get():
            if events.type == QUIT:
                restart = False
                return (False)
            if events.type == KEYDOWN:
                if events.key == K_r:
                    restart = False
                    packman.rect.x = 0
                    packman.rect.y = 0

def winning(packman):
    win.blit(transform.scale(image.load('win.png'), (1024, 1024)), (0, 0))
    display.update()
    restart = True
    while restart:
        for events in event.get():
            if events.type == QUIT:
                restart = False
                return (False)
            if events.type == KEYDOWN:
                if events.key == K_r:
                    restart = False
                    packman.rect.x = 0
                    packman.rect.y = 0

while run:

    time.delay(50)

    for events in event.get():
        if events.type == KEYDOWN:
            if events.key == K_t:
                run = False
        if events.type == QUIT:
            run = False
    win.blit(transform.scale(image.load('background.jpg'), (1024, 1024)), (0, 0))
    packman.update(packman,wall_up1,wall_up2,wall_up3,wall_side)
    packman.draw()



    wall_up1.place()
    wall_up2.place()
    wall_side.place()
    wall_up3.place()
    prize.place()
    enemy.update(400,700)
    enemy.draw()
    display.update()

    '''if  sprite.collide_rect(packman,wall_up1) or sprite.collide_rect(packman,wall_up2) or sprite.collide_rect(packman,wall_up3) or sprite.collide_rect(packman,wall_side):
        if packman.left:
            packman.rect.x += 20
        if packman.right:
            packman.rect.x -=20
        if packman.up:
            packman.rect.y +=20
        if packman.down:
            packman.rect.y -=20'''

    if sprite.collide_rect(packman,enemy):

        if losing(packman) == False:
            break
    if sprite.collide_rect(packman,prize):
        if winning(packman) == False:
            break




    display.update()



time.delay(1)