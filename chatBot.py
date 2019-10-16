from chatterbot import ChatBot
bot = ChatBot("Test")#,read_only=True)  <- read to stop training the bot
from chatterbot.trainers import ListTrainer

chats = ['oi', 'ola', 'tudo bom?', 'tudo e voce?', 'estou bem obrigado.'] # chats

trainer = ListTrainer(bot) # training

trainer.train(chats) # training with the chats

while True:
    quest = input('You: ') 

    response = bot.get_response(quest) # bot response

    print('Bot: ', response) 

# author: Valtercio Junior
