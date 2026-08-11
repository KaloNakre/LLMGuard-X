<div align="center">
  <img src="assets/hero_banner.png" alt="LLMGuard-X Hero Banner" width="800"/>
</div>

# LLMGuard-X Enterprise

An AI-powered security operations and real-time verification platform for Large Language Models. Features an intelligent LLM gateway (Rust), an AI classification engine (Python/Transformers), and a real-time security dashboard (Next.js).

## Features
- AI-Powered LLM Security Gateway
- Real-Time Web Verification
- Security Operations Dashboard

## Architecture
- **Frontend**: Next.js Dashboard
- **Gateway**: Rust (Axum, Tokio)
- **AI Engine**: Python (FastAPI, Transformers)
- **Database**: PostgreSQL (or SQLite local)

## Quickstart
1. Clone the repository
2. Run `docker-compose up -d`
3. Access Dashboard at `http://localhost:3000`
