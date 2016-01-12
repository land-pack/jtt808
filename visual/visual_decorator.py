# Read color for error information!
def yellow_decorate(f):
    def wrapper(x):
        print '\033[1;33;40m'
        print '*' * 50
        f(x)
        print '*' * 50
        print '\033[0m'

    return wrapper


def blue_decorate(f):
    def wrapper(x):
        print '\033[1;34;40m'
        print '*' * 50
        f(x)
        print '*' * 50
        print '\033[0m'

    return wrapper


def red_decorate(f):
    def wrapper(x):
        print '\033[1;31;40m'
        print '*' * 50
        f(x)
        print '*' * 50
        print '\033[0m'

    return wrapper


@red_decorate
def error(val):
    print '[Error]\t', val


@blue_decorate
def info(val):
    print '[Info]\t', val


@yellow_decorate
def warning(val):
    print '[Warn]\t', val


if __name__ == '__main__':
    error("The data format error")
    warning("The data is not complete")
    info('connect from 192.168.0.76')
