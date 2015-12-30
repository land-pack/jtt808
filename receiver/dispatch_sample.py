from core.urls import pattern


def hey_fun(request):
    print 'the request is ', request


def bye_fun(request):
    print 'bye, see you !'


urlpatterns = pattern(
        ('hey', hey_fun),
        ('bye', bye_fun)
)


def reflect(flag, request):
    urlpatterns[flag](request)


def dispatch_sample(flag, request):
    if flag:
        reflect(flag, request)


if __name__ == '__main__':
    dispatch_sample('bye', 'i am request')
