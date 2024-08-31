import os
import sys
import cv2
import numpy as np
import pyautogui
import time

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
REGION_WIDTH, REGION_HEIGHT = 387, 685
LEFT = (SCREEN_WIDTH - REGION_WIDTH) // 2
TOP = (SCREEN_HEIGHT - REGION_HEIGHT) // 2

flower_templates = [cv2.imread(os.path.join(base_path, f'flower_template_{i}.png'), 0) for i in range(1, 6)]
ice_templates = [cv2.imread(os.path.join(base_path, f'ice_template_{i}.png'), 0) for i in range(1, 3)]
bomb_templates = [cv2.imread(os.path.join(base_path, f'bomb_template_{i}.png'), 0) for i in range(1, 3)]
play_button_template = cv2.imread(os.path.join(base_path, 'play_button_template.png'), 0)
home_template = cv2.imread(os.path.join(base_path, 'home.png'), 0)
play_home_template = cv2.imread(os.path.join(base_path, 'play_home.png'), 0)

def capture_screen(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    return screenshot_gray

def find_template_position(templates, screenshot_gray, threshold=0.8):
    if isinstance(templates, list):
        for template in templates:
            if template is None or template.shape[0] > screenshot_gray.shape[0] or template.shape[1] > screenshot_gray.shape[1]:
                continue
            
            result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val >= threshold:
                return (max_loc, template.shape)
    else:
        if templates is None or templates.shape[0] > screenshot_gray.shape[0] or templates.shape[1] > screenshot_gray.shape[1]:
            return None
        
        result = cv2.matchTemplate(screenshot_gray, templates, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            return (max_loc, templates.shape)

    return None

def click_position(position, offset=(LEFT, TOP)):
    (max_loc, template_shape) = position
    x, y = max_loc
    pyautogui.click(x + template_shape[1] // 2 + offset[0], y + template_shape[0] // 2 + offset[1])

def click_center_screen():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.click(center_x, center_y)

def scroll_down():
    pyautogui.scroll(-5000)

print("Application is running...")

while True:
    screenshot_gray = capture_screen((LEFT, TOP, REGION_WIDTH, REGION_HEIGHT))
    home_position = find_template_position(home_template, screenshot_gray)
    if home_position:
        scroll_down()
        time.sleep(1)
        play_home_position = find_template_position(play_home_template, screenshot_gray)
        if play_home_position:
            click_position(play_home_position)
        continue 
    
    ice_position = find_template_position(ice_templates, screenshot_gray)
    if ice_position:
        click_position(ice_position)
        continue
    
    bomb_position = find_template_position(bomb_templates, screenshot_gray, threshold=0.9)
    if not bomb_position:
        flower_position = find_template_position(flower_templates, screenshot_gray)
        if flower_position:
            click_position(flower_position)
    
    play_button_position = find_template_position(play_button_template, screenshot_gray)
    if play_button_position:
        click_center_screen()
        click_position(play_button_position)
