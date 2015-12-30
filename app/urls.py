import views
from core.urls import pattern

"""
dispatch method will return a Dicts to urlpatterns
and then,you can call 'view.register' by pickname 'register'
"""
urlpatterns = pattern(
        ('register', views.register),
        ('auth', views.auth),
        ('unregister',None)
)

if __name__ == '__main__':
    print urlpatterns
