import tkinter as tk
from PIL import ImageGrab
import pytesseract
import time
import win32clipboard


npc_patterns = {
    "clarrisa": "ABC",
    "hargan": "r-r-|-r-r|r-.-r",
    "yeena": "b-b-g|b-g-b|g-b-b|nne|rint"
}

def regexToClipBoard(text):
    return npc_patterns.get(text, text)

def update_clipboard_win32(new_text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(new_text)
    win32clipboard.CloseClipboard()

def ocr_loop():
    while True:
        x1, y1, x2, y2 = (screen_width - 150) // 2, 0, (screen_width + 150) // 2, 35
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        text = pytesseract.image_to_string(screenshot).lower().strip()
        
        if text in npc_patterns:
            updated_text = regexToClipBoard(text)
            update_clipboard_win32(updated_text)
        time.sleep(1)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

root = tk.Tk()
root.overrideredirect(True)
screen_width = root.winfo_screenwidth()

ocr_loop()
