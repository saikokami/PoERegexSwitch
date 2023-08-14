# PoERegexSwitch

PoERegexSwitch is a tool designed to enhance the item search experience for Path of Exile players by allowing them to configure custom regular expressions for in-game NPCs. These custom regex patterns can be tailored to your individual preferences and help you quickly identify specific items in the in-game shop.

## How It Works

1. **Clone or download the repository to your local machine.**

2. **Configure the custom regular expressions:**
   Open the `main.py` file and modify the `npc_patterns` dictionary. Add your own regular expressions for each NPC following this format:
   
   ```python
   npc_patterns = {
       "Clarissa": r"Pattern for Clarissa's items",
       "Hargan": r"Pattern for Hargan's items"
       # Add more NPCs and patterns as needed
   }
   ```

3. **Run the tool:**
   Execute the `main.py` script using Python, and it will monitor the in-game text using OCR (Optical Character Recognition) on the specified screen region for each NPC. If the recognized text matches any of the configured regular expressions, the corresponding action will be triggered.

4. **Improved item searches:**
   As you interact with NPCs in Path of Exile, the tool will automatically recognize their items based on your custom regex patterns. This streamlined process will help you find items more efficiently in the shop.

## Requirements

- Python 3.x
- pytesseract
- pyperclip
- win32clipboard (for Windows users)

## Getting Started

1. **Install the required Python packages:**
   ```
   pip install pytesseract pyperclip pywin32
   ```

2. **Clone or download this repository.**

3. **Configure your custom regular expressions in the `main.py` file.**

4. **Run the tool:**
   ```
   python main.py
   ```

## Disclaimer

This tool is intended for personal use and experimentation. Be mindful that it relies on Optical Character Recognition and may require adjustments based on your display settings, text font, and in-game environment.

Feel free to contribute to this repository by sharing your custom regex patterns, improving the code, or suggesting enhancements.

Happy item hunting in Path of Exile!
