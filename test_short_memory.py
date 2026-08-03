from brain.short_memory import ShortMemory

memory = ShortMemory()

# Clear old data
memory.clear()

# Add some messages
memory.remember("user", "Hello Vyom")
memory.remember("assistant", "Hello Anshdeep!")
memory.remember("user", "How are you?")

# Print memory
print(memory.recall())