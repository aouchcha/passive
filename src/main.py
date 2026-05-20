import argparse
import os
from social import searchWithUsername
from address_ip import searchForIp
from full_name import fullName

def main():
    parser = argparse.ArgumentParser(prog="passive", add_help=False, description="Welcome to passive v1.0.0")
    parser.add_argument("-fn", help="Search with full-name")
    parser.add_argument("-ip", help="Search with ip address")
    parser.add_argument("-u", help="Search with username")
    parser.add_argument("-h", "--help", help="Print help massage", action="store_true")
    args = parser.parse_args()

    if not any([args.fn, args.ip, args.u]) or args.help:
        printHelp()
        exit(0)

    if args.u:
        result = searchWithUsername(args.u)
    elif args.ip:
        result = searchForIp(args.ip)
    else:
        result = fullName(args.fn)
    print(result["data"])


main()

def printHelp():
    print(
    """
        Welcome to passive v1.0.0

        OPTIONS:
            -fn         Search with full-name
            -ip         Search with ip address
            -u          Search with username
    """
    )

def get_result_filename() -> str:
    if not os.path.exists("passive/result.txt"):
        return "passive/result.txt"
    n = 2
    while os.path.exists(f"passive/result{n}.txt"):
        n += 1
    return f"passive/result{n}.txt"
 
 
def save_result(content: str, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Saved in {filename}")