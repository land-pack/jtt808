"""
If your get a SIG_TSTP signal,(CTRL+Z)
and it's will get a input windows!
ask you input some command!
"""
from conf.rest import SOCKET_DESCRIPTOR
from visual.visual_decorator import display_color
from app.urls import urlpatterns
from app import views


@display_color('cyan')
def hello(a, b):
    print '[1] Checking the terminal information'
    print '[2] Setting the terminal'
    print '[3] Do something else!'
    cmd = raw_input('Please input cmd your :')
    if cmd == 1:
        urlpatterns['position'] = views.get_ter_info
    else:
        print 'No match command!'
