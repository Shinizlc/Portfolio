from telethon import TelegramClient, events, sync





from loguru import logger
@logger.catch
def send_message():
    #phone = 642041828473
    bot_token=''
    #receiver='shinizlc'
    with TelegramClient('session',4271659,'e67709a01806af2328f715a516b4cf07') as conn:
        conn.start()
        #entity = conn.get_entity(receiver)
        conn.send_message(entity=entity,message='Test')
send_message()