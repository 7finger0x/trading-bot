# 🚀 Rolls Royce AI Trading Bot


A fully automated AI-powered crypto trading bot that scans **DexScreener, Pump.fun, RugCheck.xyz, Pocket Universe, and on-chain explorers** to:

- Detect new tokens

- Filter out scams/rugs/fake volume

- Auto-buy and auto-sell with profit/loss management

- Integrate with **Telegram** (BonkBot trading + live alerts)


---


## ✨ Features

- DexScreener + Pump.fun token fetching

- RugCheck & PocketUniverse API integration

- On-chain enrichment (Etherscan, BscScan, BaseScan, SolScan)

- Fake volume detection

- Auto-trading (buy/sell, profit target 20–30%, stop-loss 15%)

- Telegram notifications + BonkBot integration

- Real-time price monitoring

- Configurable via `config.json`


---


## ⚡ Quick Setup


### 🔹 Windows (Batch)

```bat

setup.bat


🔹 Windows (PowerShell)


.\setup.ps1


🔹 Linux / Mac


bash scripts/deploy.sh



⸻


🐳 Docker Setup


docker build -t trading-bot .

docker run -d --name bot trading-bot



⸻


⚙️ Config


Edit config.json to set your:

• API keys (Etherscan, SolScan, etc.)

• Telegram bot token

• Filters (profit %, stop-loss %, volume thresholds)


⸻


🧪 Testing


pytest tests/
