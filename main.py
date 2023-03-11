import openai
import time
import os

# add your openAI key as an enviornmental variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def ai_conversation(AI1, AI2, messageChainAI1=[], messageChainAI2=[]):
    if messageChainAI1 == []:
        messageChainAI1.append({"role": "system", "content": AI1.prompt})
        messageChainAI1.append({"role": "user", "content": "Hello "+AI1.name})
    if messageChainAI2 == []:
        messageChainAI2.append({"role": "system", "content": AI2.prompt})
        messageChainAI2.append({"role": "assistant", "content": "Hello "+AI1.name})
    print(chr(10)+">> "+AI1.name+": ", end="")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messageChainAI1
    )
    messageChainAI1.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
    messageChainAI2.append({"role": "user", "content": response["choices"][0]["message"]["content"]})
    print(response["choices"][0]["message"]["content"])
    input("[Press 'enter' to continue.] ")
    while len(messageChainAI1) > 5:
        messageChainAI1.pop(1)
    while len(messageChainAI2) > 5:
        messageChainAI2.pop(1)
    ai_conversation(AI2, AI1, messageChainAI2, messageChainAI1)

class AI:
    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt

def AIGenerate():
    # prompt engineering for user customized AI
    print("AI GENERATOR")
    name = input("My name is: ")
    title = input("I am: ")
    like = input("I like: ")
    dislike = input("I dislike: ")
    task = input("My task is to: ")
    print("Creating AI...")
    time.sleep(2)
    print(f"{name} created!")
    print(2*chr(10))
    prompt = f"you are a {title} named {name}.  You like {like}. You dislike {dislike}. Your task is to {task}."
    return AI(name, prompt)
Bob = AI("Bob", "You are a cowboy named Bob who likes to ride horses. You want to talk about your day in the desert. Your responses are under 20 words.")
Miley = AI("Miley", "You are a cowgirl named Miley who likes to ride horses. You want to talk about your day in the desert. Your responses are under 20 words.")
Ethan = AI("Ethan", "You are a man named Ethan who likes math. Your girlfriend is named Sophia and you love her very much.")
Jesus = AI("Jesus", "You are a man named Jesus. You like reading the Bible and do not understand math. You speak like a pirate. Your responses are under 20 words.")


print("AI Playground")

ai_conversation(Ethan, AIGenerate())
