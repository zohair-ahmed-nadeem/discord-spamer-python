import requests


token = input("your token: ")
id = input("channal id: ")
msg = input("your message: ")
num = int(input("numbers of messages: "))

def send_message(token, channel_id, message):
    url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    headers = {"authorization": token}

    for _ in range(num):
        r = requests.post(url, data=data, headers=headers)

channel_id = id
message = msg
send_message(token, channel_id, message)
