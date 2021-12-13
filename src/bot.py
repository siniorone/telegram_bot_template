import os

import telebot
from emoji import demojize, emojize
from loguru import logger

from src.utils.constant import keyboards
from src.utils.io import write_json


class Bot(object):
    """
    This class is a template for building a telegram bot.
    """
    def __init__(self, environ_token):
        logger.info("Bot Started ...")
        self.bot = telebot.TeleBot(os.environ[environ_token], parse_mode=None)
        self.send_welcome =self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)

    def run(self):
        logger.info("Bot is running ...")
        self.bot.infinity_polling()

    def send_welcome(self, message):
        """
        A welcome message is sent to the user
        who has just hit the bot start button.
        """
        logger.info(f"Sending message to user = {message.from_user.id}")
        self.bot.reply_to(message, f"Hello {message.chat.first_name}!")

    def echo_all(self, message):
        """
        The user message is automatically returned.
        the appropriate keyboard is then sent the user.
        """
        logger.info(f"Sending message to user = {message.from_user.id}")
        self.bot.send_message(
         message.chat.id,
         emojize(message.text),
         reply_markup=keyboards.main,
         )
        #write_json('m.json', message.json)

if __name__ == "__main__":
    bot = Bot('NASHENAS_BOT_TOKEN')
    bot.run()
    logger.info("Done!")