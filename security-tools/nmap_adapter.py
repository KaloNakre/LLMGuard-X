import subprocess
import re

def is_valid_target(target: str) -> bool:
    # Strict validation: only allow alphanumeric, dots, and hyphens (basic hostname/IP)
    return bool(re.match(r'^[a-zA-Z0-9.-]+$', target))

def run_nmap_scan(target: str):
    """Safe wrapper for nmap. Only runs specific fast scan."""
    if not is_valid_target(target):
        raise ValueError("Invalid target format.")
        
    # No shell=True! Fixed arguments.
    cmd = ["nmap", "-T4", "-F", target]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.output
    except FileNotFoundError:
        return "nmap not installed on this system."
