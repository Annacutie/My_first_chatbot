from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 

#crate a new chat bot

chatbot = ChatBot('my first chat bot', storage_adapter = 'chatterbot.storage.SQLStorageAdapter', logic_adapter = ['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.TimeLogicAdapter', 'chatterbot.logic.BestMatch'] ,database_uri = 'sqlite:///database.db')

trainer = ListTrainer(chatbot)

trainer.train(['can I help you find a book? ', 'Shure I would like to find a book', 'Your book has been chosen.'])
# getting a responce
print('Type something to begin')
while True:
    try:
        user_input = input('>')
        response = chatbot.get_response(user_input)
        print(response)

    except(KeyboardInterrupt, SystemExit, EOFError):
        break
        
