import pythongames
pythongames.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pythongames.display.set_mode((WIDTH, HEIGHT))
pythongames.display.set_caption("1st game")

BLUE = (115, 147, 179)
BLACK = (0, 0, 0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 45
YELLOW_SPACESHIP_IMAGE = pythongames.image.load(
    'C:\\Users\\ARUN\\PycharmProjects\\pythonProject\\Assets\\spaceship_yellow.png')
YELLOW_SPACESHIP = pythongames.transform.rotate(
    pythongames.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pythongames.image.load('C:\\Users\\ARUN\\PycharmProjects\\pythonProject\\Assets\\spaceship_red.png')
RED_SPACESHIP = pythongames.transform.rotate(
    pythongames.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
SPACE_BACKGROUND =  pythongames.transform.scale(pythongames.image.load('C:\\Users\\ARUN\\PycharmProjects\\pythonProject\\Assets\\space.png'), (WIDTH, HEIGHT))
SPACESHIP_VELOCITY = 3
BODER = pythongames.Rect(WIDTH / 2 - 3, 0, 6, HEIGHT)
MAX_BULLETS = 3
BULLET_VELOCITY = 6
HEALTH_FONT = pythongames.font.SysFont('comicsans', 30)
WINNER_FONT = pythongames.font.SysFont('comicsans', 100)

YELLOW_HIT = pythongames.USEREVENT + 1
RED_HIT = pythongames.USEREVENT + 2


def displayupdate(red, yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    WIN.blit(SPACE_BACKGROUND,(0,0))
    pythongames.draw.rect(WIN, BLACK, BODER)
    red_health_text = HEALTH_FONT.render("RED Health :" + str(red_health),True,WHITE)
    yellow_health_text = HEALTH_FONT.render("YELLOW Health :" + str(yellow_health), True, WHITE)
    WIN.blit(red_health_text,(WIDTH- red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text,(10,10))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    for bullets in red_bullets:
        pythongames.draw.rect(WIN, RED, bullets)
    for bullets in yellow_bullets:
        pythongames.draw.rect(WIN, YELLOW, bullets)




    pythongames.display.update()


def spaceship_movement(key_pressed, yellow, red):
    if key_pressed[pythongames.K_a] and yellow.x - SPACESHIP_VELOCITY > 0:  # LEFT
        yellow.x -= SPACESHIP_VELOCITY
    if key_pressed[pythongames.K_d] and yellow.x + SPACESHIP_VELOCITY < WIDTH / 2 - SPACESHIP_WIDTH:  # RIGHT
        yellow.x += SPACESHIP_VELOCITY
    if key_pressed[pythongames.K_s] and yellow.y + SPACESHIP_VELOCITY < HEIGHT - SPACESHIP_HEIGHT:  # DOWN
        yellow.y += SPACESHIP_VELOCITY
    if key_pressed[pythongames.K_w] and yellow.y - SPACESHIP_VELOCITY > 0:  # UP
        yellow.y -= SPACESHIP_VELOCITY

    if key_pressed[pythongames.K_LEFT] and red.x + SPACESHIP_VELOCITY > WIDTH / 2 + 5:  # LEFT
        red.x -= SPACESHIP_VELOCITY
    if key_pressed[pythongames.K_RIGHT] and red.x - SPACESHIP_VELOCITY < WIDTH - SPACESHIP_WIDTH:  # RIGHT
        red.x += SPACESHIP_VELOCITY
    if key_pressed[pythongames.K_DOWN] and red.y + SPACESHIP_VELOCITY < HEIGHT - SPACESHIP_HEIGHT - 3:  # DOWN
        red.y += SPACESHIP_VELOCITY
    if key_pressed[pythongames.K_UP] and red.y + SPACESHIP_VELOCITY > 7:  # UP
        red.y -= SPACESHIP_VELOCITY

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pythongames.event.post(pythongames.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        elif bullet.x > WIDTH :
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pythongames.event.post(pythongames.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text,True,WHITE)
    WIN.blit(draw_text,(WIDTH/2-draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
    pythongames.display.update()
    pythongames.time.delay(5000)



def main():
    run = True
    yellow = pythongames.Rect(WIDTH // 6, HEIGHT // 2 - 30, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pythongames.Rect(WIDTH // 1.3, 250 - 30, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow_bullets = []
    red_bullets = []
    red_health = 10
    yellow_health = 10
    winner_text = ""

    clock = pythongames.time.Clock()
    while (run):
        clock.tick(FPS)
        for event in pythongames.event.get():
            if event.type == pythongames.QUIT:
                run = False
                pythongames.quit()

            if event.type == pythongames.KEYDOWN:
                if event.key == pythongames.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pythongames.Rect(yellow.x + yellow.width, yellow.y + yellow.height / 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pythongames.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pythongames.Rect(red.x, red.y + red.height / 2 - 2, 10, 5)
                    red_bullets.append(bullet)

            if event.type == RED_HIT:
                red_health-=1

            if event.type == YELLOW_HIT:
                yellow_health-=1

        if red_health<=0:
            winner_text = "YELLOW WINS!!"
        if yellow_health<=0:
            winner_text = "RED WINS"
        if winner_text!="":
            draw_winner(winner_text)
            run = False




        handle_bullets(yellow_bullets,red_bullets,yellow,red)

        key_pressed = pythongames.key.get_pressed()
        spaceship_movement(key_pressed, yellow, red)

        displayupdate(red, yellow,red_bullets,yellow_bullets,red_health,yellow_health)

    main()

if __name__ == '__main__':
    main()
