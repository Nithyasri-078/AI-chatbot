import ollama
print("AI CHATBOT")
while True:
    q = input("YOU:")
    if q.lower() == "exit":
        print("AI:Good bye")
        break
    response = ollama.chat(
        model = "llama3.2",
        messages=[
            {
                "role" : "user",
                "content": q
            }
        ]
    )
    print("AI:", response["message"]["content"])