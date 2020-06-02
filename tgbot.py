import requests
import datetime


token = '1205073223:AAH6n2DzHOFTBuL102WxYWFvOeguoEKlLZ4'
url = f'https://api.telegram.org/bot{token}/'
class MyTgBot:
    

    def __init__(self, token):
        self.token = token
        self.url = f'https://api.telegram.org/bot{token}/'




    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.url + method, params)
        result_json = resp.json()['result']
        return result_json


    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.url + method, params=params)
        
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update



my_bot = MyTgBot(token)
greetings = ('привет', 'прив', 'добрый день', ' доброе утро', 'добрый вечер', 'доброй ночи', 'здравствуй')
now = datetime.datetime.now()

def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        my_bot.get_updates(new_offset)
        
        last_update = my_bot.get_last_update()


        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            my_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1
         
        if last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            my_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1
         
        if last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 24:
            my_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            today += 1
            
        if last_chat_text.lower() in greetings and today == now.day and 0 <= hour < 6:
            my_bot.send_message(last_chat_id, ' Доброй ночи, {}'.format(last_chat_name))
            today += 1
        
          

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
        
    except KeyboardInterrupt:
        exit    
