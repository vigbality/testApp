from functions import *
def studentPage():

  black = (0, 0, 0)
  white = (255, 255, 255)
  purple = (255, 10, 246)
  skyblue = (0, 215, 255)
  lightPurple = (245, 150, 240)
  green = (0, 200, 30)
  green1 = (0, 200, 100)
  homeButtonL = (200, 247, 12) 
  homeButtonR = (200, 247, 12)
  red = (235, 8, 0)
  yellow = (166,255,0)
  exitColor, infoColor ,backColor,availableTestsColor,viewResultsColor = yellow, yellow, yellow,yellow,yellow
  blue = (2, 59, 181)
# ------------------------------loadingImages-----------------------------------------------------------------

  backIcon = pygame.transform.scale(pygame.image.load('backIcon.png'), (35,35))
  exitIcon = pygame.transform.scale(pygame.image.load('exitIcon.png'), (35, 35))
  infoIcon = pygame.transform.scale(pygame.image.load('infoIcon.jpg'), (35, 35))
  vigbalityBG = pygame.transform.scale(pygame.image.load('vigbalityBG.jpg'), (1366, 768))
  testappBG = pygame.transform.scale(pygame.image.load('testappBG.jpg'), (1366, 768))


  run = True
  while run:
      
      gameDisplay.fill((12,12,12))
      pygame.draw.circle(gameDisplay,availableTestsColor, (680, 350), 125)
      pygame.draw.circle(gameDisplay, black, (680, 350), 120,3)
 
      blitText('WRITE',50,(600,305),black,'AllerDisplay.ttf')
      blitText('TEST',50,(643,350),black,'AllerDisplay.ttf')
      
      pygame.draw.circle(gameDisplay, backColor, (50, 50), 25)
      
      gameDisplay.blit(backIcon, (32, 32))
      
      pygame.display.update()
    
      for event in pygame.event.get():
          if event.type == pygame.MOUSEMOTION:  # for button color change
              xm, ym = event.pos
              if (((xm - 50) ** 2) + ((ym - 50) ** 2) - (25 ** 2)) < 0:
                  backColor = blue
              elif (((xm - 680) ** 2) + ((ym - 350) ** 2) - (125 ** 2)) < 0:
                  availableTestsColor = blue
                
              else:
                  availableTestsColor, viewResultsColor , backColor = yellow, yellow, yellow
          if event.type == pygame.MOUSEBUTTONUP:  # for button clicking
              pos = pygame.mouse.get_pos()
              xClick, yClick = pos
              if (((xm - 50) ** 2) + ((ym - 50) ** 2) - (25 ** 2)) < 0:
                  run = False
              if (((xm - 680) ** 2) + ((ym - 350) ** 2) - (125 ** 2)) < 0:
                  writeTest(getStudentName())
          if event.type == pygame.KEYDOWN:  # universal quiting option escape
              if event.key == pygame.K_ESCAPE:
                  run = False
                  pygame.quit()
                  quit()

  

