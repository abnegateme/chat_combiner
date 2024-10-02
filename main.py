from os import makedirs
from os.path import exists, join as p_join
import argparse
from combiner_lib import get_dirs, get_chat, date_generator

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

    min_date = min([chat.first_date for chat in chats]).date()
    max_date = max([chat.last_date for chat in chats]).date()

    print(min_date, max_date)

    result_dir = p_join(args.path, "result")
    if not exists(result_dir):
        makedirs(result_dir)

    date_range = date_generator(min_date, max_date)
    for x in range(3):
        print(next(date_range))
