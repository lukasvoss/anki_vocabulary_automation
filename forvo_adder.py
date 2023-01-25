import time
import pyautogui

number_of_cards = 4
counter = 0
time.sleep(4)

# Move cursor to the list in Anki fullscreen
pyautogui.moveTo(1044, 158)
time.sleep(0.2)
pyautogui.click()

while counter < number_of_cards:

    # Move cursor to the list in Anki fullscreen
    pyautogui.moveTo(974, 204)
    time.sleep(1)
    pyautogui.click()

    time.sleep(4)
    # Move cursor to the button in the Forvo add-in
    pyautogui.moveTo(880, 304)
    time.sleep(1)
    pyautogui.click()

    time.sleep(1)
    # Move cursor cancel a possible error message: small error window if no sound was found
    pyautogui.moveTo(606, 365)
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(1)
    # Move cursor cancel a possible error message: Big error window if a problem occured
    pyautogui.moveTo(470, 224)
    time.sleep(0.2)
    pyautogui.click()

    # Time between clicking the Forvo sound and pushing down
    time.sleep(4)

    pyautogui.moveTo(1044, 158)
    time.sleep(1)
    pyautogui.click()
    # Press the down arrow key
    pyautogui.press('down')

    counter += 1