from brain.state import VyomState
from brain.decision import DecisionEngine

state = VyomState()
decision = DecisionEngine()

print("=" * 40)
print("      Decision Engine Test")
print("=" * 40)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    state.set_task(user_input)

    action = decision.decide(state)

    print(f"Decision -> {action}")