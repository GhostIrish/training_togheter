import pyautogui

pyautogui.PAUSE = 1
# list of full keyboard keys this lib accept -> pyautogui.KEYBOARD_KEYS

text = '''
----------------------------------------------------------------------------------------------------

This is my first attempt to using pyautogui for automate every process in my pc, 
sorry for the privacy invasion, but i need to show you my knowledgements, thanks for attention :)

----------------------------------------------------------------------------------------------------
'''


pyautogui.typewrite(['win'])
pyautogui.typewrite('notes')
pyautogui.typewrite(['enter'])
pyautogui.hotkey('ctrl', 'n')
pyautogui.typewrite(text, interval=0.08)
