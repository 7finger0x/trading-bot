import aiohttp


POCKET_API = "https://api.pocketuniverse.app/v1/volume"


async def verify_volume(token):

    async with aiohttp.ClientSession() as session:

        url = f"{POCKET_API}?address={token['address']}"

        async with session.get(url) as r:

            data = await r.json()

            return not data.get("fake_volume", False)
