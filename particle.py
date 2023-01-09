import PIL
import cv2
import pyautogui as pg
import numpy as np
import pytesseract as tess
import math
import time

#delay to get to the right tab
time.sleep(5)

#ill add function that makes sure the right settings are on and a new indicator is picked up

#initial x and y vel of cursor
xvel = 0
yvel = 0

#find current position of mouse/indicator
xpos = pg.position()[0]
ypos = pg.position()[1]

#loop that moves cursor
while True:
  #box to search for angle + v/m is 45 to each side and 50 up
  vectorimg = PIL.ImageGrab.grab(bbox = (xpos - 45, ypos - 50, 90, 50))
  vectorimg = pg.screenshot(region = (xpos - 45, ypos - 50, 90, 50))
  #convert tiny screenshot to b&w then use google tesseract to extract text
  vectortxt = tess.image_to_string(cv2.cvtColor(np.array(vectorimg), cv2.COLOR_BGR2GRAY), lang ='eng')
  print(vectortxt)

  #vars for charge and mass of electron
  q = 1
  m = 1

  #extract angle and accel from the extracted text
  angle = vectortxt[:1]
  accel = vectortxt[1:] * q / m

  #update vel and pos values, need to figure out timelength of one of these loops so i can apropriately add accel and vel
  time = 1

  xpos += xvel * time
  ypos += yvel * time
  
  xvel += accel * math.cos(angle) * time
  yvel -= accel * math.sin(angle) * time

  #actually move mouse to new pos values
  pg.moveTo(xpos)
  pg.moveTo(ypos)