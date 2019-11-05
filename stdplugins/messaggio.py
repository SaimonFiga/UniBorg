from telethon import TelegramClient, events

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'bene' in event.raw_text:
        await event.reply('/scommessa 5000')

client.start()
client.run_until_disconnected()
