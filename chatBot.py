from chatterbot import ChatBot
bot = ChatBot("Ron Obvious")
from chatterbot.trainers import ListTrainer

chats = ['oi', 'ola', 'tudo bom?', 'tudo e voce?', 'estou bem obrigado.']

trainer = ListTrainer(bot)

trainer.train(chats)

while True:
    quest = input('Voce: ')

    response = bot.get_response(quest)

    print('Bot: ', response)

