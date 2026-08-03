VOICE_PROFILES = {

    "male": {

        "en": {
            "voice": "en-US-GuyNeural",
            "rate": "+0%",
            "pitch": "+0Hz",
            "volume": "+0%",
        },

        "hi": {
            "voice": "hi-IN-MadhurNeural",
            "rate": "+0%",
            "pitch": "+0Hz",
            "volume": "+0%",
        },
    },

    "female": {

        "en": {
            "voice": "en-US-AriaNeural",
            "rate": "+0%",
            "pitch": "+0Hz",
            "volume": "+0%",
        },

        "hi": {
            "voice": "hi-IN-SwaraNeural",
            "rate": "+0%",
            "pitch": "+0Hz",
            "volume": "+0%",
        },
    },
}

def get_profile(language="en", gender="male"):
    return VOICE_PROFILES[gender][language]