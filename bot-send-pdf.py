from datetime import *
from email import message
from pytz import *
from telegram import *
from telegram.ext import *

semanaEnviar = {
    "29-08":[],
}   

#Zona del tiempo y hora

today = datetime.now(timezone('America/Caracas'))
today_string = today.strftime("%d-%m")

#Informacion Telegram Bot y Chat

API_Key = "5471229694:AAET621gdTd88ZDDgezqffp7hyvS0LC3gkw"
CHAT_ID = "-1001728713111"
CHAT_ID2 = "-1001532789642"

bot = Bot(API_Key)
updater = Updater(API_Key, use_context=True)
updater.start_polling()

if today_string in semanaEnviar:
    document =open('pdftest.pdf', 'rb')
    bot.send_document(
        chat_id = CHAT_ID2,
        document = document
    )

updater.stop()