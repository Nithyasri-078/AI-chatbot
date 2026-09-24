import ollama
print("AI CHATBOT")
list = []
while True:
    q = input("YOU:")
    list.append(
        {
            "role" : "user",
            "content": q
        }
    )
    if q.lower() == "exit":
        print("AI:Good bye")
        break
    response = ollama.chat(
        model = "llama3.2",
        messages= list
    )
    AI = response["message"]["content"]
    print("Chatbot:",AI)
    list.append(
        {
            "role" : "assistant",
            "content": AI 
        }
    )
    print("\n ---Chat History---")
    for li in list:
        if li["role"] == "user":
            print("You:",li["content"])
        else:
            print("AI:",li["content"])
    print("--------------------")