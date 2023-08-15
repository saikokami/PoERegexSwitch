import tkinter as tk
from PIL import ImageGrab
import pytesseract
import time
import win32clipboard


npc_patterns = {
    "nessa": "regexHere",  # Act 1
    "tarkleigh": "regexHere",  # Act 1
    "greust": "regexHere",  # Act 2
    "yeena": "regexHere",  # Act 2
    "clarissa": "regexHere",  # Act 3
    "hargan": "regexHere",  # Act 3
    "siosa": "regexHere",  # Act 3
    "kira": "regexHere",  # Act 4
    "petarus and vanja": "regexHere",  # Act 4
    "lani": "regexHere",  # Act 5
    "utula": "regexHere",  # Act 5
    "bannon": "regexHere",  # Act 5
    "bestel": "regexHere",  # Act 6
    "lilly roth": "regexHere",  # Act 6
    "helena": "regexHere",  # Act 7
    "irasha": "regexHere",  # Act 9
    "weylam roth": "regexHere",  # Act 10
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
