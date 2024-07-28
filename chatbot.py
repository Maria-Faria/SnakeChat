from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("SnakeBot")

conversation = [
    "Oi",
    "Mensagem automática enviada pelo SnakeBot Python"
    "Tudo tranquilo?",
    "Tranquilo",
    "Terminou AWS?",
    "Eu não, e vc?",
    "Claro que não",
    "Decepcionante",
    "Eu sei"
]

#trainer = ListTrainer(chatbot)
#trainer.train(conversation)

while True:
    message = input("Mande uma mensagem para o chatbot: ")

    if message == "tchau":
        break

    response = chatbot.get_response(message)
    print(response)