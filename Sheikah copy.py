import threading
def playSound(path):
    pass
def loadImages(_,__):
    pass
def getImageLength():
    pass
def AlbumAnim():
    pass
def ssAsync():
    pass
images=[None]*12
path=""
currentScreen=0












def SwitchScreenTo(delta):
    global currentImgPage,isViewImage,viewedImage
    screenNum=currentScreen+delta
    imgPage=currentImgPage+delta
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
                        viewedImage=11
                        playSound(path+"Album/Page.flac")
                    else:
                        isViewImage=False
                        playSound(path+"Album/BackOut.flac")


                else:
                    viewedImage+=delta
                    playSound(path+"Album/Page.flac")







            else:
                if imgPage>0 or imgPage<getImageLength()//12+1:
                    currentImgPage=imgPage
                    threading.Thread(target=AlbumAnim).start()
                else:
                    threading.Thread(target=ssAsync,args=(screenNum,)).start()




        else:
            threading.Thread(target=ssAsync,args=(screenNum,)).start()





def switchScreenToOld(screenNum):
    global currentImgPage,isViewImage,viewedImage
    print(screenNum)
    if screenNum>=-1 and screenNum<=2:
        if (currentScreen==1) and not isViewImage and not ((screenNum-currentScreen+currentImgPage)*12>getImageLength() or (screenNum-currentScreen+currentImgPage)<0):
            currentImgPage+=screenNum-currentScreen
            threading.Thread(target=AlbumAnim).start()
            playSound(path+"Album/Page.flac")
        elif (currentScreen==1) and isViewImage:
            if viewedImage>=11:
                if currentImgPage!=getImageLength()//12+1:
                    currentImgPage+=screenNum-currentScreen
                    viewedImage=0
                    loadImages(currentImgPage,12)
                    isViewImage=True
                    playSound(path+"Album/Page.flac")
                else:
                    isViewImage=False
                    threading.Thread(target=ssAsync,args=(screenNum,)).start()

                loadImages(currentImgPage,12)
            elif viewedImage <=0:
                if currentImgPage!=0:
                    currentImgPage+=screenNum-currentScreen
                    viewedImage=11
                    loadImages(currentImgPage,12)
                    isViewImage=True
                    playSound(path+"Album/Page.flac")
                else:
                    isViewImage=False
                    threading.Thread(target=ssAsync,args=(screenNum,)).start()
                
            else:
                viewedImage+=screenNum-round(currentScreen)
                playSound(path+"Album/Page.flac")
            if images[viewedImage] == None:
                isViewImage=False
                playSound(path+"Album/BackOut.flac")
            else:
                isViewImage=True
                
                

        else:
            if screenNum==1:
                loadImages(currentImgPage,12)
            threading.Thread(target=ssAsync,args=(screenNum,)).start()
