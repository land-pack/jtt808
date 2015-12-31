from core.urls import pattern

"""
Here, have both function for call!
and each guys reflect by a name!
"""


def hey_fun(request):
    print 'the request is ', request
    request.sendall('hey! see you again!')


def bye_fun(request):
    print 'bye, see you !'
    request.sendall('okay!see you')


"""
You can see,each function have a nickname!
"""
urlpatterns = pattern(
        ('hey', hey_fun),
        ('bye', bye_fun)
)


def reflect(flag, request):
    urlpatterns[flag](request)


"""
flag is a key of function Dicts!
"""


def dispatch_sample(flag, request):
    if flag:
        reflect(flag, request)


if __name__ == '__main__':
    dispatch_sample('bye', 'i am request')
