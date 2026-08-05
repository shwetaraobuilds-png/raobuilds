import anthropic

client = anthropic.Anthropic()

conversation = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Claude: Goodbye!")
        break

    conversation.append({
        "role": "user",
        "content": user_input
    })

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=300,
        messages=conversation
    )

    assistant_answer = response.content[0].text

    print("Claude:", assistant_answer)

    conversation.append({
        "role": "assistant",
        "content": assistant_answer
    })
