from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('ChatBot')

first_chat = ['Oi', 'Olá', 
            'Tudo bem?', 'Tudo ótimo', 
]
bot.set_trainer(ListTrainer)
bot.train(first_chat)

exit_condition = ('exit')
while True:
    query = input("[Me] <<  ")

    if query in exit_condition:
        break

    response = bot.get_response(query)
    if float(response.confidence) > 0.5:
        print(f'[Bot] 🤗 >>  {response}')
    else:
        print('[Bot] 🤗 >> Desculpe, ainda não sei falar sobre isso!')