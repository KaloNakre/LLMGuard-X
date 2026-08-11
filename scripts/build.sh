#!/bin/bash
set -e

echo "[+] Building LLMGuard-X Enterprise..."

# Build Frontend
echo "[+] Building Frontend..."
cd frontend
npm run build
cd ..

# Build Rust Gateway
echo "[+] Building Rust Gateway..."
cd gateway/rust
cargo build --release
cd ../..

echo "[+] Build complete."
