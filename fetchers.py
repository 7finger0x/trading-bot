import aiohttp

import logging


logger = logging.getLogger("fetchers")


DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/tokens"

PUMPFUN_URL = "https://api.pump.fun/v1/tokens"


async def fetch_new_tokens():

    tokens = []

    async with aiohttp.ClientSession() as session:

        try:

            async with session.get(DEXSCREENER_URL) as r:

                data = await r.json()

                tokens.extend(data.get("pairs", []))

        except Exception as e:

            logger.error(f"DexScreener fetch error: {e}")


        try:

            async with session.get(PUMPFUN_URL) as r:

                data = await r.json()

                tokens.extend(data.get("tokens", []))

        except Exception as e:

            logger.error(f"Pump.fun fetch error: {e}")


    return tokens
