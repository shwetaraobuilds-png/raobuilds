import anthropic

client = anthropic.Anthropic()

first_message= client.messages.create(
model= "claude-sonnet-4-5",
max_tokens=300,
messages =[{
"role":"user",
"content":"Explain What is collaborative filtering?"

}]

)

print("first_message")

print(first_message.content[0].text)

first_answer= first_message.content[0].text


second_message= client.messages.create(
model= "claude-sonnet-4-5",
max_tokens= 300,
messages=[{
"role":"user",
"content":"Explain What is collaborative filtering?"},

{"role":"assistant",
"content":first_answer
},

{
"role":"user",
"content":"can you give me example with respect to Netflix"
}
])

print("second_message")
 
print(second_message.content[0].text)

print(type(first_message))
print(type(second_message))
print(type(second_message.content))
print(type(second_message.content[0]))




