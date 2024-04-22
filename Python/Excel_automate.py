import pyautogui
import time

# Delay to give time to switch to the target window
time.sleep(2)

# Loop
for i in range(181, 501):
    pyautogui.click(x=42, y=236)
    time.sleep(0.5)

    pyautogui.typewrite(f"A{i}:A500")
    time.sleep(1.5)
    
    pyautogui.press('enter')
    time.sleep(1.5)

    # Delay before pressing Cmd+X to ensure clipboard content is fully copied
    time.sleep(1.5)

    pyautogui.hotkey('command', 'x')
    time.sleep(1.5)

    pyautogui.press('up')
    time.sleep(1.5)

    # Delay before pressing Cmd+V to ensure clipboard content is fully copied
    time.sleep(0.5)
    
    pyautogui.hotkey('command', 'v')
    time.sleep(1.5)