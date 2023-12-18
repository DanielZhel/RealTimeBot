import requests

def send_noti(message):
    TOKEN = "6069140994:AAFtHiqZ_7VOUr5a4sYMmOpJqsMJffh1qBU"
    chat_id = "762771346"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

    requests.get(url)


