Write-Output "Setting up Rolls Royce Trading Bot..."

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

Write-Output "Setup complete. Run 'python bot/main.py' to start."
