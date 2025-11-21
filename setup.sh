#!/bin/bash

set -e

echo "Setting up PerformanceBot..."

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create backend run script
cat <<EOF > backend/run_backend.sh
#!/bin/bash
source venv/bin/activate
sudo venv/bin/uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
EOF
chmod +x backend/run_backend.sh

# Create bot run script
cat <<EOF > bot/run_bot.sh
#!/bin/bash
source venv/bin/activate
python -m bot.bot
EOF
chmod +x bot/run_bot.sh

echo "Setup complete."
echo "To run the backend: ./backend/run_backend.sh"
echo "To run the bot: ./bot/run_bot.sh"