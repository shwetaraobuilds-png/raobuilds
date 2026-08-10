import anthropic

client = anthropic.Anthropic()

system = """
You are an history Coach dont answer any other question rather than history.
...
"""


conversation = []


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Claude: Goodbye!")
        break



    if not user_input.strip():
        continue





    # Add the user's message first
    conversation.append({
        "role": "user",
        "content": user_input
    })

    # Now conversation has at least one message
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=300,
        system=system,
        messages=conversation
    )

    assistant_answer = response.content[0].text

    print("Claude:", assistant_answer)
    print("Input Tokens:", response.usage.input_tokens)
    print("Output Tokens:", response.usage.output_tokens)

    # Save Claude's answer for the next turn
    conversation.append({
        "role": "assistant",
        "content": assistant_answer
    })
