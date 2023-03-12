import openai
import time
import os
import json

# add your openAI key as an enviornmental variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def ai_ai_chat(ai1, ai2, messageChainAi1=[], messageChainAi2=[]):
    # main chat function, used to initiate crosstalk between two ai models
    if messageChainAi1 == []:
        messageChainAi1.append({"role": "system", "content": ai1.prompt})
        messageChainAi1.append({"role": "user", "content": "Hello "+ai1.name})
    if messageChainAi2 == []:
        messageChainAi2.append({"role": "system", "content": ai2.prompt})
        messageChainAi2.append(
            {"role": "assistant", "content": "Hello "+ai1.name})
    print(">> "+ai1.name+": ", end="")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messageChainAi1
    )
    messageChainAi1.append(
        {"role": "assistant", "content": response["choices"][0]["message"]["content"]})
    messageChainAi2.append(
        {"role": "user", "content": response["choices"][0]["message"]["content"]})
    print(response["choices"][0]["message"]["content"])
    if input() == "quit":
        return 0
    while len(messageChainAi1) > 5:
        messageChainAi1.pop(1)
    while len(messageChainAi2) > 5:
        messageChainAi2.pop(1)
    ai_ai_chat(ai2, ai1, messageChainAi2, messageChainAi1)

def ai_user_chat(ai1, messageChainAi1=[]):
    # secondary chat function, used to initiate chat between an ai model and the user
    if messageChainAi1 == []:
        messageChainAi1.append({"role": "system", "content": ai1.prompt})
        messageChainAi1.append({"role": "user", "content": "Hello "+ai1.name})
    print(chr(10)+">> "+ai1.name+": ", end="")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messageChainAi1
    )
    messageChainAi1.append(
        {"role": "assistant", "content": response["choices"][0]["message"]["content"]})
    
    print(response["choices"][0]["message"]["content"]+chr(10))
    userInput= input(">> User: ")
    if userInput == "quit":
        return 0
    messageChainAi1.append(
        {"role": "user", "content": userInput})
    
    while len(messageChainAi1) > 5:
        messageChainAi1.pop(1)
    ai_user_chat(ai1, messageChainAi1)

class ai:
    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt

def ai_new():
    # prompt engineering for user customized AI
    print("Please fill out the following questionnaire to create your AI. Answer the questions as if you are the AI.")
    name = input("My name is: ")
    title = input("I am: ")
    like = input("I like: ")
    dislike = input("I dislike: ")
    task = input("My task is to: ")
    print("Creating AI...")
    time.sleep(2)
    print(f"{name} created!")
    while True:
        userInput = input("Would you like to save this AI? (y/n)")
        if userInput == 'y':
            saveAs=input("Save as?: ")
            data = {
                "name": name,
                "title": title,
                "like": like,
                "dislike": dislike,
                "task": task
            }
            ai_save(saveAs, data)
            break
        if userInput == 'n':
            break
    return 0

def ai_save(name, data):
    with open(os.path.join(os.path.dirname(__file__), "personas.json"), 'r+') as jsonfile:
        # First we load existing data into a dict.
        personas = json.load(jsonfile)
        # Join new_data with file_data inside personas
        personas[name] = data
        # Sets file's current position at offset.
        jsonfile.seek(0)
        # convert back to json.
        json.dump(personas, jsonfile, indent=4)
        print(f"{name} saved successfully!")
        time.sleep(1)
        return 0

def ai_delete():
    try:
        with open(os.path.join(os.path.dirname(__file__), "personas.json"), 'r+') as jsonfile:
            # First we load existing data into a dict.
            personas = json.load(jsonfile)
        AIRetrieveList = ', '.join(personas.keys())
        persona = input(f"Choose a model. ({AIRetrieveList}): ")
        if persona in personas.keys():
            while True:
                userInput = input(f"Are you sure you want to delete {persona}? This cannot be undone. (y/n)")
                if userInput =='y':
                    del personas[persona]
                    break
                if userInput =='n':
                    print("Cancelled. Returning to menu.")
                    time.sleep(1)
                    return 0
        else:
            print("Name not found. Returning to menu.")
            time.sleep(1)
            return 0
        with open(os.path.join(os.path.dirname(__file__), "personas.json"), 'w') as jsonfile:
            json.dump(personas, jsonfile, indent = 4)
            print(f"{persona} deleted successfully!")
            time.sleep(1)
            return 0
    except:
        input("Error reading file. Please reinstall program and or check for json file existance.")
        quit()
    
def ai_load():
    # loads a saved AI from the personas.json file
    try:
        with open(os.path.join(os.path.dirname(__file__), "personas.json"), 'r') as jsonfile:
            # First we load existing data into a dict.
            personas = json.load(jsonfile)
            AIRetrieveList = ', '.join(personas.keys())
    except:
        input("Error reading file. Please reinstall program and or check for json file existance.")
        return 0
    while True:
        persona = input(f"Choose a model. ({AIRetrieveList}): ")
        if persona in personas.keys():
            name = personas[persona]["name"]
            title = personas[persona]["title"]
            like = personas[persona]["like"]
            dislike = personas[persona]["dislike"]
            task = personas[persona]["task"]
            prompt = f"Your task is to act like you are a {title} named {name}. You like {like}. You dislike {dislike}. Your task is to {task}."
            return ai(name, prompt)
        print("Name not found. Returning to menu.")
        time.sleep(1)
        return 0      

def home_screen_1():
    while True:
            print(100*chr(10))
            print("""-- AI Chat --
Welcome to AI Chat!
Press 1 to create a new AI
Press 2 to delete a saved AI
Press 3 to begin a conversation between saved AIs
Press 4 to speak with to a saved AI""")
            userInput = input("")
            if userInput == "1":
                print(100*chr(10))
                ai_new()
            if userInput == "2":
                print(100*chr(10))
                ai_delete()   
            if userInput == "3":
                print(100*chr(10))
                ai_ai_chat(ai_load(), ai_load())
            if userInput == "4":
                print(100*chr(10))
                ai_user_chat(ai_load())

home_screen_1()
