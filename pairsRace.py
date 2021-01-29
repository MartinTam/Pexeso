import pygame
import os

pygame.init()


FPS = 60

WHITE = (255, 255, 255)

IMAGE = {
            'background' : pygame.image.load(os.path.join('images', 'background.jpeg')),
            
            'img1' : pygame.image.load(os.path.join('images', '01.jpeg')),
            'img2' : pygame.image.load(os.path.join('images', '02.jpeg')),
            'img3' : pygame.image.load(os.path.join('images', '03.jpeg')),

            'header' : pygame.image.load(os.path.join('images', 'header.png'))
        }



LOAD_BUTTON_ORG =   {
                        'play' : pygame.image.load(os.path.join('images', 'play.png')),
                        'next' : pygame.image.load(os.path.join('images', 'next.png')),
                        'success' : pygame.image.load(os.path.join('images', 'success.png')),
                        'fail' : pygame.image.load(os.path.join('images', 'fail.png')),
                        'home' : pygame.image.load(os.path.join('images', 'home.png'))
                    }



SIZE =  {
            'window' : (1000, 700),
            'play_button' : (100, 110),
            'next_button' : (200, 200),
            'success_icon' : (80,80),
            'fail_icon' : (80,80),
            'home_button' : (100,100)

        }



BUTTON =    {
                'play' : pygame.transform.scale( LOAD_BUTTON_ORG['play'], SIZE['play_button'] ),
                'next' : pygame.transform.scale( LOAD_BUTTON_ORG['next'], SIZE['next_button'] ),
                'success' : pygame.transform.scale( LOAD_BUTTON_ORG['success'], SIZE['success_icon'] ),
                'fail' : pygame.transform.scale( LOAD_BUTTON_ORG['fail'], SIZE['fail_icon'] ),
                'home' : pygame.transform.scale( LOAD_BUTTON_ORG['home'], SIZE['home_button'] )
            }



POSITION =  {   
                'background' : (0,0),
                'text_play' : (430,230),
                'play_button' : (445,295),
                'header' : (301,50),
                'text_time' : (15,15),
                'next_button' : (775,525),
                'success_icon' : (460,23),
                'fail_icon' : (460,23),

                'img1' : (270, 135),
                'img2' : (520, 135),
                'img3' : (270, 308),
                'img4' : (520, 308),
                'img5' : (270, 481),
                'img6' : (520, 481),

                'text_result' : (325,230),
                'home_button' : (445,395)
            }

FONT = pygame.font.SysFont('comicsans', 70)

TEXT =  {
            'play' : FONT.render('PLAY', True, WHITE),
            'time' : FONT.render('00:00:00', True, WHITE),
            'result' : FONT.render('Time: 00:00:00', True, WHITE)
        }






WIN = pygame.display.set_mode(SIZE['window'])
pygame.display.set_caption('Pairs Race')


def draw():
    
    WIN.fill(WHITE)
    WIN.blit(IMAGE['background'], POSITION['background'])
    
    WIN.blit(TEXT['play'], POSITION['text_play'])
    WIN.blit(BUTTON['play'], POSITION['play_button'])
    
    WIN.blit(IMAGE['header'], POSITION['header'])
    
    
    WIN.blit(TEXT['time'], POSITION['text_time'])

    
    WIN.blit(BUTTON['next'], POSITION['next_button'])
    
    WIN.blit(BUTTON['success'], POSITION['success_icon'])
    WIN.blit(BUTTON['fail'], POSITION['fail_icon'])

    WIN.blit(IMAGE['img1'], POSITION['img1'])
    WIN.blit(IMAGE['img2'], POSITION['img2'])

    WIN.blit(IMAGE['img2'], POSITION['img3'])
    WIN.blit(IMAGE['img3'], POSITION['img4'])

    WIN.blit(IMAGE['img3'], POSITION['img5'])
    WIN.blit(IMAGE['img1'], POSITION['img6'])
    
    WIN.blit(TEXT['result'], POSITION['text_result'])
    WIN.blit(BUTTON['home'], POSITION['home_button'])
    
    pygame.display.update()

def main():

    run = True
    clock = pygame.time.Clock()

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

        draw()

    pygame.quit()

main()