import pygame
import math


import resource
import sys



# soft, hard = resource.getrlimit(resource.RLIMIT_AS)
# print("soft =", soft)
# print("hard =", hard)
# exit()








pygame.init()
screen = pygame.display.set_mode((800,480))
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
pygame.display.set_caption("Sheikah Slate")
screenWidth, screenHeight = screen.get_size()

path="./Assets/"
pathtoimg="Assets/pictures"
running= True
FPS=20
elapsed=0



clock = pygame.time.Clock()
#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES
BG = pygame.image.load(path+"BG.JPG")
BG = pygame.transform.scale(BG, (screenWidth,screenHeight))
Glow = pygame.image.load(path+"Glow.png")
Glow = pygame.transform.scale(Glow, (screenWidth,screenHeight))
Glow.set_alpha(100)
Glow2V = pygame.image.load(path+"Glow copy.png")
Glow2V = pygame.transform.rotate(Glow2V,90.0)
Glow2V = pygame.transform.scale(Glow2V, (screenWidth,screenHeight))
Glow2H = pygame.image.load(path+"Glow copy.png")
Glow2H = pygame.transform.scale(Glow2H, (screenWidth,screenHeight))


InitIconScale = 1.5
InitIconM = pygame.image.load(path+"IconImg.png")
InitIconM = pygame.transform.scale(InitIconM, (screenHeight/InitIconScale,screenHeight/InitIconScale))
InitIconR = pygame.image.load(path+"IconImgRight.png")
InitIconR = pygame.transform.scale(InitIconR, (screenHeight/InitIconScale,screenHeight/InitIconScale))
InitIconL = pygame.image.load(path+"IconImgLeft.png")
InitIconL = pygame.transform.scale(InitIconL, (screenHeight/InitIconScale,screenHeight/InitIconScale))
#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES

while running:
    screen.fill((0,0,0))
    elapsed+=1/FPS
    deltatime=clock.get_time()
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
    # screen.blit(CompendiumTitle,(screenWidth/2-CompendiumTitle.get_size()[0]/2+modifierPage(2),screenHeight/90))
    #####################!#####################!#####################!
    delay = .3
    endSplitAnim = .5
    endFadeAnim = .7
    deltapos=math.sin((math.pi/2)*min((elapsed-delay)/endSplitAnim,1))
    splitanimspeed=60
    if elapsed < delay:
        screen.blit(InitIconM,(screenWidth/2-InitIconM.get_size()[0]/2,screenHeight/2-InitIconM.get_size()[1]/2))
        screen.blit(InitIconL,(screenWidth/2-InitIconL.get_size()[0]/2,screenHeight/2-InitIconL.get_size()[1]/2))
        screen.blit(InitIconR,(screenWidth/2-InitIconR.get_size()[0]/2,screenHeight/2-InitIconR.get_size()[1]/2))
    elif elapsed < endSplitAnim+delay:
        screen.blit(InitIconM,(screenWidth/2-InitIconM.get_size()[0]/2,screenHeight/2-InitIconM.get_size()[1]/2))
        screen.blit(InitIconL,(screenWidth/2-InitIconL.get_size()[0]/2-deltapos*splitanimspeed,screenHeight/2-InitIconL.get_size()[1]/2))
        screen.blit(InitIconR,(screenWidth/2-InitIconR.get_size()[0]/2+deltapos*splitanimspeed,screenHeight/2-InitIconR.get_size()[1]/2))
        pass
    elif elapsed < endSplitAnim+endFadeAnim+delay:
        InitIconM.set_alpha(255-255*(elapsed-endSplitAnim)/endFadeAnim)
        screen.blit(InitIconM,(screenWidth/2-InitIconM.get_size()[0]/2,screenHeight/2-InitIconM.get_size()[1]/2))
        InitIconL.set_alpha(255-255*(elapsed-endSplitAnim)/endFadeAnim)
        screen.blit(InitIconL,(screenWidth/2-InitIconL.get_size()[0]/2-splitanimspeed,screenHeight/2-InitIconL.get_size()[1]/2))
        InitIconR.set_alpha(255-255*(elapsed-endSplitAnim)/endFadeAnim)
        screen.blit(InitIconR,(screenWidth/2-InitIconR.get_size()[0]/2+splitanimspeed,screenHeight/2-InitIconR.get_size()[1]/2))
    # screen.blit(Glow,(0,0))
    pygame.display.flip()
    clock.tick(FPS)


