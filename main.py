import asyncio

from bot.fetchers import fetch_new_tokens

from bot.filters import filter_tokens

from bot.enrichment import enrich_token_data

from bot.rugcheck import rugcheck_verify

from bot.trading import TradingEngine

from bot.telegram_bot import TelegramNotifier

from bot.config import CONFIG


async def main():

    notifier = TelegramNotifier(CONFIG["telegram"]["bot_token"], CONFIG["telegram"]["chat_id"])

    trading_engine = TradingEngine(CONFIG, notifier)


    await notifier.send_message("🚀 Bot started and monitoring tokens...")


    while True:

        try:

            tokens = await fetch_new_tokens()

            filtered = await filter_tokens(tokens)


            for token in filtered:

                enriched = await enrich_token_data(token)

                rugcheck_passed = await rugcheck_verify(enriched)


                if rugcheck_passed:

                    await notifier.send_message(f"✅ Token Passed Filters: {enriched['symbol']}")

                    if CONFIG["trading"]["auto_buy"]:

                        await trading_engine.auto_trade(enriched)

        except Exception as e:

            await notifier.send_message(f"⚠️ Error: {str(e)}")

        await asyncio.sleep(30)


if __name__ == "__main__":

    asyncio.run(main())



⸻


