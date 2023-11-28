import pyautogui
import json
import time

# venv\Scripts\activate.bat - для Windows;
# source venv/bin/activate - для Linux и MacOS.

def write_cfg(coord):
    with open("config.json", "w+") as cfg_file:
        json.dump (coord, cfg_file)

def read_cfg():
    try:
        with open("config.json", "r") as cfg_file:
            return json.load(cfg_file)
    except:
        return None
        
def calibration():
    coord = []

    for i in range(5):
        print(f'Enter coordinates and press enter')
        input()
        coord.append(pyautogui.position()) 
    
    write_cfg (coord)

def work():
    coord = read_cfg()
    while True:
        i = 0
        for x,y in coord:
            print(f"coord {x} {y}")
            pyautogui.moveTo(x=x,y=y)

            if i==2:
                pyautogui.mouseDown()
            elif i==3:
                pyautogui.mouseUp()
            else:
                pyautogui.click(x=x, y=y)

            i+=1
            

        time.sleep(60 * 3)


def main():
    pyautogui.PAUSE = 5
    pyautogui.FAILSAFE = True

    print('Enter mode:')
    print('1. Calibration.')
    print('2. Work.')

    mode = input()

    if mode == '1':
        calibration()
    elif mode == '2':
        work()
    else :
        pass

if __name__ == "__main__":
    main()