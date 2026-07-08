import pyotp
import time
import store

def get_code(secret: str):
    totp = pyotp.TOTP(secret)
    code = totp.now()
    seconds_left = 30 - int(time.time()) % 30
    return code, seconds_left

test_secret = "JBSWY3DPEHPK3PXP"
code, seconds_left = get_code(test_secret)
print(f"{code} {seconds_left}s left")
print(store.config_dir())
print(store.load())