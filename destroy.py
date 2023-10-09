import webbrowser
import pyautogui

url = "https://www.youtube.com/watch?v=AaF_f6KaAQw"


for x in range(12):
    pyautogui.hotkey('ctrl', 'n')
    webbrowser.open_new(url)
    