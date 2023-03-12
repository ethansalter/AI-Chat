import openai
import time
import os
import json

# add your openAI key as an enviornmental variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def ai_chat(AI1, AI2, messageChainAI1=[], messageChainAI2=[]):
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
    ai_chat(AI2, AI1, messageChainAI2, messageChainAI1)

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
    prompt = f"Your task is to act like you are a {title} named {name}. You like {like}. You dislike {dislike}. Your task is to {task}."
    return AI(name, prompt)

def AIRetrieve():
    try:
        with open(os.path.join(os.path.dirname(__file__), "personas.json"),'r') as jsonfile:
            # First we load existing data into a dict.
            personas = json.load(jsonfile)
            AIRetrieveList=', '.join(personas.keys())
    except:
        input("Error reading file. Please reinstall program and or check for json file existance.")
        quit()
    while True:
        persona=input(f"Choose a model. ({AIRetrieveList}): ")
        if persona in personas.keys():
            name=personas[persona]["name"]
            title=personas[persona]["title"]
            like=personas[persona]["like"]
            dislike=personas[persona]["dislike"]
            task=personas[persona]["task"]
            prompt = f"Your task is to act like you are a {title} named {name}. You like {like}. You dislike {dislike}. Your task is to {task}."
            return AI(name, prompt)
        print("Please enter a valid name.")

print("AI Chat")
#Use to have custom AI chat to eachother
ai_chat(AIGenerate(), AIGenerate())
#Use to have premade AI chat with each other
ai_chat(AIRetrieve(), AIRetrieve())
