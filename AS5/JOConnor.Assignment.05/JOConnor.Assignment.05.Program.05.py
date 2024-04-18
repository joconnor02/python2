def make_bold(fn):
    def wrapper(args):
        return '\033[1m' + fn(str(args)) + '\033[0m'
    return wrapper


def make_italic(fn):
    def wrapper(args):
        return '\033[3m' + fn(str(args)) + '\033[0m'
    return wrapper


def make_underline(fn):
    def wrapper(args):
        return '\033[4m' + fn(str(args)) + '\033[0m'
    return wrapper


@make_bold
@make_italic
@make_underline
def print_message(m):
    return m


def main():
    m = "hello world"
    print(f"Original Message: {m}")
    print(f"Modified Message:", print_message(m))


main()
