import requests


id = input("channel id: ")
msg = input("message: ")
no = int(input("num of message: "))

def send_message1(token1, channel_id, message):
    url1 = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data1 = {"content": message}
    headers1 = {"authorization": token1}
    url2 = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data2 = {"content": message}
    headers2 = {"authorization": token2}
    for _ in range(no):
        r = requests.post(url1, data=data1, headers=headers1)
        r = requests.post(url2, data=data2, headers=headers2)

token1 = ""#your token id
token2 = ""#your token id
channel_id = id
message = msg
send_message1(token1, channel_id, message)
