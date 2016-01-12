def route_to(arg):
    def _route_to(func):
        def __route_to(request):
            print 'do something ...'
            func(request)
            print 'do some another ...'

        return __route_to

    return _route_to


@route_to('position')
def position_view(request):
    pass


if __name__ == '__main__':
    pass
