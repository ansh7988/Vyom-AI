class SpeechRequest:

    def __init__(
        self,
        text,
        profile,
        priority="normal",
        emotion="normal",
        interrupt=False,
    ):

        self.text = text
        self.profile = profile
        self.priority = priority
        self.emotion = emotion
        self.interrupt = interrupt