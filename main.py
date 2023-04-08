import re
import time

from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.types import Channel, InputPeerChannel, InputPeerChat, InputPeerSelf

# Use your own values from my.telegram.org
api_id = 28921419
api_hash = '8aca63a102fec741ebf418074c070499'

client = TelegramClient('anon2', api_id, api_hash)

lst_channel = 'scanmmovn;congdongfbtool;fbmarketisocial;SHOP2FA;trieuvia;FSpammer;okscanw;GroupiSocial;tricksandtipsbuysell;chonguyenlieuisocial;CongDongIsocialTuDo;AdbreakUnderground;iforumfacebookblack;VOIADSviaBMXMDN;clonermmo;FacebookVietNam;congdongfacebookvietnam;bmgiare;bangkinggruop;adstichxank;CheckScammer;congdongscanviavietnam;HGN_B4NKLOG;kenhscan'


def forward_message_toChat(client: TelegramClient, arr: []):
    self_peer = InputPeerSelf()
    messages = client.get_messages(self_peer, limit=1)
    latest_message = messages[0]

    for i in range(len(arr) - 1, -1, -1):
        #     reversed_arr.append(arr[i])
        # for channel_str in arr:
        username = str(arr[i])
        try:
            client(JoinChannelRequest(username))
            # dialogs = client.get_dialogs(limit=1)
            print(" wirte to channel name" + username)
            client(ForwardMessagesRequest(
                from_peer=client.get_input_entity(self_peer),
                id=[latest_message.id],
                to_peer=client.get_input_entity(username)
            ))
            print(" wirte to channel name" + username + ' Successfully')
            time.sleep(30)
        except Exception as e:
            print(f'write to channel {username} error {e}')
            error: str = str(e)
            if error.__contains__('wait'):
                wait_time = re.findall("[0-9]{3}", str(e))[0]
                print(f'waiting ... {wait_time}')
                time.sleep(int(wait_time))
            else:
                continue


def main():
    # Getting information about yourself
    me = client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    arr: [] = lst_channel.split(';')

    forward_message_toChat(client, arr)

    # invite_link = ';fbmarketisocial'
    # channel: Channel = client.get_entity('fbmarketisocial')
    # # Get the chat ID of the group
    # print('channel name ' + channel.username)
    # # chat = channel.chats[0]
    # # chat_id = chat.id
    # channel_id = str(channel.id)
    # print("join Channel id" + channel_id)
    #
    # # Join the group
    # client(JoinChannelRequest('smartviatool'))
    #
    # print('Successfully joined the group!')

    # You can print all the dialogs/conversations that you are part of:
    # for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself kkk !')
    # ...to some chat ID
    # await client.send_message(-100123456, 'Hello, group!')
    # ...to your contacts
    # await client.send_message('+34600123123', 'Hello, friend!')
    # ...or even to any username
    # await client.send_message('daomanh97', 'Testing Telethon!')

    # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )

    # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)

    # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')

    # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')


with client:
    main()
