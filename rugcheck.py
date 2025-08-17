import aiohttp


RUGCHECK_API = "https://api.rugcheck.xyz/v1/tokens"


async def rugcheck_verify(token):

    async with aiohttp.ClientSession() as session:

        url = f"{RUGCHECK_API}/{token['address']}"

        async with session.get(url) as r:

            data = await r.json()

            return data.get("status") == "good" and not data.get("bundled", False)
