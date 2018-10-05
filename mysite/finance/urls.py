

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.login2,name="login2"),
    url(r'content2$',views.content2,name="content2"),
    url(r'menu2$',views.menu2,name="menu2"),
]