import re
import json
from os import listdir, PathLike
from os.path import isdir, join as p_join, basename


def get_dirs(path: str | PathLike, restricted_regex: list = []) -> list[str]:
    if not isinstance(restricted_regex, list):
        raise TypeError

    content = [p_join(path, name) for name in listdir(path)]
    content = [path for path in content if isdir(path)]
    for regex in restricted_regex:
        regex = re.compile(regex)
        content = [path for path in content if not regex.match(basename(path))]

    return content


def get_chats(dirs: list) -> list[dict]:
    chats = []
    for dir in dirs:
        with open(p_join(dir, "result.json")) as _f:
            dump = json.load(_f)
            chats.append(dump)

    return chats
