import subprocess
import re

def is_valid_domain(domain: str) -> bool:
    return bool(re.match(r'^[a-zA-Z0-9.-]+$', domain))

def run_openssl_check(domain: str):
    """Safe wrapper for openssl s_client to check TLS."""
    if not is_valid_domain(domain):
        raise ValueError("Invalid domain format.")
        
    cmd = ["openssl", "s_client", "-connect", f"{domain}:443", "-brief"]
    try:
        # Pass quit to stdin to ensure it doesn't hang
        result = subprocess.run(cmd, input="Q\n", capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.output
    except FileNotFoundError:
        return "openssl not installed."
