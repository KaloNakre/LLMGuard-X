import subprocess
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme in ('http', 'https'), result.netloc])
    except ValueError:
        return False

def run_curl_check(url: str):
    """Safe wrapper for curl. Extracts headers only."""
    if not is_valid_url(url):
        raise ValueError("Invalid URL format.")
        
    cmd = ["curl", "-I", "-s", "--max-time", "5", url]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.output
    except FileNotFoundError:
        return "curl not installed."
