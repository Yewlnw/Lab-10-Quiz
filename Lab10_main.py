import pyautogui, sys
import keyboard
import mss
import cv2
import numpy
from time import time, sleep

pyautogui.PAUSE = 0
pause = False
keyboard.wait('s')
sct = mss.mss()
dimensions_focus = {
        'left': 0,
        'top': 0,
        'width': 180,
        'height': 180
    }

c1_b = cv2.imread('1cactus_b.jpg')
c1_s = cv2.imread('1cactus_s.jpg')
try:
    while True:
        x, y = pyautogui.position()
        
        dimensions_focus['left']=x
        dimensions_focus['top']=y
        scr = numpy.array(sct.grab(dimensions_focus))

        scr_remove = scr[:,:,:3]
        result = cv2.matchTemplate(scr_remove, c1_s, cv2.TM_CCOEFF_NORMED)
        _, max_val1, _, max_loc1 = cv2.minMaxLoc(result)
        result = cv2.matchTemplate(scr_remove, c1_b, cv2.TM_CCOEFF_NORMED)
        _, max_val2, _, max_loc2 = cv2.minMaxLoc(result)
        #print(f"Max Val: {max_val5} Max Loc: {max_loc5}\t")

        if (max_val1 > .75)or((max_val2 > .75)):
            pyautogui.press('up')
        
        src = scr.copy()
        cv2.imshow('Screen Focus', scr)
        cv2.resizeWindow("Screen Focus", 300, 300)
        
        cv2.waitKey(1)
        sleep(.05)
        if keyboard.is_pressed('q'):
            break
            
except KeyboardInterrupt:
    print('\n')
