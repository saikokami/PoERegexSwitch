import tkinter as tk
from PIL import ImageGrab
import pytesseract
import time
import win32clipboard

# Define constants
SCREEN_WIDTH = None  # Will be assigned later
UPDATE_INTERVAL = 1 # Interval in seconds for the OCR loop

# NPC regex patterns - TODO: Check if some are wrong or missing
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

def regexToClipboard(text):
    return npc_patterns.get(text, text)

def updateClipboardWin32(new_text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(new_text)
    win32clipboard.CloseClipboard()

def performOCR():
    # Define the coordinates for the OCR screenshot
    # Dunno if this works for resolutions != 1920x1080
    x1, y1, x2, y2 = (SCREEN_WIDTH - 150) // 2, 0, (SCREEN_WIDTH + 150) // 2, 35
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    text = pytesseract.image_to_string(screenshot).lower().strip()

    if text in npc_patterns:
        updated_text = regexToClipboard(text)
        updateClipboardWin32(updated_text)

def startOCRLoop():
    while True:
        performOCR()
        time.sleep(UPDATE_INTERVAL)  # Wait for 1 second before the next OCR

def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    root = tk.Tk()
    root.overrideredirect(True)
    global SCREEN_WIDTH
    SCREEN_WIDTH = root.winfo_screenwidth()

    startOCRLoop()

if __name__ == "__main__":
    main()
