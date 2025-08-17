import aiohttp


class TelegramNotifier:

    def __init__(self, bot_token, chat_id):

        self.bot_token = bot_token

        self.chat_id = chat_id


    async def send_message(self, text):

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

        async with aiohttp.ClientSession() as session:

            await session.post(url, json={"chat_id": self.chat_id, "text": text})


