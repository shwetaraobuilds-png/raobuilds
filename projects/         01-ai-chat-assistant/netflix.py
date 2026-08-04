import anthropic;

client = anthropic.Anthropic();

message = client.messages.create(
model="claude-sonnet-4-5",
max_tokens=300,

messages=[{

"role" : "user",
"content" : "What is collaborative filtering?"

}]

)

print("collaborative filtering")

print(message.content[0].text)
