from transformers import pipeline

class URLClassifier:
    def __init__(self):
        self.model_name = "URL-Heuristics-Advanced"
        # In a real scenario, this could be a DistilBERT model fine-tuned on malicious URLs
        
    def analyze(self, url: str):
        url_lower = url.lower()
        suspicious_keywords = ["admin", "login", "cmd", "exec", "shell", ".php?", ".exe", "eval("]
        
        # Calculate a basic risk score
        risk_score = 10
        if len(url) > 100:
            risk_score += 20
        if len(url) > 200:
            risk_score += 30
            
        keyword_hits = sum(1 for kw in suspicious_keywords if kw in url_lower)
        risk_score += keyword_hits * 25
        
        risk_score = min(risk_score, 100)
        suspicious = risk_score > 50
        
        return {
            "model": self.model_name,
            "category": "URL_ANOMALY" if suspicious else "SAFE",
            "confidence": 0.85 if suspicious else 0.95,
            "risk": risk_score
        }

class PromptClassifier:
    def __init__(self):
        self.model_name = "ProtectAI/deberta-v3-base-prompt-injection-v2"
        try:
            # Try to load a real prompt injection detection model
            self.classifier = pipeline(
                "text-classification",
                model="ProtectAI/deberta-v3-base-prompt-injection-v2"
            )
            self.use_fallback = False
        except Exception:
            # Fallback if model cannot be loaded (e.g. no internet/transformers issue)
            self.use_fallback = True
            self.injection_keywords = ["ignore previous instructions", "bypass", "system prompt", "forget all", "do not follow", "you are now"]
        
    def analyze(self, prompt: str):
        if not self.use_fallback:
            try:
                result = self.classifier(prompt[:512])[0] # limit length for safety
                # Usually labels might be INJECTION or SAFE, depends on the model.
                # Assuming label "INJECTION" or similar. We map the score.
                is_injection = result['label'] == 'INJECTION' or result['score'] > 0.8
                score = result['score']
                risk = int(score * 100) if is_injection else int((1-score)*100)
                confidence = score
            except Exception:
                is_injection, confidence, risk = self._fallback_analyze(prompt)
        else:
            is_injection, confidence, risk = self._fallback_analyze(prompt)
        
        return {
            "model": self.model_name if not self.use_fallback else "Fallback-Heuristics",
            "category": "PROMPT_INJECTION" if is_injection else "SAFE",
            "confidence": round(confidence, 2),
            "risk": risk,
            "decision": "BLOCK" if is_injection else "ALLOW"
        }
        
    def _fallback_analyze(self, prompt: str):
        prompt_lower = prompt.lower()
        keyword_hits = sum(1 for kw in self.injection_keywords if kw in prompt_lower)
        is_injection = keyword_hits > 0
        confidence = min(0.6 + (keyword_hits * 0.15), 0.99) if is_injection else 0.98
        risk = min(50 + (keyword_hits * 20), 100) if is_injection else 5
        return is_injection, confidence, risk
