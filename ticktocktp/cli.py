import argparse
import totp
import store
import time

def main():
    parser = argparse.ArgumentParser(prog="ticktocktp")
    subparsers = parser.add_subparsers(dest="command", required=True)

    get_parser = subparsers.add_parser("get", help="Print the current code for an account")
    get_parser.add_argument("name", help="Account name")

    add_parser = subparsers.add_parser("add", help="Add an account")
    add_parser.add_argument("name", help="Account name")
    add_parser.add_argument("secret", help="OTP secret")

    list_parser = subparsers.add_parser("list", help="List the current codes for all accounts")

    args = parser.parse_args()

    if args.command == "get":
        try:
            code, seconds_left = totp.get_code(args.name)
            print(f"{code} {seconds_left}s left")
        except ValueError as ex:
            print(ex)
    elif args.command == "add":
        existing = store.load()
        is_update = args.name in existing
        if is_update:
            choice = input("Overwrite? (y/n): ").lower()
            if choice != "y":
                print("Operation cancelled.")
                return

        try:
            store.add_secret(args.name, args.secret)
            print("Account updated succesfully!" if is_update else "Account added succesfully!")
        except Exception as ex:
            print("idk how you got here, but heres an error message ig???")
            print(f"ERROR: {ex}")
    elif args.command == "list":
        secrets = store.load()

        for name in secrets.keys():
            code, seconds_left = totp.get_code(name)
            print(f"{name}: {code} {seconds_left}s left")

main()