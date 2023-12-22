import pyautogui

COUNTER_FNAME = ".cnt"

def load_counter(fname):
    try:
        return len(open(fname,'a').readlines())
    except:
        return 0
    return 0    

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'123.png')

