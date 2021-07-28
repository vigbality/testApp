import pygame
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from functions import *

pygame.init()
gameDisplay = pygame.display.set_mode((1366, 768),pygame.FULLSCREEN)
pygame.display.set_caption('testApp')
clock = pygame.time.Clock()





try:
   
    gameDisplay.blit(kvhvfBgImg, (0, 0))
    pygame.display.update()
    time.sleep(7)
    gameDisplay.blit(testappBG, (0, 0))
    pygame.display.update()
    speed = 0.01
    for i in range(1, 81):
        if i == 20:
            speed = 0.05
        if i == 60:
            speed = 0.15
        showText('Loading  ' + str(i) + '%', speed, white, 30, (670, 700))
        gameDisplay.blit(testappBG, (0, 0))
        pygame.display.update()
    
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("testapp-6d21738b9b56.json", scope)

    client = gspread.authorize(creds)
    dataFile = client.open("dataFile")
    resultData = client.open("resultData")
    for i in range(81, 101):
        speed = 0.05
        showText('Loading  ' + str(i) + '%', speed, white, 30, (670, 700))
        gameDisplay.blit(testappBG, (0, 0))
        pygame.display.update()
    main()
except:
    popUp('Please check your internet connectivity \nand try again.')
    pygame.quit()
    quit()
# ----------------------------------------------------CodeEndsHere------------------------------------------------------
