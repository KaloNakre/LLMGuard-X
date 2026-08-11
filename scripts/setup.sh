#!/bin/bash
set -e

echo "[+] Setting up LLMGuard-X Enterprise..."

# Frontend
echo "[+] Installing frontend dependencies..."
cd frontend && npm install
cd ..

# Python AI Engine
echo "[+] Setting up Python AI engine..."
cd ai-engine
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Rust Gateway
echo "[+] Setting up Rust gateway..."
cd gateway/rust
cargo build
cd ../..

echo "[+] Setup complete!"
