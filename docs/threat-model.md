# Threat Model

LLMGuard-X is designed to operate safely as a defensive AI-SOC.

## Trust Boundaries
- **User Interface**: Untrusted. All inputs are validated at the Rust gateway.
- **Rust Gateway**: Partially trusted. Validates inputs, handles auth, forwards requests safely.
- **Python AI Engine**: Trusted environment. Only accessible from the Rust Gateway or internal network.

## Attack Surface
- **API Endpoints**: Protected by Rate Limiting and strict schema validation.
- **Security Tools Wrappers**: Command injection prevented by avoiding `shell=True` and strictly validating input formats (e.g. alphanumeric domain names).
- **LLM Prompt Injection**: The platform uses ML models (Transformers) to classify incoming prompts *before* they are sent to the LLM, neutralizing injection attempts.
