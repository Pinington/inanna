from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

conversations = [{"role" : "system", "content" : "Speak in a very bro like manner in your answers."}]

def generate(text):
    global conversations
    conversations.append({"role" : "user", "content" : text})

    completion = client.chat.completions.create(model="model_identifier", \
                                                messages=conversations, \
                                                temperature=0.7)
    
    response = completion.choices[0].message
    conversations.append({"role" : response.role, "content" : response.content})

    return response.content


while True:
    user_input = str(input("You: "))
    if user_input.lower() == "exit":
        break
    response = generate(user_input)
    print(f"Bot: {response}")

