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


Linux/Mac


git clone https://github.com/YOUR_USERNAME/trading-bot.git

cd trading-bot

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python bot/main.py


Docker


docker-compose up --build -d



⸻


📲 Config


Edit bot/config.json with your API keys and settings.


⸻


⚡ Deploy

• Push to GitHub

• GitHub Actions (.github/workflows/python-app.yml) auto-tests it.

• You can run it on any server or via Docker.


---


# 📄 **5. `deploy.ps1`** (Windows PowerShell install script)

```powershell

Write-Output "🚀 Setting up Trading Bot on Windows..."

python -m venv venv

.\venv\Scripts\Activate

pip install --upgrade pip

pip install -r requirements.txt

python bot/main.py



⸻


📄 6. deploy.sh (Linux/Mac install script)


#!/bin/bash

echo "🚀 Setting up Trading Bot..."

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

python bot/main.py



⸻


📄 7. Dockerfile


FROM python:3.11-slim


WORKDIR /app

COPY . /app


RUN pip install --upgrade pip && pip install -r requirements.txt


CMD ["python", "bot/main.py"]



⸻


📄 8. docker-compose.yml


version: "3.8"

services:

  trading-bot:

    build: .

    container_name: trading-bot

    restart: always

    volumes:

      - .:/app

    environment:

      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}

      - TELEGRAM_CHAT_ID=${TELEGRAM_CHAT_ID}



⸻


📄 9. .github/workflows/python-app.yml


name: Python Bot CI


on:

  push:

    branches: [ "main" ]

  pull_request:

    branches: [ "main" ]


jobs:

  build:

    runs-on: ubuntu-latest

    steps:

    - uses: actions/checkout@v3

    - name: Set up Python

      uses: actions/setup-python@v4

      with:

        python-version: "3.11"

    - name: Install dependencies

      run: |

        python -m pip install --upgrade pip

        pip install -r requirements.txt

    - name: Lint

      run: |

        python -m compileall .



⸻


✅ Now you have:

• All .py scripts

• Config files

• Setup scripts (deploy.ps1, deploy.sh)

• GitHub workflow

• Docker support

• Full GitHub-ready structure
