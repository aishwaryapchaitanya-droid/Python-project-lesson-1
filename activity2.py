import pygame

pygame.init()

#screen dimentions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

#Create Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Penguin with shapes")

#Colors
SKY_BLUE = (135, 206, 235)
WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (200,  230,  255)


clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Background
    screen.fill(SKY_BLUE)

    #Snow ground
    pygame.draw.rect(screen, WHITE, (0,380,500,120))

    #Ice block
    pygame.draw.rect(screen, LIGHT_BLUE(50,330,100,50))
    pygame.draw.rect(screen, LIGHT_BLUE(350,320,120,60))

    #Penguin Body
    pygame.draw.ellipse(screen, BLACK(180,150,140,200))

    #penguin tummy
    pygame.draw.ellipse(screen, WHITE(205,190,90,130))    

    #Penguin head
    pygame.draw.circle(screen, BLACK(250,130),60)

    #Eyes
    pygame.draw.circle(screen, WHITE(230,115),10)
    pygame.draw.circle(screen, WHITE(270,155),10)

    pygame.draw.circle(screen, BLACK(230,155),4)
    pygame.draw.circle(screen, BLACK(270,155),4)

    #Beak
    pygame.draw.polygon(screen, ORANGE,
                        [(250, 130), (235, 145), (265, 145)])

    # Feet

    pygame.draw.ellipse(screen, ORANGE, (205, 335, 35, 15))
    pygame.draw.ellipse(screen, ORANGE, (260, 335, 35, 15))

    # Wings
    pygame.draw.ellipse(screen, BLACK, (145, 190, 45, 110))
    pygame.draw.ellipse(screen, BLACK, (310, 190, 45, 110))

    # Text
    font = pygame.font.Font(None, 40)
    text = font.render("Hello World!", True, BLACK)
    screen.blit(text, (170, 430))

    pygame.display.update()
    clock.tick(30)

pygame.quit()