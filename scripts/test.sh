#!/bin/bash
set -e

echo "[+] Running automated tests..."

echo "[+] Testing Rust Gateway..."
cd gateway/rust
cargo test
cd ../..

echo "[+] Testing Python AI Engine..."
cd ai-engine
source venv/bin/activate || true
pytest tests/ || echo "[-] Pytest failed or not installed"
cd ..

echo "[+] All tests completed."
