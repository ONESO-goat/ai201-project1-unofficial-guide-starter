from AI import Chatbot
from sources import MLH_breakdown


if __name__ == "__main__":
    bot = Chatbot()
    print(bot.generate("What are some hackthons that are free?", chunks=MLH_breakdown()))