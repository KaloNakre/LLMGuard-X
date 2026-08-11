# Architecture

The LLMGuard-X platform is built on a polyglot microservice architecture designed for high performance, security, and extensibility.

## Components
1. **Frontend**: Next.js Dashboard
2. **Rust Gateway**: Axum API server routing requests and handling fast security verification.
3. **Python AI Engine**: FastAPI service wrapping Transformer models and LLM integration.
4. **Database**: PostgreSQL (or SQLite).

## Real-Time Event Stream
The frontend receives updates in real-time via WebSocket/SSE connections exposed by the Rust Gateway. This ensures that operators can immediately see threats as they are detected by the ML models.
