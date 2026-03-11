from telethon import TelegramClient
api_id = 32561277
api_hash = '426cd88d36ba6f077b473f34f8d08376'

client = TelegramClient('promofinder', api_id, api_hash)
async def main():
    me = await client.get_me()
    print(me.first_name)
with client:
    client.loop.run_until_complete