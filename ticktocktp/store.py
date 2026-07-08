from pathlib import Path
import json

def config_dir():
    # project root = ../../ from this file (ticktocktp/ticktocktp/store.py -> ticktocktp/)

    root = Path(__file__).resolve().parent.parent
    path = root / "config"
    path.mkdir(parents=True, exist_ok=True)
    return path

def load():
    try:
        with open(config_dir() / "secrets.json", 'r') as f:
            secrets = json.load(f)
        return secrets
    except FileNotFoundError:
        return {}


def save(secrets):
    with open(config_dir() / "secrets.json", 'w') as f:
        json.dump(secrets, f)