import anthropic

client = anthropic.Anthropic()

# --------------------------
# First API Call
# --------------------------

first_message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": "Explain recommendation systems."
        }
    ]
)

first_answer = first_message.content[0].text

print("FIRST RESPONSE")
print(first_answer)

print("\n" + "="*60 + "\n")

# --------------------------
# Second API Call
# --------------------------

second_message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": "Explain recommendation systems."
        },
        {
            "role": "assistant",
            "content": first_answer
        },
        {
            "role": "user",
            "content": "Can you give me an e-commerce example?"
        }
    ]
)

print("SECOND RESPONSE")
print(second_message.content[0].text)
