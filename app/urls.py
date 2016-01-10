import views
from core.urls import pattern

"""
the urls control where are the request goes!
dispatch method will return a Dicts to urlpatterns
and then,you can call 'view.register' by nickname 'register'
"""
urlpatterns = pattern(
        ('ser_reg_rsp', views.register),
        ('ter_aut_req', views.auth),
        ('position', views.position)
)

if __name__ == '__main__':
    print urlpatterns
