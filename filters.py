from bot.config import CONFIG


async def filter_tokens(tokens):

    filtered = []

    blacklist = CONFIG["filters"]["blacklist_tokens"]

    dev_blacklist = CONFIG["filters"]["blacklist_developers"]


    for t in tokens:

        symbol = t.get("symbol")

        dev = t.get("developer", "unknown")

        volume = t.get("volume", 0)


        if symbol in blacklist:

            continue

        if dev in dev_blacklist:

            continue

        if volume < CONFIG["filters"]["min_volume"]:

            continue


        filtered.append(t)

    return filtered
