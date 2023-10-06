import time
import pyautogui

number_of_cards = 537
counter = 0
time.sleep(4)

# Move cursor to the list in Anki fullscreen
pyautogui.moveTo(444, 108)
time.sleep(0.2)
pyautogui.click()

while counter < number_of_cards:

    # Move cursor to the list in Anki fullscreen
    pyautogui.moveTo(1016, 82)
    time.sleep(1)
    pyautogui.click()

    time.sleep(4)
    # Move cursor to the button in the Forvo add-in
    pyautogui.moveTo(920, 364)
    time.sleep(1)
    pyautogui.click()

    time.sleep(1.5)
    # Move cursor cancel a possible error message: small error window if no sound was found
    pyautogui.moveTo(752, 373)
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(1)
    # Move cursor cancel a possible error message: Big error window if a problem occured
    pyautogui.moveTo(508, 280)
    time.sleep(0.2)
    pyautogui.click()

    # Time between clicking the Forvo sound and pushing down
    time.sleep(4)

    # Anki's full window mode has 40 entries per page. If we are not on the last page, we can just click on the next
    if counter <= 40:
        pyautogui.moveTo(444, 108+(counter+1)*23)
        time.sleep(1)
        pyautogui.click()

    else:
        pyautogui.moveTo(444, 944)
        time.sleep(1)
        pyautogui.click()
        # Press the down arrow key
        pyautogui.press('down')

    counter += 1