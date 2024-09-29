from os import makedirs, listdir
from os.path import dirname, abspath, exists, join as p_join, isdir
import combiner_lib


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


THIS_SCRIPT_PATH = dirname(abspath(__file__))
TEST_DIR = p_join(THIS_SCRIPT_PATH, "test")


def print_result(test_name, expression):
    if expression:
        print(f"{test_name} : {bcolors.OKGREEN}OK{bcolors.ENDC}")
    else:
        print(f"{test_name} : {bcolors.FAIL}FAIL{bcolors.ENDC}")


test_dirs = []

for dir in ["named_chat", "someChat", "grr11"]:
    if not exists(dir):
        makedirs(dir)
    test_dirs.append(p_join(TEST_DIR, dir))

#
res = combiner_lib.get_dirs(TEST_DIR)
print_result(
    "test get_dirs()",
    combiner_lib.get_dirs(TEST_DIR, [".*11"]) == test_dirs[:-1],
)
