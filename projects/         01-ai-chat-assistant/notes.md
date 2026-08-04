#Day 1 

Called Anthropic API simple API using python. 

What is the difference between a Message, a TextBlock, and a string?
- A message is anthropic object, which fetch the response from the anthropic API. 
- One piece of Claude's generated content. The Message stores its responses as a list of content blocks, and each block contains information such as the generated text.
- String is characters 


Why doesn't Claude remember previous API calls?
- Claude is stateless. Every API request is independent. If we want Claude to remember earlier messages, our application must resend the conversation history with each new request.

Why does the application have to send the conversation history?
Since Claude does not remember previous API calls, the application is responsible for maintaining the conversation history and sending it with every request. 
This allows Claude to answer based on the current conversation rather than treating each request independently.


What surprised me the most today?

- When hitting a API through postman, sometimes it takes days to get the response. Through the claude & Python, the request was achieved in few minutes. 
- It is facinating how it is remembering the history and replying to the answers just by few line of code. 
