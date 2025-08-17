# Rolls Royce Trading Bot 🚀

A fully automated crypto trading bot that integrates:

- DexScreener + Pump.fun
- RugCheck.xyz API
- Pocket Universe fake volume checks
- On-chain enrichment (Etherscan, BscScan, BaseScan, Solscan)
- Filters + Blacklists
- Auto Buy/Sell with profit targets + stop-loss
- Telegram notifications
- Docker + GitHub CI/CD ready

## 🔧 Setup

1. Clone repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/trading-bot.git
   cd trading-bot

    Install deps:

pip install -r requirements.txt


    Add your keys to config/.env.

    Run bot:

python bot/main.py
