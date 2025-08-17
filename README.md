# Trading Bot 🚀

This bot fetches tokens from DexScreener and Pump.fun, filters them,
checks rug risks with RugCheck, verifies fake volume with Pocket Universe,
runs on-chain enrichment (Etherscan, BscScan, BaseScan, Solscan),
and auto-trades via BonkBot with Telegram alerts.

---

## Features
- ✅ DexScreener + Pump.fun fetchers
- ✅ RugCheck API integration
- ✅ Pocket Universe fake-volume detection
- ✅ Blacklist for coins & developers
- ✅ On-chain enrichment (Etherscan, Solscan, etc.)
- ✅ Auto-buy / auto-sell with 20–30% profit target
- ✅ Stop-loss at 15%
- ✅ Telegram real-time alerts
- ✅ Docker + GitHub Actions ready

---

## 🔧 Installation

### Windows (PowerShell)
```powershell
git clone https://github.com/YOUR_USERNAME/trading-bot.git
cd trading-bot
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
python bot/main.py
