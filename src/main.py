import argparse
from social import searchWithUsername

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
        searchWithUsername(args.u)


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