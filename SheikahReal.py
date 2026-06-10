import json
import pygame
import math
import threading
import os
import time

def takePicture():
    global thisimgpath, campicORsave, camera

    os.makedirs("Assets/pictures", exist_ok=True)

    filename = f"IMG_{int(time.time())}.jpg"
    filepath = os.path.join("Assets/pictures", filename)

    camera.capture_file(filepath)

    thisimgpath = filename  # only filename, since Compendium uses pathtoimg
    campicORsave = False    # go to naming screen
    print("saved",filepath)
previewImage=None
isSaveToCompendium=False
picElapsed=0
# Source - https://stackoverflow.com/a/48082769
# Posted by brentlance
# Retrieved 2026-06-09, License - CC BY-SA 3.0





pygame.init()
screen = pygame.display.set_mode((800,480))
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
pygame.display.set_caption("Sheikah Slate")
screenWidth, screenHeight = screen.get_size()

path="./Assets/"
pathtoimg="Assets/pictures"


#!PICAM
from picamera2 import Picamera2
import numpy as np

# Init camera
camera = Picamera2()

CAM_W, CAM_H = 1280, 720

config = camera.create_video_configuration(
    main={"size": (CAM_W, CAM_H), "format": "RGB888"}
)
camera.configure(config)
camera.start()

x = (screen.get_width() - CAM_W) // 2
y = (screen.get_height() - CAM_H) // 2
#!PICAM



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
Glow2V = pygame.image.load(path+"Glow copy.png")
Glow2V = pygame.transform.rotate(Glow2V,90.0)
Glow2V = pygame.transform.scale(Glow2V, (screenWidth,screenHeight))
Glow2H = pygame.image.load(path+"Glow copy.png")
Glow2H = pygame.transform.scale(Glow2H, (screenWidth,screenHeight))


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
RuneFGScaleBASE = 4
RuneFGScale = 4
RuneBG = pygame.image.load(path+"Runes/RuneBG.png")
RuneBG = pygame.transform.scale(RuneBG, (screenHeight/RuneScale,screenHeight/RuneScale))
# RuneFG = pygame.image.load(path+"Runes/RuneSelectFG.png")
# RuneFG = pygame.transform.scale(RuneFG, (screenHeight/RuneScale+RuneFGScale*2,screenHeight/RuneScale+RuneFGScale*2))
RuneFGBASE = pygame.image.load(path+"Runes/RuneSelectFG.png")


RuneLineScalex = 5/4
RuneLineScaley = 40
RuneLine = pygame.image.load(path+"Runes/RuneLine.png")
RuneLine = pygame.transform.scale(RuneLine, (screenHeight/RuneLineScalex,screenHeight/RuneLineScaley))

