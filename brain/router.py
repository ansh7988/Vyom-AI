def detect_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in [
        "open",
        "launch",
        "start"
    ]):
        return "COMMAND"

    if any(word in text for word in [
        "remember",
        "forget"
    ]):
        return "MEMORY"

    if any(word in text for word in [
        "search",
        "find"
    ]):
        return "SEARCH"

    return "CHAT"