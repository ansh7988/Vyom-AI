from brain.classifier import classify

while True:
    text = input("You: ")

    print(classify(text))