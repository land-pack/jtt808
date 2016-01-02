def auth(func):
    def inner():
        print 'Before ...'
        func()
        print 'After ...'

    return inner


@auth
def func1():
    print 'hello ..'


if __name__ == '__main__':
    func1()
