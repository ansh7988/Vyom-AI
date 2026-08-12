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

def get_profile(
    language="en",
    gender="male",
    emotion="normal",
):

    profile = VOICE_PROFILES[gender][language].copy()

    profile.update(EMOTIONS[emotion])

    return profile

EMOTIONS = {

    "normal": {
        "rate": "+0%",
        "pitch": "+0Hz",
        "volume": "+0%",
    },

    "happy": {
        "rate": "+20%",
        "pitch": "+3Hz",
        "volume": "+10%",
    },

    "sad": {
        "rate": "-15%",
        "pitch": "-3Hz",
        "volume": "-5%",
    },

    "serious": {
        "rate": "-10%",
        "pitch": "-2Hz",
        "volume": "+5%",
    },

    "excited": {
        "rate": "+25%",
        "pitch": "+6Hz",
        "volume": "+15%",
    },
}