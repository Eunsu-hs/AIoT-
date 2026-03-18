import telepot
import requests
from bs4 import BeautifulSoup
import time

telegram_id = '730238165'
my_token = '5400967414:AAEmAvwaQF6du8gny7A9upRniGvtHOi-Ro0'
 
bot = telepot.Bot(my_token)

def get_price(com_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + com_code
    result = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    bs_obj = BeautifulSoup(result.content, "html.parser")
    no_today = bs_obj.find("p", {"class":"no_today"})
    blind_now = no_today.find("span", {"class":"blind"})
    return blind_now.text

try:
    while True:
        msg = "삼성전자의 현재가격은 " + get_price("005930") + " 입니다"
        print(msg)
        bot.sendMessage(chat_id = telegram_id, text = msg)
        time.sleep(60000*10)

except KeyboardInterrupt:
    pass