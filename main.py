import argparse
from combiner_lib import get_dirs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="chat_combiner", description="combining chats"
    )

    parser.add_argument("path")
    parser.add_argument("-r", "--restricted", nargs="+", default=[])

    args = parser.parse_args()

    print(get_dirs(args.path, args.restricted))
