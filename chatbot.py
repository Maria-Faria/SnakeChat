from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("SnakeBot")

conversation = [
    "Opa",
    "E aí, tranquilo?",
    "Tranquilo",
    "Terminou AWS?",
    "Eu não, e vc?",
    "Claro que não",
    "Decepcionante",
    "Eu sei"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)