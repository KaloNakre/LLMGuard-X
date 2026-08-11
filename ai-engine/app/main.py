from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from models.transformer_model import URLClassifier, PromptClassifier

app = FastAPI(title="LLMGuard-X AI Engine")

url_classifier = URLClassifier()
prompt_classifier = PromptClassifier()

class URLRequest(BaseModel):
    url: str

class PromptRequest(BaseModel):
    prompt: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/analyze/url")
def analyze_url(req: URLRequest):
    result = url_classifier.analyze(req.url)
    return result

@app.post("/api/analyze/prompt")
def analyze_prompt(req: PromptRequest):
    result = prompt_classifier.analyze(req.prompt)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
