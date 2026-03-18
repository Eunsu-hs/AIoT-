import telepot
import time

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print("chat_id:",chat_id)
    bot.sendMessage(chat_id, 'id:'+str(chat_id))

my_token = '5400967414:AAEmAvwaQF6du8gny7A9upRniGvtHOi-Ro0' # 토큰 입력
bot = telepot.Bot(my_token)

bot.message_loop(handle)

while True:
    time.sleep(10)
