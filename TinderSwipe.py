from pyautogui import *
import time
'''
TinderSwipe:
size() returns x, y
PAUSE = int
FAILSAFE = boolean
moveTo(x,y,duration = int)
moveRel(horizontal,vertical,duration = int)
position() returns current coords x, y
click(x,y,button = 'left, middle, right')
doubleClick()
rightClick()
mouseDown()
mouseUp()
dragTo(horizontal,vertical,duration = int)
dragRel(horizontal,vertical,duration = int)
scroll(int)
screenshot("img.png")
typewriter(String)
typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
keyDown(String)
keyUp(String)
confirm()
alert("Displays this alert")

'''
def TinderSwipe():
    try:
        width, height = size()
        moveTo(width//2, height//2)
        midX, midY = position()
        swipes = 0
        while True:
            dragRel(200, 0, duration=.5)
            moveTo(midX,midY)
            time.sleep(1)
            swipes+=1

    except FailSafeException:
        print("Mouse moved to upper left corner: Fail Safe in place.")
    except KeyboardInterrupt:
        print("Keyboard Interruption")

def main():
    TinderSwipe()

if __name__ == '__main__':
    main()