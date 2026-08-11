import subprocess
import re

def is_valid_domain(domain: str) -> bool:
    return bool(re.match(r'^[a-zA-Z0-9.-]+$', domain))

def run_dig(domain: str):
    """Safe wrapper for dig to get DNS records."""
    if not is_valid_domain(domain):
        raise ValueError("Invalid domain format.")
        
    cmd = ["dig", "+short", domain]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.output
    except FileNotFoundError:
        return "dig not installed."
