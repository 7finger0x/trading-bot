import aiohttp

from bot.config import CONFIG


ETHERSCAN = "https://api.etherscan.io/api"

BSCSCAN = "https://api.bscscan.com/api"

BASESCAN = "https://api.basescan.org/api"

SOLSCAN = "https://public-api.solscan.io"


async def enrich_token_data(token):

    enriched = token.copy()

    # Example: fetch top holders from Etherscan

    async with aiohttp.ClientSession() as session:

        if token.get("chain") == "ETH":

            url = f"{ETHERSCAN}?module=token&action=tokenholderlist&contractaddress={token['address']}&apikey={CONFIG['apis']['etherscan']}"

            async with session.get(url) as r:

                enriched["holders"] = await r.json()

    return enriched
