import argparse
import totp

def main():
    parser = argparse.ArgumentParser(prog="ticktocktp")
    subparsers = parser.add_subparsers(dest="command", required=True)

    get_parser = subparsers.add_parser("get", help="Print the current code for an account")
    get_parser.add_argument("name", help="Account name")

    args = parser.parse_args()

    if args.command == "get":
        try:
            code, seconds_left = totp.get_code(args.name)
            print(f"{code} {seconds_left}s left")
        except ValueError as ex:
            print(ex)

main()