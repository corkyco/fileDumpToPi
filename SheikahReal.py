import pygame
import math
import threading
import os
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((300,300))
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
pygame.display.set_caption("Sheikah Slate")
screenWidth, screenHeight = screen.get_size()

path="./Assets/"
pathtoimg="Assets/pictures"


#!MUSIC
pygame.mixer.init()
def playSound(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(loops=0)
#!MUSIC
playSound(path+"Map/OpenMap.flac")





clock = pygame.time.Clock()
#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES
BG = pygame.image.load(path+"BG.JPG")
BG = pygame.transform.scale(BG, (screenWidth,screenHeight))
Glow = pygame.image.load(path+"Glow.png")
Glow = pygame.transform.scale(Glow, (screenWidth,screenHeight))
Glow.set_alpha(100)

ShrineIconScale = 8
ShrineIcon = pygame.image.load(path+"BG.png")
ShrineIcon = pygame.transform.scale(ShrineIcon, (screenHeight/ShrineIconScale,screenHeight/ShrineIconScale))
ShrineIcon2 = pygame.image.load(path+"ShrineIconImg.png")
ShrineIcon2 = pygame.transform.scale(ShrineIcon2, (screenHeight/ShrineIconScale*200/87,screenHeight/ShrineIconScale))

DateTimeScale = 4
DateTime = pygame.image.load(path+"DateTime.png")
DateTime = pygame.transform.scale(DateTime, (screenHeight/DateTimeScale*259/150,screenHeight/DateTimeScale))



RefreshScale = .1
Refresh = pygame.image.load(path+"BG.png")
Refresh = pygame.transform.scale(Refresh, (screenHeight*RefreshScale,screenHeight*RefreshScale))


RuneScale = 8
Rune1 = pygame.image.load(path+"BG.png")
Rune1 = pygame.transform.scale(Rune1, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune2 = pygame.image.load(path+"BG.png")
Rune2 = pygame.transform.scale(Rune2, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune3 = pygame.image.load(path+"BG.png")
Rune3 = pygame.transform.scale(Rune3, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune4 = pygame.image.load(path+"BG.png")
Rune4 = pygame.transform.scale(Rune4, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune5 = pygame.image.load(path+"BG.png")
Rune5 = pygame.transform.scale(Rune5, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune6 = pygame.image.load(path+"BG.png")
Rune6 = pygame.transform.scale(Rune6, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune7 = pygame.image.load(path+"BG.png")
Rune7 = pygame.transform.scale(Rune7, (screenHeight/RuneScale,screenHeight/RuneScale))


InitIconScale = 4
InitIcon = pygame.image.load(path+"IconImg.png")
InitIcon = pygame.transform.scale(InitIcon, (screenHeight/InitIconScale,screenHeight/InitIconScale))
#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES
#!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT
font = pygame.font.SysFont("manapua", 80)
RunesTitle = font.render("Runes", True, (255,255,255))
MapTitle = font.render("Map", True, (255,255,255))
AlbumTitle = font.render("Album", True, (255,255,255))
CompendiumTitle = font.render("Compendium", True, (255,255,255))

# print(pygame.font.get_fonts())
# exit()
#!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT


FPS = 60
compendium={
    "Barbary Macaque":pathtoimg+"ThinkingMonkey copy 3.webp",
    "Happy Barbary Macaque":pathtoimg+"HappyMonkey copy.webp",
    # "Name":"filepath"  
    }
images=[None]*12
def getImageLength():
    return len(os.listdir("Assets/pictures"))

def loadImages(page,perpage,invis=False):
    global images,pathtoimg
    num=0
    images=[None]*perpage
    for filename in os.listdir(pathtoimg):
        num+=1
        curpage=(num-1)//perpage
        # print(curpage,page)
        if curpage!=page:
            continue
        images[(num-1)%perpage] = pygame.image.load(os.path.join(pathtoimg,filename))
        # images[num%perpage-1] = pygame.transform.scale(images[num%perpage-1], (screenWidth/5,screenHeight/4))
        if invis:
            images[(num-1)%perpage].set_alpha(0)
    # print(images)







currentScreen=0
currentScreenGoal=0
currentImgPage = 0
isMouseDown=False
mouseDownLocation=(0,0)

isViewImage=False
viewedImage=0
def switchScreenTo(delta):
    global currentImgPage,isViewImage,viewedImage
    screenNum=currentScreen+delta
    imgPage=currentImgPage+delta
    print("delta:",delta,"\tviewedImage:",viewedImage)
    print(images)
    if screenNum>=-1 and screenNum<=2:

        if currentScreen==1:




            if isViewImage:
                if viewedImage+delta<0:
                    if currentImgPage>0:
                        currentImgPage=imgPage
                        loadImages(imgPage,12)
                        viewedImage=11
                        playSound(path+"Album/Page.flac")
                    else:
                        isViewImage=False
                        playSound(path+"Album/BackOut.flac")



                elif viewedImage+delta>11:
                    if currentImgPage<getImageLength()//12+1:
                        currentImgPage=imgPage
                        loadImages(imgPage,12)
                        viewedImage=0
                        playSound(path+"Album/Page.flac")
                    else:
                        isViewImage=False
                        playSound(path+"Album/BackOut.flac")

                elif images[viewedImage+delta]==None:
                    isViewImage=False
                    playSound(path+"Album/BackOut.flac")


                else:
                    viewedImage+=delta
                    playSound(path+"Album/Page.flac")







            else:
                if imgPage>=0 and imgPage<getImageLength()//12+1:
                    currentImgPage=imgPage
                    loadImages(currentImgPage,12)
                    threading.Thread(target=AlbumAnim).start()
                else:
                    threading.Thread(target=ssAsync,args=(screenNum,)).start()




        else:
            if screenNum==1:loadImages(currentImgPage,12)
            threading.Thread(target=ssAsync,args=(screenNum,)).start()

AnimSpeed=10
def AlbumAnim():
    elapsed=0
    while running and elapsed<1:
        elapsed+=AnimSpeed/math.sqrt(60*FPS)
        for image in images:
            if image!= None:
                image.set_alpha(255-255*elapsed)
        clock.tick(FPS)
    for image in images:
        if image!= None:
            image.set_alpha(9)

    loadImages(currentImgPage,12,invis=True)

    elapsed=0
    while running and elapsed<1:
        elapsed+=AnimSpeed/FPS
        for image in images:
            if image!= None:
                image.set_alpha(255*elapsed)
        clock.tick(FPS)
    for image in images:
        if image!= None:
            image.set_alpha(255)



def ssAsync(screenNum):
    global currentScreen,currentScreenGoal
    playSound(path+"Menu/MenuPage.flac")
    currentScreenGoal=screenNum
    elapsed=.01
    ΔscreenNum=0
    iscreenNum=currentScreen
    fscreenNum=screenNum
    ΔfscreenNum = fscreenNum-iscreenNum
    speed=.01

    while running:

        elapsed+=60*speed/FPS

        # ΔscreenNum=math.sqrt(math.sqrt(elapsed/2))*2*(ΔfscreenNum)
        ΔscreenNum=math.sqrt(elapsed/2)*3*(ΔfscreenNum)

        currentScreen=iscreenNum+ΔscreenNum
        if abs(ΔscreenNum) >= abs(ΔfscreenNum):
            ΔscreenNum=ΔfscreenNum
            currentScreen=iscreenNum+ΔscreenNum
            break
        clock.tick(FPS)

#!    ["RemoteBomb1","RemoteBomb2","Magnesis","Stasis","Cryonis","Camera","Amiibo","Zoom"]
runes=[None,         None,         None,       None,   None,     "Camera", None,   "Zoom"]
currentRune=None
elapsed=0
running=True
cooldown=0

def mobileInput():
    time=1
    while time>0:
        time-=1/FPS
        if kill:
            time=-9
    if time>-8:
        isMouseDown=True
        time=1
        while time>0:
            time-=1/FPS
        isMouseDown=False


while running:
    cooldown-=3/FPS
    isMouseDown=False
    match currentRune:
        case None:
            elapsed+=1/FPS
            deltatime=clock.get_time()

            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running=False
                    case pygame.MOUSEBUTTONDOWN:
                        threading.Thread(target=mobileInput).start()
                        mouseDownLocation=event.pos
                    case pygame.MOUSEBUTTONUP:
                        isMouseDown=False
                    case pygame.MOUSEMOTION:
                        if abs(event.rel[0])>50: switchScreenTo(event.rel[0]/abs(event.rel[0]))
                        cooldown=1
                        kill=(event.rel[0]>30 or event.rel[1]>30)
                        
                    case pygame.KEYDOWN:
                        match event.key:
                            # case pygame.K_a:
                            #     switchScreenTo(-1)
                            # case pygame.K_s:
                            #     switchScreenTo(0)
                            # case pygame.K_d:
                            #     switchScreenTo(1)
                            # case pygame.K_e:
                            #     switchScreenTo(-1)
                            # case pygame.K_r:
                            #     switchScreenTo(1)
                            case pygame.K_q:
                                running=False


            screen.fill((0,0,0))
            modifierPage = lambda page: page*screenWidth-currentScreen*screenWidth

            screen.blit(BG,(0,0))
            #####################!Runes#####################!Runes#####################!Runes
            bufferPercent=.01
            screen.blit(Rune1,(0+modifierPage(-1)+screenWidth/2-7*Rune1.get_size()[0]/2-bufferPercent*screenWidth*3,              screenHeight/2-Rune1.get_size()[0]/2))
            screen.blit(Rune2,(0+modifierPage(-1)+screenWidth/2-5*Rune2.get_size()[0]/2-bufferPercent*screenWidth*2,              screenHeight/2-Rune2.get_size()[0]/2))
            screen.blit(Rune3,(0+modifierPage(-1)+screenWidth/2-3*Rune3.get_size()[0]/2-bufferPercent*screenWidth,              screenHeight/2-Rune3.get_size()[0]/2))
            screen.blit(Rune4,(0+modifierPage(-1)+screenWidth/2-Rune4.get_size()[0]/2,              screenHeight/2-Rune4.get_size()[0]/2))
            screen.blit(Rune5,(0+modifierPage(-1)+screenWidth/2+Rune5.get_size()[0]/2+bufferPercent*screenWidth,              screenHeight/2-Rune5.get_size()[0]/2))
            screen.blit(Rune6,(0+modifierPage(-1)+screenWidth/2+3*Rune6.get_size()[0]/2+bufferPercent*screenWidth*2,              screenHeight/2-Rune6.get_size()[0]/2))
            screen.blit(Rune7,(0+modifierPage(-1)+screenWidth/2+5*Rune7.get_size()[0]/2+bufferPercent*screenWidth*3,              screenHeight/2-Rune7.get_size()[0]/2))

            Rune1Rect = (0+modifierPage(-1)+screenWidth/2-7*Rune1.get_size()[0]/2-bufferPercent*screenWidth*3,screenHeight/2-Rune1.get_size()[0]/2,Rune1.get_size()[0]+modifierPage(-1)+screenWidth/2-7*Rune1.get_size()[0]/2-bufferPercent*screenWidth*3,screenHeight/2+Rune1.get_size()[0]/2)
            Rune2Rect = (0+modifierPage(-1)+screenWidth/2-5*Rune2.get_size()[0]/2-bufferPercent*screenWidth*2,screenHeight/2-Rune2.get_size()[0]/2,Rune2.get_size()[0]+modifierPage(-1)+screenWidth/2-5*Rune2.get_size()[0]/2-bufferPercent*screenWidth*2,screenHeight/2+Rune2.get_size()[0]/2)
            Rune3Rect = (0+modifierPage(-1)+screenWidth/2-3*Rune3.get_size()[0]/2-bufferPercent*screenWidth,screenHeight/2-Rune3.get_size()[0]/2,Rune3.get_size()[0]+modifierPage(-1)+screenWidth/2-3*Rune3.get_size()[0]/2-bufferPercent*screenWidth,screenHeight/2+Rune3.get_size()[0]/2)
            Rune4Rect = (0+modifierPage(-1)+screenWidth/2-Rune4.get_size()[0]/2,screenHeight/2-Rune4.get_size()[0]/2,Rune4.get_size()[0]+modifierPage(-1)+screenWidth/2-Rune4.get_size()[0]/2,screenHeight/2+Rune4.get_size()[0]/2)
            Rune5Rect = (0+modifierPage(-1)+screenWidth/2+Rune5.get_size()[0]/2+bufferPercent*screenWidth,screenHeight/2-Rune5.get_size()[0]/2,Rune5.get_size()[0]+modifierPage(-1)+screenWidth/2+Rune5.get_size()[0]/2+bufferPercent*screenWidth,screenHeight/2+Rune5.get_size()[0]/2)
            Rune6Rect = (0+modifierPage(-1)+screenWidth/2+3*Rune6.get_size()[0]/2+bufferPercent*screenWidth*2,screenHeight/2-Rune6.get_size()[0]/2,Rune6.get_size()[0]+modifierPage(-1)+screenWidth/2+3*Rune6.get_size()[0]/2+bufferPercent*screenWidth*2,screenHeight/2+Rune6.get_size()[0]/2)
            Rune7Rect = (0+modifierPage(-1)+screenWidth/2+5*Rune7.get_size()[0]/2+bufferPercent*screenWidth*3,screenHeight/2-Rune7.get_size()[0]/2,Rune7.get_size()[0]+modifierPage(-1)+screenWidth/2+5*Rune7.get_size()[0]/2+bufferPercent*screenWidth*3,screenHeight/2+Rune7.get_size()[0]/2)
            runeBoxes=(Rune1Rect,Rune2Rect,Rune3Rect,Rune4Rect,Rune5Rect,Rune6Rect,Rune7Rect)
            #x1 y1 x2 y2
            runeNum=0
            for rune in runeBoxes:
                if isMouseDown and mouseDownLocation[0]>rune[0] and  mouseDownLocation[0]<rune[2] and  mouseDownLocation[1]>rune[1] and  mouseDownLocation[1]<rune[3]:
                    currentRune=runes[runeNum]
                    match runeNum:
                        case 0:
                            playSound(path+"Menu/SelectMenu.flac")
                        case 1:
                            playSound(path+"Menu/SelectMenu.flac")
                        case 2:
                            playSound(path+"Menu/SelectMenu.flac")
                        case 3:
                            playSound(path+"Menu/SelectMenu.flac")
                        case 4:
                            playSound(path+"Menu/SelectMenu.flac")
                        case 5:
                            playSound(path+"Menu/SelectMenu.flac")
                        case 6:
                            playSound(path+"Runes/PlaceAmiibo.flac")
                
                    
                runeNum+=1

            screen.blit(RunesTitle,(screenWidth/2-RunesTitle.get_size()[0]/2+modifierPage(-1),screenHeight/90))
            #####################!Map#####################!Map#####################!Map
            # screen.blit(BG,(0+modifierPage(0),0))

            # screen.blit(ShrineText, (screenWidth-ShrineIcon.get_size()[0]*1.5+modifierPage(0)-screenHeight*.1,screenHeight-ShrineIcon.get_size()[1]*1.5-abs(modifierPage(0))))
            # screen.blit(ShrineText2, (screenWidth-ShrineIcon.get_size()[0]*1.5+modifierPage(0)-screenHeight*.1,screenHeight-ShrineIcon.get_size()[1]*1.5-abs(modifierPage(0))))
            # screen.blit(ShrineIcon, (screenWidth-ShrineIcon.get_size()[0]*1.5+modifierPage(0),screenHeight-ShrineIcon.get_size()[1]*1.5-abs(modifierPage(0))))
            screen.blit(ShrineIcon2, (screenWidth-ShrineIcon2.get_size()[0]-ShrineIcon2.get_size()[1]*.2+modifierPage(0),screenHeight-ShrineIcon.get_size()[1]*1.2))
            screen.blit(DateTime, (ShrineIcon2.get_size()[1]*.2+modifierPage(0),screenHeight-(DateTime.get_size()[1])-ShrineIcon.get_size()[1]*.2))
            screen.blit(MapTitle,(screenWidth/2-MapTitle.get_size()[0]/2+modifierPage(0),screenHeight/90))
            #####################!Album#####################!Album#####################!Album
            # screen.blit(BG,(0+modifierPage(1),0))
            if currentScreenGoal == 1 or math.floor(currentScreen)==1 or math.ceil(currentScreen)==1:
                
                # screen.blit(Refresh,(0+modifierPage(1),0))
                # if isMouseDown and mouseDownLocation[0]<screenHeight*RefreshScale and  mouseDownLocation[1]<screenHeight*RefreshScale:
                #     loadImages(currentImgPage,12)


                if not isViewImage:
                    for i in range(12):
                        image=images[i]
                        if image!=None:

                            screen.blit(pygame.transform.scale(image, (screenWidth/5,screenHeight/4)),(screenWidth/20*(i%4+1)+screenWidth/5*(i%4)+modifierPage(1),    screenHeight/16*(i//4+1)+screenHeight/4*(i//4)))



                    if isMouseDown and mouseDownLocation[0]>screenWidth/20 and mouseDownLocation[0]<screenWidth*19/20 and mouseDownLocation[0]>screenHeight/16 and mouseDownLocation[0]<screenHeight*15/16:
                        isViewImage=True
                        # viewedImage= int(mouseDownLocation[0]*4//screenWidth + 4*(mouseDownLocation[1]*3//screenHeight))
                        mx, my = mouseDownLocation

                        col = int((mx - screenWidth/20) // (screenWidth/4))
                        row = int((my - screenHeight/16) // (screenHeight/4 + screenHeight/16))

                        if 0 <= col < 4 and 0 <= row < 3:
                            viewedImage = row * 4 + col







                        
                        playSound(path+"Menu/SelectMenu.flac")
                
                
                else:
                    if isMouseDown and mouseDownLocation[0]<screenWidth/20 and mouseDownLocation[1]<screenWidth/20:
                        isViewImage=False
                        playSound(path+"Album/BackOut.flac")
                    # imgsize=images[viewedImage].get_size()
                    # if imgsize[0]/imgsize[1]>screenWidth/screenHeight:
                    #     screen.blit(pygame.transform.scale(images[viewedImage], (screenWidth*7/8,screenWidth*7/8*imgsize[1]/imgsize[0])),(screenWidth/16,screenHeight/2-imgsize[1]/2))
                    # else:
                    #     screen.blit(pygame.transform.scale(images[viewedImage], (screenHeight*7/8*imgsize[0]/imgsize[1],screenHeight*7/8)),(screenWidth/2-imgsize[0]/2,screenHeight/16))
                    imgsize=images[viewedImage].get_size()

                    if imgsize[0]/imgsize[1]>screenWidth/screenHeight:
                        screen.blit(
                            pygame.transform.scale(
                                images[viewedImage],
                                (screenWidth*7/8,
                                screenWidth*7/8*imgsize[1]/imgsize[0])
                            ),
                            (screenWidth/16,
                            screenHeight/2-imgsize[1]/2)
                        )
                    else:
                        screen.blit(
                            pygame.transform.scale(
                                images[viewedImage],
                                (screenHeight*7/8*imgsize[0]/imgsize[1],
                                screenHeight*7/8)
                            ),
                            (screenWidth/2-imgsize[0]/2,
                            screenHeight/16)
                        )

            screen.blit(AlbumTitle,(screenWidth/2-AlbumTitle.get_size()[0]/2+modifierPage(1),screenHeight/90))
            #####################!Compendium#####################!Compendium#####################!Compendium
            
            



            screen.blit(CompendiumTitle,(screenWidth/2-CompendiumTitle.get_size()[0]/2+modifierPage(2),screenHeight/90))
            #####################!#####################!#####################!





            endScaleAnim = .5
            endFadeAnim = .7
            if elapsed < endScaleAnim:
                # InitIcon = pygame.transform.scale(pygame.image.load(path+"IconImg.png"), (screenHeight/InitIconScale+math.log(math.sqrt(elapsed*screenHeight))*40,screenHeight/InitIconScale+math.log(math.sqrt(elapsed*screenHeight))*40))
                InitIcon = pygame.transform.scale(pygame.image.load(path+"IconImg.png"), (screenHeight/InitIconScale+math.log(elapsed*screenHeight)*40,screenHeight/InitIconScale+math.log(elapsed*screenHeight)*40))
                screen.blit(InitIcon,(screenWidth/2-InitIcon.get_size()[0]/2,screenHeight/2-InitIcon.get_size()[1]/2))
            elif elapsed < endScaleAnim+endFadeAnim:
                # InitIcon = pygame.transform.scale(pygame.image.load(path+"IconImg.png"), (screenHeight/InitIconScale+math.log(math.sqrt(endScaleAnim*screenHeight))*40,screenHeight/InitIconScale+math.log(math.sqrt(endScaleAnim*screenHeight))*40))
                InitIcon = pygame.transform.scale(pygame.image.load(path+"IconImg.png"), (screenHeight/InitIconScale+math.log(endScaleAnim*screenHeight)*40,screenHeight/InitIconScale+math.log(endScaleAnim*screenHeight)*40))
                InitIcon.set_alpha(255-255*(elapsed-endScaleAnim)/endFadeAnim)
                screen.blit(InitIcon,(screenWidth/2-InitIcon.get_size()[0]/2,screenHeight/2-InitIcon.get_size()[1]/2))

            screen.blit(Glow,(0,0))
            pygame.display.flip()
            clock.tick(FPS)












#!####################################################################################################
#!####################################################################################################
#!####################################################################################################
#!####################################################################################################
        case "Camera":
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running=False
                    case pygame.MOUSEBUTTONDOWN:
                        if event.pos[0]<screenHeight*.1 and event.pos[1]<screenHeight*.1:
                            currentRune=None
                            playSound(path+"Exit.flac")
            screen.fill((0,0,0))
            pygame.display.flip()
            clock.tick(FPS)
#!####################################################################################################
#!####################################################################################################
#!####################################################################################################
#!####################################################################################################
        case "Zoom": #place markers with using the image its placed at to locate its position in later frames
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running=False
                    case pygame.MOUSEBUTTONDOWN:
                        if event.pos[0]<screenHeight*.1 and event.pos[1]<screenHeight*.1:
                            currentRune=None
                            playSound(path+"Exit.flac")
            screen.fill((0,0,0))
            pygame.display.flip()
            clock.tick(FPS)



playSound(path+"Exit.flac")
while pygame.mixer.music.get_busy():
    pygame.time.wait(100)