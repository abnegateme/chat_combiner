import argparse
from combiner_lib import get_dirs, get_chat

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="chat_combiner", description="combining chats"
    )

    parser.add_argument("path")
    parser.add_argument("-r", "--restricted", nargs="+", default=[])

    args = parser.parse_args()

    chats = []
    for dir in get_dirs(args.path, args.restricted):
        chats.append(get_chat(dir))

    for msg in chats[0]:
        print(msg)
        break
