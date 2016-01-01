import views
from core.urls import pattern

"""
dispatch method will return a Dicts to urlpatterns
and then,you can call 'view.register' by nickname 'register'
"""
urlpatterns = pattern(
        ('ser_reg_rsp', views.register),
        ('ter_aut_rep', views.auth),
)

if __name__ == '__main__':
    print urlpatterns
