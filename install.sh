#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "==========================================="
echo "Starting YouTube Downloader Setup...       - Meetsoni555"
echo "==========================================="

# 1. Update system and install Google Chrome using yay
if command -v yay &> /dev/null; then
    echo "[1/4] Detected 'yay'. Installing Google Chrome..."
    yay -S --noconfirm google-chrome
else
    echo "Error: 'yay' package manager is not installed."
    echo "Please install Google Chrome manually and then rerun this script."
    exit 1
fi

# 2. Setup Python Virtual Environment
echo "[2/4] Setting up Python virtual environment..."
if [ -d "myvenv" ]; then
    echo "Virtual environment 'myvenv' already exists. Skipping creation."
else
    python -m venv myvenv
fi

# 3. Activate environment and install dependencies
echo "[3/4] Activating environment and installing Selenium..."
source myvenv/bin/activate
pip install --upgrade pip
pip install selenium

# 4. Create an executable launcher
echo "[4/4] Creating executable launcher 'run.sh'..."
cat << 'EOF' > run.sh
#!/bin/bash
source myvenv/bin/activate
python youtube.py
EOF

# Make run.sh executable
chmod +x run.sh

echo "==========================================="
echo "Setup complete!"
echo "To run the script in the future, just type: ./run.sh"
echo "==========================================="
