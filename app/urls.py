import views
from core.urls import pattern

"""
the urls control where are the request goes!
dispatch method will return a Dicts to urlpatterns
and then,you can call 'view.register' by nickname 'register'
If you have emergency thing to do,you can reset the value of Dicts
Example, when the position run on the views.position,you want to
get terminal information,so on the linux, CTRL+Z will raise a TSTIP
signal,and then process catch it, and do some change to urlpatterns
so you can make position run on the views.terminal_info ....
"""
urlpatterns = pattern(
        ('ser_reg_rsp', views.register),
        ('ter_aut_req', views.auth),
        ('position', views.position),
        ('get_ter_info_rsp', views.terminal_info),
        ('get_ter_attr_rsp', views.terminal_attr)
)

if __name__ == '__main__':
    print urlpatterns