Rune1 = pygame.image.load(path+"Runes/BotW_Remote_Bomb_Icon.webp")
Rune1 = pygame.transform.scale(Rune1, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune2 = pygame.image.load(path+"Runes/BotW_Remote_Bomb_Icon2.png")
Rune2 = pygame.transform.scale(Rune2, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune3 = pygame.image.load(path+"Runes/BotW_Magnesis_Icon.webp")
Rune3 = pygame.transform.scale(Rune3, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune4 = pygame.image.load(path+"Runes/BotW_Stasis_Icon.png")
Rune4 = pygame.transform.scale(Rune4, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune5 = pygame.image.load(path+"Runes/BotW_Cryonis_Icon.png")
Rune5 = pygame.transform.scale(Rune5, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune6 = pygame.image.load(path+"Runes/BotW_Camera_Icon.png")
Rune6 = pygame.transform.scale(Rune6, (screenHeight/RuneScale,screenHeight/RuneScale))
Rune7 = pygame.image.load(path+"Runes/TotK_amiibo_Icon.png")
Rune7 = pygame.transform.scale(Rune7, (screenHeight/RuneScale,screenHeight/RuneScale))

compendiumBGimage = pygame.image.load(path+"BG.JPG")
compendiumBGimage = pygame.transform.scale(compendiumBGimage, (screenWidth/10,screenHeight/6))



InitIconScale = 1.5
InitIconM = pygame.image.load(path+"IconImg.png")
InitIconM = pygame.transform.scale(InitIconM, (screenHeight/InitIconScale,screenHeight/InitIconScale))
InitIconR = pygame.image.load(path+"IconImgRight.png")
InitIconR = pygame.transform.scale(InitIconR, (screenHeight/InitIconScale,screenHeight/InitIconScale))
InitIconL = pygame.image.load(path+"IconImgLeft.png")
InitIconL = pygame.transform.scale(InitIconL, (screenHeight/InitIconScale,screenHeight/InitIconScale))
#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES#!IMAGES
#!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT
font = pygame.font.SysFont("arial", 20)
subfont = pygame.font.SysFont("arial", 12)
compfont = pygame.font.SysFont("arial", 9)
spacingcompdots=20
compdotsfont = pygame.font.SysFont("sometype mono", spacingcompdots*3)


compendiumDots = compdotsfont.render("˙", True, (255,255,255))
compendiumDotsEtc = compdotsfont.render("˙", True, (100,100,100))


runesTitleText=["RemoteBomb","RemoteBomb","Magnesis","Stasis","Cryonis","Camera","Amiibo","Camera"]
runesSubTitle=["A bomb that can be detonated remotely","A bomb that can be detonated remotely","Manipulate metallic objects using magnetism","Stop the flow of time for an object","Create a pillar of ice from a water surface","Instantly render a visible image into a picture.","Amiibo","Instantly render a visible image into a picture."]
runesSubText=[
    ["The force of the blast can be used to damage monsters or","destroy objects. There are both round and cube bombs,","so use whichever best fits the situation"],
    ["The force of the blast can be used to damage monsters or","destroy objects. There are both round and cube bombs,","so use whichever best fits the situation"],
    ["Grab on to metallic objects using the magnetic energy that","pours forth from the Magnesis rune. objects held in the magnetic","snare can be lifted up and moved freely."],
    ["Stops an object in time while storing its kinetic energy.","The stored energy willl act upon the object when the flow","of time resumes. Making good use of the stored energy","can move even the largest of objects"],
    ["Builds ice pillars that are very stable. These pillars can be","used as stepping stones or as obstacles. Use Cryonis on","an ice pillar to break it"],
    ["Camera"],
    ["Amiibo"],
    ["Pictures ccreated are saved in the album. It has a useful","feature that connects to the Hyrule Compendium and","automatically registers pictures of new entries"]]
for title in range(len(runesTitleText)):
    runesTitleText[title]=font.render(runesTitleText[title], True, (108,219,247))
for title in range(len(runesSubTitle)):
    runesSubTitle[title]=font.render(runesSubTitle[title], True, (108,219,247))
for title in range(len(runesSubText)):
    for text in range(len(runesSubText[title])):
        runesSubText[title][text]=subfont.render(runesSubText[title][text], True, (108,219,247))
    # runesSubText[title]=font.render(runesSubText[title], True, (255,255,255))


RunesTitle = font.render("Runes", True, (255,255,255))
MapTitle = font.render("Map", True, (255,255,255))
AlbumTitle = font.render("Album", True, (255,255,255))
CompendiumTitle = font.render("Compendium", True, (255,255,255))

#!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT!TEXT

compendium = json.load(open("test.txt"))

FPS = 20
# compendium={
#     "Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "1Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "1Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "2Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "2Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "3Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "3Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "91Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "91Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "911Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "911Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "912Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "912Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "913Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "913Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "12Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "12Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "13Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "13Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "11Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "11Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "111Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "111Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "112Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "112Happy Barbary Macaque":"HappyMonkey copy.webp",
#     "113Barbary Macaque":"ThinkingMonkey copy 3.webp",
#     "113Happy Barbary Macaque":"HappyMonkey copy.webp",
#     # "Name":"filepath"  
#     }
def addToCompendium(path,name):
    global compendium
    if name in list(compendium.keys()): return False
    compendium[name]=path
    return True
images=[None]*12
imagesCompendium=[None]*24
titlesCompendium=[None]*24
def getImageLength():
    return len(os.listdir("Assets/pictures"))

def loadImages(page,perpage=12,invis=False):
    global images,pathtoimg
    num=0
    images=[None]*perpage
    for filename in os.listdir(pathtoimg):
        num+=1
        curpage=(num-1)//perpage
        if curpage!=page:
            continue
        images[(num-1)%perpage] = pygame.image.load(os.path.join(pathtoimg,filename))
        # images[num%perpage-1] = pygame.transform.scale(images[num%perpage-1], (screenWidth/5,screenHeight/4))
        if invis:
            images[(num-1)%perpage].set_alpha(0)




def loadImagesCompendium(page,perpage=24,invis=False):
    global imagesCompendium, compendium, titlesCompendium
    num=0
    imagesCompendium=[None]*perpage
    for file in list(compendium.keys()):
        filename=compendium[file]
        num+=1
        curpage=(num-1)//perpage
        if curpage!=page:
            continue
        imagesCompendium[(num-1)%perpage] = pygame.image.load(os.path.join(pathtoimg,filename))
        # titlesCompendium[(num-1)%perpage] = compfont.render(file, True, (255,255,255),None,round(screenWidth/10))

        max_width = round(screenWidth/10)

        text = file
        while compfont.size(text)[0] > max_width and len(text) > 0:
            text = text[:-1]

        if text != file:
            text += "..."

        titlesCompendium[(num-1)%perpage] = compfont.render(
            text, True, (255,255,255)
        )


        # images[num%perpage-1] = pygame.transform.scale(images[num%perpage-1], (screenWidth/5,screenHeight/4))
        if invis:
            imagesCompendium[(num-1)%perpage].set_alpha(0)








currentScreen=0
currentScreenGoal=0
currentImgPage = 0

currentImgPageCompendium = 0
isMouseDown=False
mouseDownLocation=(0,0)

isViewImage=False
viewedImage=0
def switchScreenTo(delta):
    global currentImgPage,currentImgPageCompendium,isViewImage,viewedImage
    delta=int(delta)
    screenNum=currentScreen+delta
    imgPage=currentImgPage+delta
    imgPageCompendium=currentImgPageCompendium+delta
    if screenNum>=-1 and screenNum<=2 or screenNum==3:

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
                    # loadImages(currentImgPage,12)
                    threading.Thread(target=AlbumAnim).start()
                else:
                    if delta>0: loadImagesCompendium(currentImgPageCompendium,24)
                    threading.Thread(target=ssAsync,args=(screenNum,)).start()




        elif currentScreen==2:



            if isViewImage:
                if viewedImage+delta<0:
                    if currentImgPageCompendium>0:
                        currentImgPageCompendium=imgPageCompendium
                        loadImagesCompendium(currentImgPageCompendium,24)
                        viewedImage=23
                        playSound(path+"Album/Page.flac")
                    else:
                        isViewImage=False
                        playSound(path+"Album/BackOut.flac")



                elif viewedImage+delta>23:
                    if currentImgPageCompendium<len(list(compendium.keys()))//24+1:
                        currentImgPageCompendium=imgPageCompendium
                        loadImagesCompendium(currentImgPageCompendium,24)
                        viewedImage=0
                        playSound(path+"Album/Page.flac")
                    else:
                        isViewImage=False
                        playSound(path+"Album/BackOut.flac")

                elif imagesCompendium[viewedImage+delta]==None:
                    isViewImage=False
                    playSound(path+"Album/BackOut.flac")


                else:
                    viewedImage+=delta
                    playSound(path+"Album/Page.flac")







            else:
                if imgPageCompendium>=0 and imgPageCompendium<len(list(compendium.keys()))//24+1:
                    currentImgPageCompendium=imgPageCompendium

                    threading.Thread(target=AlbumAnimCompendium).start()
                else:
                    threading.Thread(target=ssAsync,args=(screenNum,)).start()
                    if screenNum==1:loadImages(currentImgPage,12)




        else:
            if screenNum==1:loadImages(currentImgPage,12)
            if screenNum==2:loadImagesCompendium(currentImgPageCompendium,24)
            threading.Thread(target=ssAsync,args=(screenNum,)).start()

AnimSpeed=10
def AlbumAnim():
    elapsedAA=0
    while running and elapsedAA<1:
        elapsedAA+=AnimSpeed/math.sqrt(60*FPS)
        for image in images:
            if image!= None:
                image.set_alpha(255-255*elapsedAA)
        clock.tick(FPS)
    for image in images:
        if image!= None:
            image.set_alpha(0)

    loadImages(currentImgPage,12,invis=True)

    elapsedAA=0
    while running and elapsedAA<1:
        elapsedAA+=AnimSpeed/FPS
        for image in images:
            if image!= None:
                image.set_alpha(255*elapsedAA)
        clock.tick(FPS)
    for image in images:
        if image!= None:
            image.set_alpha(255)
albumCompendiumInAnim=False
def AlbumAnimCompendium():
    global albumCompendiumInAnim
    albumCompendiumInAnim=True
    elapsedAAC=0
    while running and elapsedAAC<1:
        elapsedAAC+=AnimSpeed/math.sqrt(60*FPS)
        for image in imagesCompendium:
            if image!= None:
                image.set_alpha(255-255*elapsedAAC)
        clock.tick(FPS)
    for image in imagesCompendium:
        if image!= None:
            image.set_alpha(0)

    loadImagesCompendium(currentImgPageCompendium,24,invis=True)

    elapsedAAC=0
    while running and elapsedAAC<1:
        elapsedAAC+=AnimSpeed/FPS
        for image in imagesCompendium:
            if image!= None:
                image.set_alpha(255*elapsedAAC)
        clock.tick(FPS)
    for image in imagesCompendium:
        if image!= None:
            image.set_alpha(255)
    albumCompendiumInAnim=False



def ssAsync(screenNum):
    global currentScreen,currentScreenGoal
    if screenNum<-1 or screenNum>2: return None

    playSound(path+"Menu/MenuPage.flac")
    currentScreenGoal=screenNum
    elapsedssa=.01
    ΔscreenNum=0
    iscreenNum=currentScreen
    fscreenNum=screenNum
    ΔfscreenNum = fscreenNum-iscreenNum
    speed=.01

    while running:

        elapsedssa+=60*speed/FPS

        # ΔscreenNum=math.sqrt(math.sqrt(elapsedssa/2))*2*(ΔfscreenNum)
        ΔscreenNum=math.sqrt(elapsedssa/2)*3*(ΔfscreenNum)

        currentScreen=iscreenNum+ΔscreenNum
        if abs(ΔscreenNum) >= abs(ΔfscreenNum):
            ΔscreenNum=ΔfscreenNum
            currentScreen=iscreenNum+ΔscreenNum
            break
        clock.tick(FPS)

#!    ["RemoteBomb1","RemoteBomb2","Magnesis","Stasis","Cryonis","Camera","Amiibo","Zoom"]
runes=[None,         None,         None,       None,   None,     "Camera", None,   "Zoom"]

currentRune=None
currentRuneReal=0
elapsed=0
running=True
cooldown=0


touchStart = None
touchMoved = False
SWIPE_THRESHOLD = 50

modifierPage = lambda page: page*screenWidth-currentScreen*screenWidth
modifierOpacity = lambda page: min(255,max(255-255*(1.5)*abs(page-currentScreen),0))
def withOpac(obj,page):
    obj.set_alpha(modifierOpacity(page))
    return obj

oscillator=0
campicORsave=False
thisimgpath=""
keyboardSingle=False

# KEY LAYOUT SETTINGS
KEY_W = 60
KEY_H = 60
MARGIN = 10
WIDTH = screenHeight*.1
keyslist = [
    # row 1
    ("Q", 0, 0), ("W", 1, 0), ("E", 2, 0), ("R", 3, 0), ("T", 4, 0),
    ("Y", 5, 0), ("U", 6, 0), ("I", 7, 0), ("O", 8, 0), ("P", 9, 0),
    # row 2 (offset)
    ("A", 0.5, 1), ("S", 1.5, 1), ("D", 2.5, 1), ("F", 3.5, 1),
    ("G", 4.5, 1), ("H", 5.5, 1), ("J", 6.5, 1), ("K", 7.5, 1), ("L", 8.5, 1),
    # row 3 (more offset)
    ("Z", 1.5, 2), ("X", 2.5, 2), ("C", 3.5, 2), ("V", 4.5, 2),
    ("B", 5.5, 2), ("N", 6.5, 2), ("M", 7.5, 2), ("del", -1, 3), (" ", 0, 3), ("submit", 1, 3)
]
typed_text = ""
delay = .3
endSplitAnim = .5
endFadeAnim = .7


while running:
    oscillator+=8/FPS
    cooldown-=3/FPS
    isMouseDown=False
    match currentRune:
        case None:
            print(round(clock.get_fps(), 3))
            elapsed+=1/FPS
            deltatime=clock.get_time()


            for event in pygame.event.get():
                match event.type:

                    case pygame.QUIT:
                        running = False

                    # Mouse support
                    case pygame.MOUSEBUTTONDOWN:
                        touchStart = event.pos
                        touchMoved = False

                    case pygame.MOUSEMOTION:
                        if touchStart:
                            dx = event.pos[0] - touchStart[0]
                            dy = event.pos[1] - touchStart[1]

                            if abs(dx) > SWIPE_THRESHOLD or abs(dy) > SWIPE_THRESHOLD:
                                touchMoved = True

                    case pygame.MOUSEBUTTONUP:
                        if touchStart:
                            dx = event.pos[0] - touchStart[0]
                            dy = event.pos[1] - touchStart[1]

                            if abs(dx) > SWIPE_THRESHOLD:
                                print("RIGHT" if dx > 0 else "LEFT")
                                if dx<0:
                                    switchScreenTo(1)
                                else: 
                                    switchScreenTo(-1)


                            elif abs(dy) > SWIPE_THRESHOLD:
                                print("DOWN" if dy > 0 else "UP")

                            else:
                                print("Click")
                                # Click
                                mouseDownLocation = event.pos
                                isMouseDown = True

                        touchStart = None
                        
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_q:
                                running=False


            screen.fill((0,0,0))

            screen.blit(BG,(0,0))
            #####################!Runes#####################!Runes#####################!Runes
            if currentScreenGoal == -1 or math.floor(currentScreen)==-1 or math.ceil(currentScreen)==-1:
                bufferPercent=.01

                RuneFGScale=round(RuneFGScaleBASE+math.sin(oscillator)*3)
                RuneFG = pygame.transform.scale(RuneFGBASE, (screenHeight/RuneScale+RuneFGScale*2,screenHeight/RuneScale+RuneFGScale*2))
                runeHeight=-screenHeight*.1
                screen.blit(RuneBG,(0+modifierPage(-1)+screenWidth/2-7*Rune1.get_size()[0]/2-bufferPercent*screenWidth*3,              screenHeight/2-Rune1.get_size()[0]/2+runeHeight))
                screen.blit(Rune1,(0+modifierPage(-1)+screenWidth/2-7*Rune1.get_size()[0]/2-bufferPercent*screenWidth*3,              screenHeight/2-Rune1.get_size()[0]/2+runeHeight))
                if currentRuneReal==0:
                    screen.blit(RuneFG,(-RuneFGScale+modifierPage(-1)+screenWidth/2-7*Rune1.get_size()[0]/2-bufferPercent*screenWidth*3,              screenHeight/2-Rune1.get_size()[0]/2-RuneFGScale+runeHeight))
                
                screen.blit(RuneBG,(0+modifierPage(-1)+screenWidth/2-5*Rune2.get_size()[0]/2-bufferPercent*screenWidth*2,              screenHeight/2-Rune2.get_size()[0]/2+runeHeight))
                screen.blit(Rune2,(0+modifierPage(-1)+screenWidth/2-5*Rune2.get_size()[0]/2-bufferPercent*screenWidth*2,              screenHeight/2-Rune2.get_size()[0]/2+runeHeight))
                if currentRuneReal==1:
                    screen.blit(RuneFG,(-RuneFGScale+modifierPage(-1)+screenWidth/2-5*Rune2.get_size()[0]/2-bufferPercent*screenWidth*2,              screenHeight/2-Rune2.get_size()[0]/2-RuneFGScale+runeHeight))
                
                screen.blit(RuneBG,(0+modifierPage(-1)+screenWidth/2-3*Rune3.get_size()[0]/2-bufferPercent*screenWidth,              screenHeight/2-Rune3.get_size()[0]/2+runeHeight))
                screen.blit(Rune3,(0+modifierPage(-1)+screenWidth/2-3*Rune3.get_size()[0]/2-bufferPercent*screenWidth,              screenHeight/2-Rune3.get_size()[0]/2+runeHeight))
                if currentRuneReal==2:
                    screen.blit(RuneFG,(-RuneFGScale+modifierPage(-1)+screenWidth/2-3*Rune3.get_size()[0]/2-bufferPercent*screenWidth,              screenHeight/2-Rune3.get_size()[0]/2-RuneFGScale+runeHeight))

                
                screen.blit(RuneBG,(0+modifierPage(-1)+screenWidth/2-Rune4.get_size()[0]/2,              screenHeight/2-Rune4.get_size()[0]/2+runeHeight))
                screen.blit(Rune4,(0+modifierPage(-1)+screenWidth/2-Rune4.get_size()[0]/2,              screenHeight/2-Rune4.get_size()[0]/2+runeHeight))
                if currentRuneReal==3:
                    screen.blit(RuneFG,(-RuneFGScale+modifierPage(-1)+screenWidth/2-Rune4.get_size()[0]/2,              screenHeight/2-Rune4.get_size()[0]/2-RuneFGScale+runeHeight))

                
                screen.blit(RuneBG,(0+modifierPage(-1)+screenWidth/2+Rune5.get_size()[0]/2+bufferPercent*screenWidth,              screenHeight/2-Rune5.get_size()[0]/2+runeHeight))
                screen.blit(Rune5,(0+modifierPage(-1)+screenWidth/2+Rune5.get_size()[0]/2+bufferPercent*screenWidth,              screenHeight/2-Rune5.get_size()[0]/2+runeHeight))
                if currentRuneReal==4:
                    screen.blit(RuneFG,(-RuneFGScale+modifierPage(-1)+screenWidth/2+Rune5.get_size()[0]/2+bufferPercent*screenWidth,              screenHeight/2-Rune5.get_size()[0]/2-RuneFGScale+runeHeight))

                
                screen.blit(RuneBG,(0+modifierPage(-1)+screenWidth/2+3*Rune6.get_size()[0]/2+bufferPercent*screenWidth*2,              screenHeight/2-Rune6.get_size()[0]/2+runeHeight))
                screen.blit(Rune6,(0+modifierPage(-1)+screenWidth/2+3*Rune6.get_size()[0]/2+bufferPercent*screenWidth*2,              screenHeight/2-Rune6.get_size()[0]/2+runeHeight))
                if currentRuneReal==5:
                    screen.blit(RuneFG,(-RuneFGScale+modifierPage(-1)+screenWidth/2+3*Rune6.get_size()[0]/2+bufferPercent*screenWidth*2,              screenHeight/2-Rune6.get_size()[0]/2-RuneFGScale+runeHeight))

                
                screen.blit(RuneBG,(0+modifierPage(-1)+screenWidth/2+5*Rune7.get_size()[0]/2+bufferPercent*screenWidth*3,              screenHeight/2-Rune7.get_size()[0]/2+runeHeight))
                screen.blit(Rune7,(0+modifierPage(-1)+screenWidth/2+5*Rune7.get_size()[0]/2+bufferPercent*screenWidth*3,              screenHeight/2-Rune7.get_size()[0]/2+runeHeight))
                if currentRuneReal==6:
                    screen.blit(RuneFG,(-RuneFGScale+modifierPage(-1)+screenWidth/2+5*Rune7.get_size()[0]/2+bufferPercent*screenWidth*3,              screenHeight/2-Rune7.get_size()[0]/2-RuneFGScale+runeHeight))


                #!!
                linespacing=15
                lineNum=0
                screen.blit(runesTitleText[currentRuneReal],(screenWidth/2-runesTitleText[currentRuneReal].get_size()[0]/2+modifierPage(-1),screenHeight/15))
                screen.blit(runesSubTitle[currentRuneReal],(screenWidth/2-runesSubTitle[currentRuneReal].get_size()[0]/2+modifierPage(-1),screenHeight/2))
                screen.blit(RuneLine,(screenWidth/2-RuneLine.get_size()[0]/2+modifierPage(-1),screenHeight/2+linespacing*2))


                for line in runesSubText[currentRuneReal]:
                    screen.blit(line,(screenWidth/2-line.get_size()[0]/2+modifierPage(-1),screenHeight/2+linespacing*(lineNum+4)))
                    lineNum+=1
                #!!


                Rune1Rect = (0+modifierPage(-1)+screenWidth/2-7*Rune1.get_size()[0]/2-bufferPercent*screenWidth*3,screenHeight/2-Rune1.get_size()[0]/2+runeHeight,Rune1.get_size()[0]+modifierPage(-1)+screenWidth/2-7*Rune1.get_size()[0]/2-bufferPercent*screenWidth*3,screenHeight/2+Rune1.get_size()[0]/2)
                Rune2Rect = (0+modifierPage(-1)+screenWidth/2-5*Rune2.get_size()[0]/2-bufferPercent*screenWidth*2,screenHeight/2-Rune2.get_size()[0]/2+runeHeight,Rune2.get_size()[0]+modifierPage(-1)+screenWidth/2-5*Rune2.get_size()[0]/2-bufferPercent*screenWidth*2,screenHeight/2+Rune2.get_size()[0]/2)
                Rune3Rect = (0+modifierPage(-1)+screenWidth/2-3*Rune3.get_size()[0]/2-bufferPercent*screenWidth,screenHeight/2-Rune3.get_size()[0]/2+runeHeight,Rune3.get_size()[0]+modifierPage(-1)+screenWidth/2-3*Rune3.get_size()[0]/2-bufferPercent*screenWidth,screenHeight/2+Rune3.get_size()[0]/2)
                Rune4Rect = (0+modifierPage(-1)+screenWidth/2-Rune4.get_size()[0]/2,screenHeight/2-Rune4.get_size()[0]/2+runeHeight,Rune4.get_size()[0]+modifierPage(-1)+screenWidth/2-Rune4.get_size()[0]/2,screenHeight/2+Rune4.get_size()[0]/2)
                Rune5Rect = (0+modifierPage(-1)+screenWidth/2+Rune5.get_size()[0]/2+bufferPercent*screenWidth,screenHeight/2-Rune5.get_size()[0]/2+runeHeight,Rune5.get_size()[0]+modifierPage(-1)+screenWidth/2+Rune5.get_size()[0]/2+bufferPercent*screenWidth,screenHeight/2+Rune5.get_size()[0]/2)
                Rune6Rect = (0+modifierPage(-1)+screenWidth/2+3*Rune6.get_size()[0]/2+bufferPercent*screenWidth*2,screenHeight/2-Rune6.get_size()[0]/2+runeHeight,Rune6.get_size()[0]+modifierPage(-1)+screenWidth/2+3*Rune6.get_size()[0]/2+bufferPercent*screenWidth*2,screenHeight/2+Rune6.get_size()[0]/2)
                Rune7Rect = (0+modifierPage(-1)+screenWidth/2+5*Rune7.get_size()[0]/2+bufferPercent*screenWidth*3,screenHeight/2-Rune7.get_size()[0]/2+runeHeight,Rune7.get_size()[0]+modifierPage(-1)+screenWidth/2+5*Rune7.get_size()[0]/2+bufferPercent*screenWidth*3,screenHeight/2+Rune7.get_size()[0]/2)
                runeBoxes=(Rune1Rect,Rune2Rect,Rune3Rect,Rune4Rect,Rune5Rect,Rune6Rect,Rune7Rect)
                #x1 y1 x2 y2
                runeNum=0
                for rune in runeBoxes:
                    if isMouseDown and mouseDownLocation[0]>rune[0] and  mouseDownLocation[0]<rune[2] and  mouseDownLocation[1]>rune[1] and  mouseDownLocation[1]<rune[3]:
                        currentRune=runes[runeNum]
                        currentRuneReal=runeNum
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

            # screen.blit(RunesTitle,(screenWidth/2-RunesTitle.get_size()[0]/2+modifierPage(-1),screenHeight/90))
            #####################!Map#####################!Map#####################!Map
            if currentScreenGoal == 0 or math.floor(currentScreen)==0 or math.ceil(currentScreen)==0:
                Glow2H.set_alpha(modifierOpacity(0))
                Glow2V.set_alpha(modifierOpacity(0))
                screen.blit(Glow2H,(0+modifierPage(0),0))   #! NEW GLOW
                screen.blit(Glow2V,(0+modifierPage(0),0))   #! NEW GLOW

                screen.blit(ShrineIcon2, (screenWidth-ShrineIcon2.get_size()[0]-ShrineIcon2.get_size()[1]*.2+modifierPage(0),screenHeight-ShrineIcon.get_size()[1]*1.2))
                screen.blit(DateTime, (ShrineIcon2.get_size()[1]*.2+modifierPage(0),screenHeight-(DateTime.get_size()[1])-ShrineIcon.get_size()[1]*.2))


                # screen.blit(MapTitle,(screenWidth/2-MapTitle.get_size()[0]/2+modifierPage(0),screenHeight/90))
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

                            # screen.blit(pygame.transform.scale(image, (screenWidth/5,screenHeight/4)),(screenWidth/20*(i%4+1)+screenWidth/5*(i%4)+modifierPage(1),    screenHeight/16*(i//4+1)+screenHeight/4*(i//4)))
                            screen.blit(pygame.transform.scale(image, (screenWidth/5,screenHeight/4)),(screenWidth/40+screenWidth/20*(i%4)+screenWidth/5*(i%4)+modifierPage(1),    screenHeight/16*(i//4+1)+screenHeight/4*(i//4)))



                    if isMouseDown and mouseDownLocation[0]>screenWidth/20 and mouseDownLocation[0]<screenWidth*19/20 and mouseDownLocation[0]>screenHeight/16 and mouseDownLocation[0]<screenHeight*15/16:
                        # viewedImage= int(mouseDownLocation[0]*4//screenWidth + 4*(mouseDownLocation[1]*3//screenHeight))
                        mx, my = mouseDownLocation

                        col = int((mx - screenWidth/20) // (screenWidth/4))
                        row = int((my - screenHeight/16) // (screenHeight/4 + screenHeight/16))

                        if 0 <= col < 4 and 0 <= row < 3 and images[row * 4 + col]!=None:
                            viewedImage = row * 4 + col
                            isViewImage=True







                        
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
                        new = pygame.transform.scale(
                                images[viewedImage],
                                (screenWidth*7/8,
                                screenWidth*7/8*imgsize[1]/imgsize[0])
                            )
                        screen.blit(
                            new,
                            (screenWidth/2-new.get_size()[0]/2,
                            screenHeight/2-new.get_size()[1]/2)
                        )
                    else:
                        new = pygame.transform.scale(
                                images[viewedImage],
                                (screenHeight*7/8*imgsize[0]/imgsize[1],
                                screenHeight*7/8)
                            )
                        screen.blit(
                            new,
                            (screenWidth/2-new.get_size()[0]/2,
                            screenHeight/2-new.get_size()[1]/2)
                        )

            # screen.blit(AlbumTitle,(screenWidth/2-AlbumTitle.get_size()[0]/2+modifierPage(1),screenHeight/90))
            #####################!Compendium#####################!Compendium#####################!Compendium
            if currentScreenGoal == 2 or math.floor(currentScreen)==2 or math.ceil(currentScreen)==2:
                if not isViewImage:
                    pages=len(list(compendium.keys()))//24+1
                    for i in range(pages):
                        if i == currentImgPageCompendium:screen.blit(compendiumDots,(screenWidth/2-spacingcompdots*(pages/2)+spacingcompdots*i,screenHeight/40))
                        else: screen.blit(compendiumDotsEtc,(screenWidth/2-spacingcompdots*(pages/2)+spacingcompdots*i,screenHeight/40))

                    for i in range(24):
                        image=imagesCompendium[i]
                        text=titlesCompendium[i]
                        screen.blit(line,(screenWidth/2-line.get_size()[0]/2+modifierPage(-1),screenHeight/2+linespacing*(lineNum+4)))

                        if image!=None:
                            screen.blit(pygame.transform.scale(image, (screenWidth/10,screenHeight/6)),(screenWidth/80+screenWidth/40*(i%8)+screenWidth/10*(i%8)+modifierPage(2),    screenHeight/16*(i//8-1)+screenHeight/5*(i//8+1)))
                            screen.blit(text,                                                                    (screenWidth/80+screenWidth/40*(i%8)+screenWidth/10*(i%8)+modifierPage(2),screenHeight/16*(i//8-1)+screenHeight/5*(i//8+2)-screenHeight/100))

                        else:
                            screen.blit(compendiumBGimage,(screenWidth/80+screenWidth/40*(i%8)+screenWidth/10*(i%8)+modifierPage(2),    screenHeight/16*(i//8-1)+screenHeight/5*(i//8+1)))
                        if not albumCompendiumInAnim: screen.blit(compfont.render(str(i+currentImgPageCompendium*24+1), True, (108,219,247), (0,0,0)),(screenWidth/80+screenWidth/40*(i%8)+screenWidth/10*(i%8)+modifierPage(2),screenHeight/16*(i//8-1)+screenHeight/5*(i//8+2)-screenHeight/18))

                    if isMouseDown and mouseDownLocation[0]>screenWidth/20 and mouseDownLocation[0]<screenWidth*19/20 and mouseDownLocation[0]>screenHeight/16 and mouseDownLocation[0]<screenHeight*15/16:
                        # viewedImage= int(mouseDownLocation[0]*4//screenWidth + 4*(mouseDownLocation[1]*3//screenHeight))
                        mx, my = mouseDownLocation

                        col = int((mx - screenWidth/20) // (screenWidth/8))
                        row = int((my - screenHeight/16) // (screenHeight/4 + screenHeight/16))

                        if 0 <= col < 8 and 0 <= row < 3 and imagesCompendium[row * 8 + col]!=None:
                            viewedImage = row * 8 + col
                            isViewImage=True







                        
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
                    imgsize=imagesCompendium[viewedImage].get_size()

                    if imgsize[0]/imgsize[1]>screenWidth/screenHeight:
                        new = pygame.transform.scale(
                                imagesCompendium[viewedImage],
                                (screenWidth*7/8,
                                screenWidth*7/8*imgsize[1]/imgsize[0])
                            )
                        screen.blit(
                            new,
                            (screenWidth/2-new.get_size()[0]/2,
                            screenHeight/2-new.get_size()[1]/2)
                        )
                    else:
                        new = pygame.transform.scale(
                                imagesCompendium[viewedImage],
                                (screenHeight*7/8*imgsize[0]/imgsize[1],
                                screenHeight*7/8)
                            )
                        screen.blit(
                            new,
                            (screenWidth/2-new.get_size()[0]/2,
                            screenHeight/2-new.get_size()[1]/2)
                        )
            



            # screen.blit(CompendiumTitle,(screenWidth/2-CompendiumTitle.get_size()[0]/2+modifierPage(2),screenHeight/90))
            #####################!#####################!#####################!

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

            screen.blit(Glow,(0,0))
            pygame.display.flip()
            clock.tick(FPS)












#!####################################################################################################
#!####################################################################################################
#!####################################################################################################
#!####################################################################################################
        case "Camera":
            print(round(clock.get_fps(), 3))
            keys=[]
            isTouchDown=False
            screen.fill((0,100,0))
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running=False
                    case pygame.MOUSEBUTTONDOWN:
                        if event.pos[0]<screenHeight*.1 and event.pos[1]<screenHeight*.1:
                            currentRune=None
                            playSound(path+"Exit.flac")
                        isTouchDown=True
                        mouse_pos=event.pos
                    case pygame.KEYDOWN:
                        print(event)
                        if not campicORsave:
                            if event.key==8:
                                typed_text=typed_text[:-1]
                                print("DELETE DELETE")
                            else:
                                typed_text=typed_text+str(event.unicode)
                        keys.append(event.key)

            pygame.draw.rect(screen,(255,0,0),(0,0,screenHeight*.1,screenHeight*.1))
            if currentRune==None:
                continue











            match campicORsave:
                case True:
                    previewImage=None
                    typed_text=""
                    # getpic()
                    start = time.time()
                    frame = camera.capture_array()
                    print(time.time() - start)
                    frame = frame[:, :, ::-1]  # swap BGR -> RGB

                    img = pygame.image.frombuffer(
                        frame.tobytes(),
                        (CAM_W, CAM_H),
                        "RGB"
                    )

                    screen.fill(0)
                    if img:
                        screen.blit(pygame.transform.scale(img,(screenWidth,screenHeight)), (0,0))
                    if isTouchDown:
                        takePicture()
                        previewImage=pygame.transform.scale(pygame.image.load(os.path.join("Assets/pictures",thisimgpath)),(screenWidth*.9,screenHeight*.9))
                        if mouse_pos[0]<screenWidth/2:
                            isSaveToCompendium=True
                        else:
                            isSaveToCompendium=False
                    pygame.display.update()












                    picElapsed=0
                case False:
                    if isSaveToCompendium:


                        # ---- INSIDE YOUR GAME LOOP BELOW EVENT HANDLING ----

                        mouse_pressed = pygame.mouse.get_pressed()[0]
                        mouse_pos = pygame.mouse.get_pos()

                        start_y = 120
                        row_spacing = KEY_H + MARGIN

                        # DRAW KEYS
                        for label, col, row in keyslist:
                            x = int((WIDTH // 2 - 5 * (KEY_W + MARGIN)) + col * (KEY_W + MARGIN) + screenWidth/2)
                            y = start_y + row * row_spacing

                            rect = pygame.Rect(x, y, KEY_W, KEY_H)

                            pygame.draw.rect(screen, (40, 40, 40), rect, border_radius=8)
                            pygame.draw.rect(screen, (200, 200, 200), rect, 2, border_radius=8)

                            text = font.render(label, True, (255, 255, 255))
                            screen.blit(text, text.get_rect(center=rect.center))

                            # INPUT CHECK (touch/mouse)
                            if mouse_pressed and not keyboardSingle and rect.collidepoint(mouse_pos):
                                if label=="del":
                                    typed_text=typed_text[:-1]
                                elif label=="submit":
                                    if isSaveToCompendium:
                                        if addToCompendium(thisimgpath,typed_text):
                                            print("yay")
                                        else:
                                            print("Nay")
                                    campicORsave=True
                                else:
                                    typed_text += label
                                    print(typed_text)
                                    print(label)
                                # pygame.time.wait(50)  # simple debounce so it doesn't spam
                                keyboardSingle=True
                            elif not mouse_pressed:
                                keyboardSingle=False
                        # OPTIONAL DISPLAY CURRENT TEXT
                        text_surface = font.render(typed_text, True, (255, 255, 255))
                        screen.blit(text_surface, (20, 20))
                        if previewImage != None:
                            screen.blit(pygame.transform.scale(previewImage,(CAM_W/6,CAM_H/6)),(screenWidth*5/12,0))
                    else:
                        picElapsed+=1/FPS
                        if picElapsed>=1:
                            campicORsave=True
                        if previewImage != None:
                            screen.blit(previewImage,(screenWidth*.05,screenHeight*.05))










                    #prompt save.  #! Name filename with compendium number



                




            pygame.display.flip()
            clock.tick(FPS)
#!####################################################################################################
#!####################################################################################################
#!####################################################################################################
#!####################################################################################################
        case "Zoom": #place markers with using the image its placed at to locate its position in later frames
            screen.fill((0,0,0))
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running=False
                    case pygame.MOUSEBUTTONDOWN:
                        if event.pos[0]<screenHeight*.1 and event.pos[1]<screenHeight*.1:
                            currentRune=None
                            playSound(path+"Exit.flac")
            pygame.display.flip()
            clock.tick(FPS)



playSound(path+"Exit.flac")
while pygame.mixer.music.get_busy():
    pygame.time.wait(100)
json.dump(compendium, open("test.txt","w"))
print("SAVED")

camera.close()
pygame.display.quit()
