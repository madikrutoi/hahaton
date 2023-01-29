from Pygame import*

clock = time.clock()
FPS = 65
win_w = 1200
win_h = 600
window = display.set_mode(win_w,win_h)
bg = transform.scale(image.load('background.jpg'),(win_w,win_h))
class Hero(Sprite.Sprite):
    def __init__(self,player_image, x , y , w , h , speed):
        sprite.sprite.__init(self)
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.right = False
        self.count = 0
        self.right = False
        self.count = 0
class Player(Hero):
    def update(self)
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.left = True
            self.right = False
        elif keys[K_RIGHT] and self.rect,x < win_w - 80:
            self.rect.x += self.speed
            self.left = False
            self.right = True
        else:
            self.left = False
            self.right = False
            self.count = 0
    def animation(self):
        if self.count = 1 >= 





hero = Hero('hero.png',5,440,85,168,10)








run = True
while run:
    window.blit(bg, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    hero.reset()

    display.update()
