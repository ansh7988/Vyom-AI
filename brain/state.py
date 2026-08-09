class VyomState:

    def __init__(self):
        self.current_task = None
        self.current_mode = "CHAT"
        self.last_response = None
        self.user_intent = None

    def set_task(self, task):
        self.current_task = task

    def get_task(self):
        return self.current_task

    def set_mode(self, mode):
        self.current_mode = mode

    def get_mode(self):
        return self.current_mode

    def set_last_response(self, response):
        self.last_response = response

    def get_last_response(self):
        return self.last_response


    def set_intent(self, intent):
        self.user_intent = intent

    def get_intent(self):
        return self.user_intent