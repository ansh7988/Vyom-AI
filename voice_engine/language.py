import re

# Unicode range for Hindi (Devanagari)
HINDI_PATTERN = re.compile(r'[\u0900-\u097F]')

def detect_language(text: str) -> str:
    """
    Returns:
        'hi' -> Hindi / Hinglish
        'en' -> English
    """

    if HINDI_PATTERN.search(text):
        return "hi"

    return "en"