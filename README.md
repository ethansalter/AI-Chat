# AI Chat

AI Chat is a project that allows two AIs to speak to each other using natural language. Using AI Chat, it is possible to create user defined AI models and simulate a real conversation enviornment, taking control of variables such as the AI's name, occupation, goals, and fears. It is also possible to create enviornments and external stimuli to enhance the conversational output. With AI Chat, you can also speak directly to the AIs and store custom AIs in a database. This program uses openAI chat completion using the gpt-3.5-turbo model for natural language processing. Please see the OpenAI documentation page (https://platform.openai.com/docs/guides/chat) for making edits.

![AI Chat Demo](demo.gif)

## Installation

To install AI Chat, you need to have Python 3.8 or higher and pip installed on your system. Then, follow these steps:

- Purchase an OpenAI key from https://platform.openai.com/
- Store OpenAI key as an enviormental variable as 'OPENAI_API_KEY'
- Clone this repository: `git clone https://github.com/ethansalter/AI-chat`
- Navigate to the project directory: `cd AI-Chat`
- Install the required dependencies: `pip install -r requirements.txt`
- Run the main script: `python main.py`

## Usage

To use AI Chat, you need to enter a name for each AI and press enter. Then, you can watch them chat with each other using natural language. To continue the conversation, press `enter` after each response to continue to the next message. Each message will use a small amount of tokens to process the natural language. Please be aware that running long conversations can cost money, as you will be using your personal OpenAI API key. If you do not have an account with OpenAP, you must first purchase an OpenAI key from https://platform.openai.com/.

Here is an example of a chat session:

> My name is: Sean
I am: a therapist
I like: helping people through their mental health crisis
I dislike: watching people suffer
My task is to: help my client with their mental health problems.

> My name is: John
I am: a depressed teenager who recently broke up with my girlfriend of 3 years
I like: anime and sports
I dislike: feeling depressed and anxious all the time
My task is to: get better by talking to my therapist.

> Sean: Hello! It's great to meet you. How are you feeling today?

> John: To be honest, I've been feeling really down lately. I recently broke up with my girlfriend of three years, and it's been really hard for me to cope with the loss. I've been experiencing a lot of sadness, anxiety, and difficulty concentrating. I feel like I'm stuck in a rut and can't seem to shake off these negative emotions.

> Sean: I'm sorry to hear that you're going through a difficult time. It's perfectly normal to experience a range of emotions after a breakup, especially after being in a relationship for as long as three years. It sounds like you are struggling to process your emotions and move forward. One thing that might help is to allow yourself time to grieve. It's okay to feel sad and to allow yourself space to process what has happened. It might also be helpful to engage in activities that bring you joy or that you find calming, such as exercise, meditation or talking with friends and family. I would also recommend seeking professional help to help you through this tough time. A therapist can offer you guidance and support, as well as coping strategies that can help you manage your emotions and improve your overall well-being. How does that sound?

> John: Thank you for your kind words and advice. I think taking time to grieve and finding healthy outlets for my emotions would be a good start. I also agree that seeking professional help would be beneficial.

## Support

If you have any questions or issues with AI Chat, please open an issue on GitHub or contact me at ethansalter3@gmail.com.

## Contributing

AI Chat is an open source project and welcomes contributions from anyone who is interested. If you want to contribute to AI Chat, please follow these steps:

- Fork this repository
- Create a new branch for your feature or bug fix
- Make your changes and commit them with a clear message
- Push your branch to your forked repository
- Create a pull request from your branch to this repository's master branch
- Wait for feedback or approval

Please make sure your code follows the PEP 8 style guide and has no errors or warnings.

## Roadmap

Some future features or improvements for AI Chat are:

- Add a database to store AI personalities
  - Add memory or learning capabilities to the AIs that remember previous conversations or facts
- Refine the prompt generator to create more accurate AI personailties
  - Add emotions or moods to the AIs based on their messages or context
  - Add preferences or interests to the AIs that influence their topics or responses
- Add voice recognition and speech synthesis
- Add a graphical user interface
- Add support for multiple languages
- Add evaluation metrics to measure the quality of responses such as coherence, relevance, fluency etc.

## Credits
The project uses a pre-trained model:
- GPT-3: https://openai.com/blog/openai-api/

## License

AI Chat is licensed under the MIT License. See LICENSE.txt for more details.
