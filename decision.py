class DecisionEngine:

    def decide(self, state):

        task = state.get_task().lower()

        if task.startswith("remember"):
            return "SAVE_MEMORY"

        elif "last question" in task:
            return "GET_PREVIOUS_QUESTION"
        
        elif "what did i just say" in task:
            return "GET_LAST_USER_MESSAGE"

        elif "what was your last reply" in task:
            return "GET_LAST_ASSISTANT_MESSAGE"

        elif task.startswith("what is my"):
            return "RECALL_MEMORY"


