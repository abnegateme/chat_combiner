import re
import json
import datetime
from os import listdir, PathLike
from os.path import isdir, join as p_join, basename

from dateparser import parse as dt_parse
from collections.abc import Iterator


class Chat(Iterator):
    def __init__(self, dump: dict):
        self._dump = dump["messages"]
        self._name = dump["name"]
        self._index = 0

        self.first_date = dt_parse(self._dump[0]["date"])
        self.last_date = dt_parse(self._dump[-1]["date"])

    def __next__(self):
        if self._index < len(self._dump):
            item = self._dump[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


def get_dirs(path: str | PathLike, restricted_regex: list = []) -> list[str]:
    if not isinstance(restricted_regex, list):
        raise TypeError

    content = [p_join(path, name) for name in listdir(path)]
    content = [path for path in content if isdir(path)]
    for regex in restricted_regex:
        regex = re.compile(regex)
        content = [path for path in content if not regex.match(basename(path))]

    return content


def get_chat(dir: str) -> Chat:
    with open(p_join(dir, "result.json")) as _f:
        dump = json.load(_f)

    return Chat(dump=dump)


def date_generator(from_date, to_date):
    while from_date <= to_date:
        yield from_date
        from_date = from_date + datetime.timedelta(days=1)
