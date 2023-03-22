import openai
import openai_sk as key
openai.api_key = key.api

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    response = generate_response(user_input)
    print("ChatGPT: ", response)