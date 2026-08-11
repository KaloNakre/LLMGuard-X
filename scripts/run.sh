#!/bin/bash
set -e

echo "[+] Starting LLMGuard-X Enterprise..."
docker-compose up -d --build
echo "[+] Services started. Dashboard available at http://localhost:3000"
