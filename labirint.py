from pygame import*
window = display.set_mode((700,500))
display.set_caption('First Game')
run = True


class GameSprite(sprite.Sprite):
    def _init_(self ,pu,w,h,x,y):
        super()._init_()
        self.image=transform.scale(image.load(background.jpg),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x.self.rect.y))
class Player(GameSprite):
    def _init(self, player_image, player_x,player_y, size_x, size_y, player_x):
        GameSprite._init_(self,player_image , player_x, player_y,size_x,size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
       if packman.rect.x <= win_width-80 and packman.rect.x >= 0 and packman.x_speed:
        self.rect.x += self.x_speed
    platforms_touched = sprite.spritecollide(self, barriers, false)
    if self.x_speed > 0:
        for p in platforms_touched:
            self.rect.right =min(self.rect.left, p.rect.right)
    elif self.x_speed < 0:
        for p in platforms_touched:
            self.rect.left = max(self.rect.left, p.rect.right)
    if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.player_y_speed <=0:
     self.rect.y += self.y_speed
     platforms_touched = sprite.spritecollide(self, parriers, False)
     if self.y_speed > 0:
         for p in platforms_touched:
             self.rect.bottom = min(self.rect.bottom, p.rect.top)
     elif self.y_speed < 0:
        for p in platforms_touched:
            self.rect.top = max(self.rect.top, p.rect.bottom)

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEVDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        elif e.type == KEYUP:
            if e_key == K_LEFT:
                packman.x_speed = 0
        if e.type == QUIT:
            run = False
        display.update()
    
class Enemy(GameSprite):
    side = "left"
    def _init_(self, player_image,player_x,player_y, size_x, size_y, player_spead):
        GameSprite._init_(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    def update(self):
        if self.rect_x <= 420:
            self.side = "right"
        if self.rect_x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -+ self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def _init_(self, player_image, player_x, player_y, size_y, player_speed):
        GameSprite._init_(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_spead
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
             self.kill()

win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)

barriers = sprite.Group()

bullets = sprite.Group()

monsters = sprite.Group()

run = True
while run:
    window.blit(bg, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    hero.reset()

    display.update()