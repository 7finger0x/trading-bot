import random

from bot.config import CONFIG


class TradingEngine:

    def __init__(self, config, notifier):

        self.config = config

        self.notifier = notifier


    async def auto_trade(self, token):

        buy_price = token.get("price_usd", 0)

        amount = self.config["trading"]["trade_amount_usd"]

        await self.notifier.send_message(f"💰 Buying {amount}$ of {token['symbol']} at {buy_price}")


        target_profit = self.config["filters"]["profit_threshold"]

        stop_loss = self.config["filters"]["stop_loss"]


        # Mock price monitor loop

        current_price = buy_price

        while True:

            change = random.uniform(-0.1, 0.1)

            current_price *= (1 + change)


            if (current_price - buy_price) / buy_price >= target_profit:

                await self.notifier.send_message(f"📈 Selling {token['symbol']} at profit target {target_profit*100}%")

                break

            if (buy_price - current_price) / buy_price >= stop_loss:

                await self.notifier.send_message(f"📉 Selling {token['symbol']} at stop loss {stop_loss*100}%")

                break
