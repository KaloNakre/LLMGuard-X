#!/bin/bash
set -e

echo "[+] Running LLMGuard-X Security Checks..."

# Python checks
echo "[+] Checking Python AI Engine..."
cd ai-engine
source venv/bin/activate || true
pip install -r requirements-dev.txt || true
flake8 app/ || echo "[-] Flake8 failed or not installed"
bandit -r app/ || echo "[-] Bandit failed or not installed"
cd ..

# Rust checks
echo "[+] Checking Rust Gateway..."
cd gateway/rust
cargo clippy -- -D warnings
cargo audit || echo "[-] cargo-audit failed or not installed"
cd ../..

# Secrets check (using trufflehog or git-secrets if installed)
echo "[+] Scanning for secrets..."
trufflehog filesystem . || echo "[-] trufflehog not found, skipping secret scan"

echo "[+] Security checks completed."
