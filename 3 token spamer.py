import requests

id = input("channel id: ")
msg = input("message: ")
no = int(input("num of message: "))
def send_message(token1, channel_id, message):
    url1 = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data1 = {"content": message}
    headers1 = {"authorization": token1}
    url2 = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data2 = {"content": message}
    headers2 = {"authorization": token2}
    url3 = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data3 = {"content": message}
    headers3 = {"authorization": token3}
    for _ in range(no):
        r = requests.post(url1, data=data1, headers=headers1)
        r = requests.post(url2, data=data2, headers=headers2)
        r = requests.post(url3, data=data3, headers=headers3)


token1 = "" #your token id
token2 = "" #your token id
token3 = "" #your token id
channel_id = id
message = msg
send_message(token1, channel_id, message)
