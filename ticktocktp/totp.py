import pyotp
import time
import store

def get_code(name: str):
    try:
        secrets = store.load()
        totp = pyotp.TOTP(secrets[name])
        code = totp.now()
        seconds_left = 30 - int(time.time()) % 30
        return code, seconds_left
    except KeyError:
        raise ValueError(f"No account found named {name}.")

# code, seconds_left = get_code("test")
# print(f"{code} {seconds_left}s left")
# print(store.config_dir())
# print(store.load())